import argparse
from math import sqrt
import Image
import ImageDraw

def color_map(v):
    assert 0 <= v <= 255
    if v == 0: return (0, 0, 0)
    if v == 255: return (255, 255, 255)
    if v < 4 * 8:
        # 0 .. 31
        return (0, 255 - (31 * 4) + v * 4, 0)
    if v < 16 * 8:
        # 32 .. 127
        # 0 .. 95
        return (128 + (v - 32) * 127 / 95, 0, 0)

    return (0, v, v)


def convert():
    if args.test:
        data = map(chr, range(256))
    else:
        data = file(args.in_file).read()

    size = len(data)
    w = 1
    while size / w > w * 8:
        w *= 2

    h = size / w
    if size % w != 0: h += 1

    image = Image.new('RGB', (w, h))
    d = ImageDraw.Draw(image)
    for i, c in enumerate(data):
        d.point((i % w, i / w), color_map(ord(c)))
        image.save(args.out_file, 'PNG')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Show binary in color pattern')
    parser.add_argument('--test', action='store_true')
    parser.add_argument('in_file', action='store')
    parser.add_argument('--out_file', action='store', default='out.png')
    args = parser.parse_args()
    convert()
