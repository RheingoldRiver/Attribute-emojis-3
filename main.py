from math import cos, pi

from PIL import Image
from PIL import ImageDraw

ELEMENTS = ['fire', 'water', 'wood', 'light', 'dark', 'nil']
INPUT_FILE_PATTERN = 'originals/{}.png'
OUTPUT_FILE_PATTERN = 'combined/{}_{}.png'

DIM = 76
R = DIM / 2
UPPER_PATH = [(0, 0), (R*cos(5 * pi/6)+R, R), (R, R), (R*cos(pi/6)+R, R), (2*R, 0), (0, 0)]
LOWER_PATH = [(DIM, DIM), (DIM, 0), (0, DIM), (DIM, DIM)]

def make_polygon(path):
    """
    :param path:
    :return: a mask to use to make the thing transparent
    """
    poly = Image.new('RGBA', (DIM, DIM))
    pdraw = ImageDraw.Draw(poly)
    pdraw.polygon(path, fill=(255, 255, 255, 255), outline=(255, 255, 255, 255))
    return poly


def run():
    for elem in ELEMENTS:
        upper_image = Image.open(INPUT_FILE_PATTERN.format(elem)).resize((DIM, DIM))

        upper_triangle = make_polygon(UPPER_PATH)

        for elem2 in ELEMENTS:
            if elem2 == elem:
                continue
            lower_image = Image.open(INPUT_FILE_PATTERN.format(elem2)).resize((DIM, DIM))

            lower_triangle = make_polygon(LOWER_PATH)

            new = Image.new('RGBA', (DIM, DIM))
            new.paste(upper_image, (0, 0), mask=upper_triangle)
            #     new.paste(lower_image, (0, 0), mask=lower_triangle)
            new.save(OUTPUT_FILE_PATTERN.format(elem, elem2))


if __name__ == '__main__':
    run()
