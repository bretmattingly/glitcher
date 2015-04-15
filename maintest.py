__author__ = 'bretmattinglyii'
__version__ = 'v0.1'

'''
A simple experiment in databending some images.
'''

from random import shuffle
from PIL import Image
from numpy import asarray
from sorts import sort_horizontal_bar
from divisions import vertical_slice
from shuffles import horizontal_shuffle, vertical_shuffle


try:
    im = Image.open("dry/armored_skeleton.jpg")
except IOError:
    print("File not found, you done messed up")
    exit()

# Print image info.
print(im.format, im.size, im.mode)
# Force image to RGB (all chops will be in RGB for now)
if not im.format == "RGB":
    im = im.convert(mode="RGB")



