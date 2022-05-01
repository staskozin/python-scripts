import requests
import shutil
from os import path, mkdir
from sys import argv
from clint.textui import progress


def get_filename(path):
    return path[-20:]


if len(argv) == 3:
    f = open(f'{argv[1]}')
    images = f.read().split('\n')
    f.close()
    destination = argv[2]
    if not path.exists(destination):
        mkdir(destination)

    for i, img in enumerate(progress.bar(images)):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
        }
        r = requests.get(img, stream=True, headers=headers)
        if r.status_code == 200:
            r.raw.decode_content = True
            local_img = open(f'{destination}/{get_filename(img)}', 'wb')
            shutil.copyfileobj(r.raw, local_img)
            local_img.close()
        else:
            print(img)
        del r
else:
    print('Usage: python download_images.py images.txt destination/path')
