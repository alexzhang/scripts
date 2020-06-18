#!/usr/bin/env python

import math
import os
import sys

from PIL import Image
from escpos.printer import Serial

STRIP_WIDTH = 8
MAX_WIDTH = 540

if len(sys.argv) != 2:
    print("\033[1;31;40musage: {} imagefile.png\033[0m".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

image = Image.open(sys.argv[1])

print("Loaded image: {}".format(sys.argv[1]))
print("Size: {}".format(image.size))

# Resize picture if too wide
(img_w, img_h) = image.size
if img_w > MAX_WIDTH:
    img_h = int(MAX_WIDTH * img_h / float(img_w))
    img_w = MAX_WIDTH
    image = image.resize((img_w, img_h), Image.ANTIALIAS)
    print("Too large, resizing to: {}".format((img_w, img_h)))

image = image.convert('L')

num_strips = math.ceil(img_h / STRIP_WIDTH)
print("Total Strips: {}".format(num_strips))
print("Strip size: {}".format((img_w, STRIP_WIDTH)))

strips = [None] * num_strips
for i in range(num_strips):
    area = (0, STRIP_WIDTH * i, img_w, STRIP_WIDTH * (i + 1))
    strips[i] = image.crop(area)
if img_h % STRIP_WIDTH != 0:
    strips[-1] = strips[-1].crop((0, 0, img_w, img_h % STRIP_WIDTH))

# Dump strips into a temporary directory
if not os.path.exists('.temp'):
    os.mkdir('.temp')
for i in range(num_strips):
    strips[i].save(os.path.join('.temp', "strip{0:03}.png".format(i)))

# Do the printing
p = Serial(devfile='COM5', baudrate=9600, parity='N', stopbits=1, timeout=1.00, dsrdtr=True)

p.text("\033@") # Reset
p.text("\033C\20") # Set sheet eject length
p.text("\0331") # Select 1/8-inch line spacing
p.text("\033$\000\000") # Set left margin
p.text("\033a\001") # Center align

for i in range(num_strips):
    p.image(os.path.join('.temp', "strip{0:03}.png".format(i)))

p.text("\033a\000") # Left align
#p.cut()
