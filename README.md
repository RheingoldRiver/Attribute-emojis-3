# Attribute-emojis-3
There is no attribute-emojis-2, this is when Gungho added a 3rd attribute to the game. See also [Attribute-emojis](https://github.com/RheingoldRiver/Attribute-emojis)

## Config
Edit this in `main.py`.
```python
# dynamic config
USE_SPRITES = False
CUR_PATH = 'combined2/{}'
INPUT_FILE_PATTERN = 'originals3/{}.png'
```

If editing a spritesheet you can also set which sheet in `crop_orbs.py`.
```python
SPRITE_FILE = 'sprites/048.png'
```

## Output directories
* `Combined` contains plain (solid color) ones
* `Combined2` contains the fancy (original asset) ones
* `Combined_spritesheets` contains prototypes of ones generated from spritesheets of orb skins. These are NOT ready for production, the slices are a bit unaligned, but you can see how they look & then maybe recreate if you like one in particular with individual images cut out from the sheet. idk why they're not aligned if you can figure it out send a pr please.
