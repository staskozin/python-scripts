from sys import argv
from os import listdir, path, mkdir
from PIL import Image
from clint.textui import progress
from win10toast import ToastNotifier


def render_watermark(image_path, watermark_path, result_path):
    image = Image.open(image_path)
    width, height = image.size
    watermark = Image.open(watermark_path).resize((width, height), Image.BICUBIC)
    result = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    result.paste(image, (0, 0))
    result.paste(watermark, (0, 0), mask=watermark)
    result = result.convert("RGB")
    result = result.resize((1024, 1024), Image.BICUBIC)
    result.save(result_path, quality=90)


if len(argv) == 4:
    watermark = argv[1]
    source = argv[2]
    destination = argv[3]
    if not path.exists(destination):
        mkdir(destination)
    for img in progress.bar(listdir(source)):
        render_watermark(path.join(source, img), watermark, path.join(destination, img[:-4] + '.jpg'))
    ToastNotifier().show_toast("Фото готовы", "Обработано " + str(len(listdir(source))) + " фото", duration=60)
else:
    print('Usage:\n''py watermark.py watermark.png source\\path destination\\path\n')
