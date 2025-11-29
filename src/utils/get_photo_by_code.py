from pathlib import Path

def get_photo_by_code(foulder: Path, code: str) -> Path | None:
    for file in foulder.iterdir():
        if file.stem == code:
            return file
    
    return None
