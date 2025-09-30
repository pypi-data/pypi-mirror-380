from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Awaitable, Callable, Dict, List, Optional, Set
from uuid import uuid4

from playwright.async_api import Browser, BrowserContext, Frame, Page, async_playwright


@dataclass
class BrowsingEvent:
    """Represents a captured page snapshot or lifecycle event."""

    timestamp: str
    page_id: str
    url: str
    title: str
    event_type: str
    html_path: Optional[str]
    status: Optional[int]
    status_text: Optional[str]
    size_bytes: Optional[int]

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


@dataclass
class HTMLSnapshot:
    """In-memory representation of a captured page source."""

    event: BrowsingEvent
    html: str

    def to_dict(self) -> Dict[str, object]:
        data = self.event.to_dict()
        data["html"] = self.html
        return data


@dataclass
class SessionResult:
    """Aggregated output returned after a recording session finishes."""

    html_snapshots: List[HTMLSnapshot]
    events: List[BrowsingEvent]
    html_directory: Optional[str]

    @property
    def html_list(self) -> List[str]:
        return [snapshot.html for snapshot in self.html_snapshots]

    def to_dict(self) -> Dict[str, object]:
        return {
            "html_snapshots": [snapshot.to_dict() for snapshot in self.html_snapshots],
            "events": [event.to_dict() for event in self.events],
            "html_directory": self.html_directory,
        }


class _SessionWriter:
    """Persists captured events and any HTML snapshots to disk."""

    def __init__(self, output_dir: Path, log_filename: str = "session_log.jsonl") -> None:
        self.directory = output_dir
        self.directory.mkdir(parents=True, exist_ok=True)
        self.log_path = self.directory / log_filename
        self._log_lock = asyncio.Lock()

    async def write_event(self, event: BrowsingEvent) -> None:
        line = json.dumps(event.to_dict(), ensure_ascii=False)
        async with self._log_lock:
            await asyncio.to_thread(self._append_line, line)

    def _append_line(self, line: str) -> None:
        with self.log_path.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")


