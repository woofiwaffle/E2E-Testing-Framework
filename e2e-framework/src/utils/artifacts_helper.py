import os
from datetime import datetime
from glob import glob

def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def save_screenshot(page, dest_dir: str, name: str = "screenshot") -> str:
    _ensure_dir(dest_dir)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    filename = f"{name}_{ts}.png"
    path = os.path.join(dest_dir, filename)
    page.screenshot(path=path, full_page=True)
    return path

def save_page_source(page, dest_dir: str, name: str = "page_source") -> str:
    _ensure_dir(dest_dir)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    filename = f"{name}_{ts}.html"
    path = os.path.join(dest_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page.content())
    return path

def list_videos(video_dir: str):
    """Вернёт список файлов видео (можно затем скопировать / загрузить)."""
    if not os.path.exists(video_dir):
        return []
    # Playwright по умолчанию пишет .webm
    patterns = [os.path.join(video_dir, "*.webm"), os.path.join(video_dir, "*.mp4")]
    files = []
    for p in patterns:
        files.extend(glob(p))
    return sorted(files)
