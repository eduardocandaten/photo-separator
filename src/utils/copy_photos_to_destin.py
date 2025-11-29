import shutil
from pathlib import Path

def copy_photos_to_destin(photos: list[Path], destin: Path) -> None:
    destin.mkdir(parents=True, exist_ok=True)

    for photo in photos:
        destin_path = destin / photo.name
        if not destin_path.exists():
            shutil.copy2(photo, destin_path)
