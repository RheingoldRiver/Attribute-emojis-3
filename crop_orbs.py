from PIL import Image

GAP = 3
ORB_DIM = 100
SPRITE_FILE = 'sprites/048.png'

orb_offsets = {
    'fire': [0, 0],
    'water': [1, 0],
    'wood': [2, 0],
    'light': [3, 0],
    'dark': [0, 1],
    'nil': [0, 3]
}


def get_orb(color):
    sprite = Image.open(SPRITE_FILE)
    target = sprite.crop(get_dim(color))
    return target


def get_dim(color):
    left = orb_offsets[color][0] * ORB_DIM + orb_offsets[color][0] * GAP
    upper = orb_offsets[color][1] * ORB_DIM + orb_offsets[color][1] * GAP
    right = left + ORB_DIM
    lower = upper + ORB_DIM
    return left, upper, right, lower
