from PIL import Image


def process(source_path: str, result_path: str):
    image = make_square(source_path)
    save_image(result_path, image)


def make_square(image_path: str, fill_color=(255, 255, 255)) -> Image:
    image = Image.open(image_path)
    x, y = image.size
    size = max(x, y)
    new_image = Image.new('RGB', (size, size), fill_color)
    new_image.paste(image, (int((size - x) / 2), int((size - y) / 2)))
    return new_image


def save_image(path: str, image: Image) -> None:
    image.save(path, quality=100)
