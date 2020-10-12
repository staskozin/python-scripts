from PIL import Image


def process(source_path: str, result_path: str):
    image = make_square(Image.open(source_path))
    image.save(result_path, quality=100)


def make_square(image: Image, fill_color=(255, 255, 255)) -> Image:
    x, y = image.size
    size = max(x, y)
    new_image = Image.new('RGB', (size, size), fill_color)
    new_image.paste(image, (int((size - x) / 2), int((size - y) / 2)))
    return new_image
