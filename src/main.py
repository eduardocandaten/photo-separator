from pathlib import Path
from utils.split_codes import split_codes
from utils.select_photos import select_photos
from utils.copy_photos_to_destin import copy_photos_to_destin

codes = split_codes(input('Códigos: '))
origin = Path(input('Pasta de origem: ')).expanduser()
destin = Path(input('Pasta de destino: ')).expanduser()

photos = select_photos(origin, codes)
copy_photos_to_destin(photos, destin)
