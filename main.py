import os
from math import cos, sin, pi
from typing import List, Tuple

from PIL import Image
from PIL import ImageDraw

CUR_PATH = 'combined/{}'

ELEMENTS = ['fire', 'water', 'wood', 'light', 'dark', 'nil']
INPUT_FILE_PATTERN = 'originals/{}.png'
OUTPUT_FILE_PATTERN = CUR_PATH + '/{}_{}_{}.png'

ITEMS_PER_FOLDER = 50

DIM = 76
R = DIM / 2
degrees = 15
A = degrees * pi / 180

ATTR1_PATH = [(0, 0), (R * cos(pi - A) + R, -R * sin(A) + R), (R, R), (R * cos(A) + R, -R * sin(A) + R), (2 * R, 0),
              (0, 0)]
ATTR2_PATH = [(2 * R, 0), (R * cos(A) + R, -R * sin(A) + R), (R, R), (R, R * 2), (R * 2, R * 2), (2 * R, 0)]
ATTR3_PATH = [(0, 0), (R * cos(pi - A) + R, -R * sin(A) + R), (R, R), (R, R * 2), (0, R * 2), (0, 0)]


def make_mask(path: List[Tuple[float, float]]) -> Image:
    """
    :param path:
    :return: a mask to use to make the thing transparent
    """
    poly = Image.new('RGBA', (DIM, DIM))
    pdraw = ImageDraw.Draw(poly)
    pdraw.polygon(path, fill=(255, 255, 255, 255), outline=(255, 255, 255, 255))
    return poly


def make_folder(f):
    path = CUR_PATH.format(f)
    if not os.path.exists(path):
        os.mkdir(path)


def main():
    folder = 0
    i = -1
    for elem in ELEMENTS:
        print(i)
        make_folder(folder)

        attr1_image = Image.open(INPUT_FILE_PATTERN.format(elem)).resize((DIM, DIM))
        attr1_mask = make_mask(ATTR1_PATH)

        for elem2 in ELEMENTS:
            attr2_image = Image.open(INPUT_FILE_PATTERN.format(elem2)).resize((DIM, DIM))
            attr2_mask = make_mask(ATTR2_PATH)

            for elem3 in ELEMENTS:
                if elem == elem2 == elem3:
                    continue
                if elem3 == "nil":
                    continue

                i = i + 1
                if i == ITEMS_PER_FOLDER:
                    i = 0
                    folder = folder + 1
                    make_folder(folder)

                attr3_image = Image.open(INPUT_FILE_PATTERN.format(elem3)).resize((DIM, DIM))
                attr3_mask = make_mask(ATTR3_PATH)

                new = Image.new('RGBA', (DIM, DIM))
                new.paste(attr1_image, (0, 0), mask=attr1_mask)
                new.paste(attr2_image, (0, 0), mask=attr2_mask)
                new.paste(attr3_image, (0, 0), mask=attr3_mask)
                new.save(OUTPUT_FILE_PATTERN.format(folder, elem, elem2, elem3))


if __name__ == '__main__':
    main()
