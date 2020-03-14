import requests
import shutil
from os import path, mkdir
from sys import argv
from clint.textui import progress

if len(argv) == 3:
    f = open(f'{argv[1]}')
    images = f.read().split('\n')
    f.close()
    destination = argv[2]
    if not path.exists(destination):
        mkdir(destination)

    for i, img in enumerate(progress.bar(images)):
        r = requests.get(img, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            local_img = open(f'{destination}/{i}.jpg', 'wb')
            shutil.copyfileobj(r.raw, local_img)
            local_img.close()
        del r
else:
    print('Usage: python download_images.py images.txt destination/path')
