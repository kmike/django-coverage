"""
Drone.io badge generator.

Currently set up to work on Mac.

Requires Pillow.
"""

import os
from PIL import Image, ImageDraw, ImageFont

SIZE = (95, 18)

def hex_colour(hex):
    if hex[0] == '#':
        hex = hex[1:]
    return (
        int(hex[:2], 16),
        int(hex[2:4], 16),
        int(hex[4:6], 16),
    )

BACKGROUND = hex_colour('#4A4A4A')
SUCCESS = hex_colour('#94B944')
WARNING = hex_colour('#E4A83C')
ERROR = hex_colour('#B10610')

SUCCESS_CUTOFF = 85
WARNING_CUTOFF = 45

FONT = ImageFont.truetype(size=10, filename="/Library/Fonts/Arial.ttf")
FONT_SHADOW = hex_colour('#525252')

PADDING_TOP = 3

def build_image(percentage, colour):
    image = Image.new('RGB', SIZE, color=BACKGROUND)
    drawing = ImageDraw.Draw(image)
    
    drawing.rectangle([(55, 0), SIZE], colour, colour)
    drawing.text((8, PADDING_TOP+1), 'coverage', font=FONT, fill=FONT_SHADOW)
    drawing.text((7, PADDING_TOP), 'coverage', font=FONT)
    
    drawing.text((63, PADDING_TOP+1), '%s%%' % percentage, font=FONT, fill=FONT_SHADOW)
    drawing.text((62, PADDING_TOP), '%s%%' % percentage, font=FONT)
    
    return image

os.chdir('_build')    
for i in range(101):
    filename = '%i.png' % i
    file = open(filename, 'wb')
    if i < WARNING_CUTOFF:
        build_image(i, ERROR).save(file)
    elif i < SUCCESS_CUTOFF:
        build_image(i, WARNING).save(file)
    else:
        build_image(i, SUCCESS).save(file)
