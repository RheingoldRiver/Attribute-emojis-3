from math import cos, sin, pi
from typing import List, Tuple

from PIL import Image
from PIL import ImageDraw

ELEMENTS = ['fire', 'water', 'wood', 'light', 'dark', 'nil']
INPUT_FILE_PATTERN = 'originals/{}.png'
OUTPUT_FILE_PATTERN = 'combined/{}_{}_{}.png'

DIM = 76
R = DIM / 2
degrees = 0
A = degrees * pi/180

ATTR1_PATH = [(0, 0), (R*cos(pi-A)+R, -R*sin(A)+R), (R, R), (R*cos(A)+R, -R*sin(A)+R), (2*R, 0), (0, 0)] 
ATTR2_PATH = [(2*R, 0), (R*cos(A)+R, -R*sin(A)+R), (R, R), (R, R*2), (R*2, R*2), (2*R, 0)] 
ATTR3_PATH = [(0, 0), (R*cos(pi-A)+R, -R*sin(A)+R), (R, R), (R, R*2), (0, R*2), (0, 0)] 

def make_mask(path: List[Tuple[float, float]]) -> Image:
    """
    :param path:
    :return: a mask to use to make the thing transparent
    """
    poly = Image.new('RGBA', (DIM, DIM))
    pdraw = ImageDraw.Draw(poly)
    pdraw.polygon(path, fill=(255, 255, 255, 255), outline=(255, 255, 255, 255))
    return poly


def main():
    for elem in ELEMENTS:
        attr1_image = Image.open(INPUT_FILE_PATTERN.format(elem)).resize((DIM, DIM))
        attr1_mask = make_mask(ATTR1_PATH)

        for elem2 in ELEMENTS:
            attr2_image = Image.open(INPUT_FILE_PATTERN.format(elem2)).resize((DIM, DIM))
            attr2_mask = make_mask(ATTR2_PATH)

            for elem3 in ELEMENTS:
                attr3_image = Image.open(INPUT_FILE_PATTERN.format(elem3)).resize((DIM, DIM))
                attr3_mask = make_mask(ATTR3_PATH)

                new = Image.new('RGBA', (DIM, DIM))
                new.paste(attr1_image, (0, 0), mask=attr1_mask)
                new.paste(attr2_image, (0, 0), mask=attr2_mask)
                new.paste(attr3_image, (0, 0), mask=attr3_mask)
                new.save(OUTPUT_FILE_PATTERN.format(elem, elem2, elem3))


if __name__ == '__main__':
    main()
