import asyncio
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if SRC_DIR.exists():
    # Allow running the example without installing the package.
    sys.path.insert(0, str(SRC_DIR))

from webscrapehelper import SessionRecorder


async def main() -> None:
    output_dir = Path("session_output")

    async def on_event(event):
        print(f"[{event.event_type}] {event.timestamp} {event.url} -> {event.html_path}")

    recorder = SessionRecorder(output_dir=output_dir, headless=False, on_event=on_event)
    await recorder.run()


if __name__ == "__main__":
    asyncio.run(main())
