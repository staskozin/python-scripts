import argparse
import os
from clint.textui import progress
import generator

parser = argparse.ArgumentParser(description='Makes single images or multiple images square')
parser.add_argument('-m', '--multi', help='Multiple images mode', action='store_true')
parser.add_argument('-s', '--source', help='Path to source image(s)', required=True)
parser.add_argument('-r', '--result', help='Where to put processed image(s)', required=True)

args = parser.parse_args()
print('Multiple images mode' if args.multi else 'Single image mode')
print(f'Source path: {args.source}')
print(f'Result path: {args.result}')

if args.multi:
    images = list(filter(lambda img: img.lower().endswith('.jpg'), os.listdir(args.source)))
    if not os.path.exists(args.result):
        os.mkdir(args.result)
    for img in progress.bar(images):
        source_path = os.path.join(args.source, img)
        result_path = os.path.join(args.result, img)
        generator.process(source_path, result_path)
else:
    generator.process(args.source, args.result)
    print('OK')
