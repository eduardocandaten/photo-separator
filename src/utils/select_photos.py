from pathlib import Path
from utils.get_photo_by_code import get_photo_by_code

def select_photos(foulder: Path, codes: list[str]):
    photos = []
    for code in codes:
        photo = get_photo_by_code(foulder, code)
        if photo:
            photos.append(photo)

    return photos