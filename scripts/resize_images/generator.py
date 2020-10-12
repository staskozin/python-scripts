from PIL import Image
from math import floor


def process(source_path: str, result_path: str, max_size: int) -> None:
    image = resize(Image.open(source_path), max_size)
    image.save(result_path, quality=100)


def resize(image: Image, max_size: int) -> Image:
    ratio = max_size / max(image.size)
    x, y = image.size
    return image.resize((floor(x * ratio), floor(y * ratio)))
