# Webscrapehelper

A lightweight Playwright helper that opens a headed browser and records the HTML source (plus metadata) for each page you visit until the browser window is closed.

## Features
- Launches Chromium (or another Playwright browser) in headed mode so you can browse manually.
- Collects page HTML, title, URL, HTTP status, and file size whenever the main frame navigates.
- Saves snapshots to disk (`session_log.jsonl` + individual `.html` files) and keeps an in-memory list for immediate post-run use.
- Returns a `SessionResult` with helpers such as `.html_list` and `.html_snapshots`.
- Optional callback hook so your code can react to each captured event in real time.
- Lets you write HTML files to a custom directory via `html_output_dir`.

## Requirements
- Python 3.9+
- Playwright (`pip install playwright` and run `playwright install` once to fetch browser binaries).

## Local installation
```bash
pip install -e .
playwright install
```

## Quick start
```python
import asyncio
from webscrapehelper import SessionRecorder

async def main():
    recorder = SessionRecorder(output_dir="session_data", headless=False)
    result = await recorder.run()
    print(f"Captured {len(result.html_list)} snapshots")
    if result.html_list:
        first_html = result.html_list[0]
        print(first_html[:200])  # preview

if __name__ == "__main__":
    asyncio.run(main())
```

Browse as usual; the script exits after you close the Playwright browser. Captured snapshots live in `session_data/`, and the returned `SessionResult` keeps the HTML in memory. To persist the HTML elsewhere, pass `html_output_dir="C:/some/folder"` when creating the recorder.

See `examples/record_session.py` for a slightly richer example that logs each event.