class SessionRecorder:
    """High-level helper to launch a browser and capture page sources as you browse."""

    def __init__(
        self,
        output_dir: Path | str = "session_captures",
        *,
        browser: str = "chromium",
        channel: Optional[str] = None,
        headless: bool = False,
        on_event: Optional[Callable[[BrowsingEvent], Awaitable[None] | None]] = None,
        html_output_dir: Path | str | None = None,
    ) -> None:
        self.output_dir = Path(output_dir)
        self.browser_name = browser
        self.browser_channel = channel
        self.headless = headless
        self.on_event = on_event
        self._writer = _SessionWriter(self.output_dir)
        self.html_output_dir = Path(html_output_dir) if html_output_dir is not None else self.output_dir
        self.html_output_dir.mkdir(parents=True, exist_ok=True)
        self._browser: Optional[Browser] = None
        self._shutdown_lock = asyncio.Lock()
        self._page_ids: Dict[Page, str] = {}
        self._doc_responses: Dict[str, Dict[str, object]] = {}
        self._tasks: Set[asyncio.Task[None]] = set()
        self._logged_page_closure: Set[str] = set()
        self._html_snapshots: List[HTMLSnapshot] = []
        self._events: List[BrowsingEvent] = []
        self._last_result: Optional[SessionResult] = None

    async def run(self, start_url: Optional[str] = None) -> SessionResult:
        """Launch the browser, optionally navigate to a start URL, and capture until it closes."""
        self._reset_results()

        async with async_playwright() as playwright:
            browser_type = getattr(playwright, self.browser_name, None)
            if browser_type is None:
                raise ValueError(f"Unsupported browser type: {self.browser_name}")

            launch_kwargs = {"headless": self.headless}
            if self.browser_channel:
                launch_kwargs["channel"] = self.browser_channel

            browser: Browser = await browser_type.launch(**launch_kwargs)
            self._browser = browser
            try:
                context: BrowserContext = await browser.new_context()

                context.on("page", lambda page: self._spawn(self._attach_page(page)))

                initial_page = await context.new_page()
                await self._attach_page(initial_page)

                if start_url:
                    await initial_page.goto(start_url)

                loop = asyncio.get_running_loop()
                disconnected = loop.create_future()

                def _mark_disconnected() -> None:
                    if not disconnected.done():
                        disconnected.set_result(None)

                browser.on("disconnected", _mark_disconnected)
                try:
                    await disconnected
                finally:
                    browser.remove_listener("disconnected", _mark_disconnected)
            finally:
                self._browser = None

        await self._wait_for_tasks()

        result = SessionResult(
            html_snapshots=list(self._html_snapshots),
            events=list(self._events),
            html_directory=str(self.html_output_dir),
        )
        self._last_result = result
        return result

    def run_sync(self, start_url: Optional[str] = None) -> SessionResult:
        """Helper to run the recorder from synchronous code."""
        return asyncio.run(self.run(start_url=start_url))

    @property
    def last_result(self) -> Optional[SessionResult]:
        return self._last_result

    @property
    def html_snapshots(self) -> List[HTMLSnapshot]:
        return list(self._html_snapshots)

    @property
    def html_list(self) -> List[str]:
        return [snapshot.html for snapshot in self._html_snapshots]

    def _reset_results(self) -> None:
        self._html_snapshots = []
        self._events = []
        self._page_ids.clear()
        self._doc_responses.clear()
        self._tasks.clear()
        self._logged_page_closure.clear()
        self._last_result = None

    def _spawn(self, coro: Awaitable[None]) -> None:
        task = asyncio.create_task(coro)
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)

    async def _wait_for_tasks(self) -> None:
        if not self._tasks:
            return
        await asyncio.gather(*self._tasks, return_exceptions=True)

    async def _attach_page(self, page: Page) -> None:
        if page in self._page_ids:
            return
        page_id = uuid4().hex[:8]
        self._page_ids[page] = page_id

        page.on("framenavigated", lambda frame: self._on_frame_navigated(page, frame))
        page.on("close", lambda: self._spawn(self._handle_page_closed(page)))
        page.on("response", lambda response: self._on_page_response(page_id, response))

        await self._capture_snapshot(page, page_id, event_type="page-opened")

    def _on_frame_navigated(self, page: Page, frame: Frame) -> None:
        page_id = self._page_ids.get(page)
        if not page_id or frame != page.main_frame:
            return
        self._spawn(self._capture_snapshot(page, page_id, event_type="navigation"))

    def _on_page_response(self, page_id: str, response) -> None:
        try:
            resource_type = response.request.resource_type
        except Exception:
            resource_type = None

        if resource_type != "document":
            return

        self._doc_responses[page_id] = {
            "url": response.url,
            "status": response.status,
            "status_text": response.status_text,
        }

    async def _handle_page_closed(self, page: Page) -> None:
        page_id = self._page_ids.pop(page, None)
        if not page_id or page_id in self._logged_page_closure:
            return
        self._logged_page_closure.add(page_id)
        event = BrowsingEvent(
            timestamp=self._timestamp(),
            page_id=page_id,
            url="",
            title="",
            event_type="page-closed",
            html_path=None,
            status=None,
            status_text=None,
            size_bytes=None,
        )
        await self._record_event(event)
        self._doc_responses.pop(page_id, None)

        if not self._page_ids:
            await self._close_browser()

    async def _close_browser(self) -> None:
        async with self._shutdown_lock:
            browser = self._browser
            if not browser or not browser.is_connected():
                return
            try:
                await browser.close()
            except Exception:
                pass

    async def _capture_snapshot(self, page: Page, page_id: str, *, event_type: str) -> None:
        if page.is_closed():
            return

        timestamp = self._timestamp()
        try:
            title = await page.title()
        except Exception:
            title = ""
        try:
            url = page.url
        except Exception:
            url = ""
        try:
            html = await page.content()
        except Exception:
            html = ""

        html_filename = self._make_html_filename(timestamp, page_id, title)
        html_path_value: Optional[str] = None
        try:
            await asyncio.to_thread(self._write_html_file, html_filename, html)
            html_path_value = html_filename
        except Exception:
            html_path_value = None

        html_size = len(html.encode("utf-8"))
        response_info = self._doc_responses.get(page_id, {})
        event = BrowsingEvent(
            timestamp=timestamp,
            page_id=page_id,
            url=url,
            title=title,
            event_type=event_type,
            html_path=html_path_value,
            status=response_info.get("status"),
            status_text=response_info.get("status_text"),
            size_bytes=html_size,
        )
        await self._record_event(event, html=html)

    async def _record_event(self, event: BrowsingEvent, *, html: Optional[str] = None) -> None:
        self._events.append(event)
        if html is not None:
            self._html_snapshots.append(HTMLSnapshot(event=event, html=html))
        await self._emit(event)
        await self._writer.write_event(event)

    def _write_html_file(self, filename: str, html: str) -> None:
        html_path = self.html_output_dir / filename
        html_path.write_text(html, "utf-8")

    async def _emit(self, event: BrowsingEvent) -> None:
        if not self.on_event:
            return
        result = self.on_event(event)
        if asyncio.iscoroutine(result):
            await result

    @staticmethod
    def _timestamp() -> str:
        return datetime.now(timezone.utc).isoformat()

    def _make_html_filename(self, timestamp: str, page_id: str, title: str) -> str:
        stamp = datetime.fromisoformat(timestamp).strftime("%Y%m%d-%H%M%S-%f")
        slug = self._slugify(title) or "untitled"
        return f"{stamp}_{page_id}_{slug}.html"

    @staticmethod
    def _slugify(value: str, max_length: int = 40) -> str:
        bad_chars = '<>:"/\\|?*'
        cleaned = [
            "_" if ch in bad_chars or ord(ch) < 32 else ch
            for ch in value.strip()
        ]
        slug = "".join(cleaned)
        if len(slug) > max_length:
            slug = slug[:max_length]
        return slug or ""


__all__ = ["SessionRecorder", "BrowsingEvent", "SessionResult", "HTMLSnapshot"]
