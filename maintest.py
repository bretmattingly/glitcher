__author__ = 'bretmattinglyii'
__version__ = 'v0.1'

'''
A simple experiment in databending some images.
'''

from random import shuffle, choice
from PIL import Image
from numpy import asarray
from sorts import sort_horizontal_bar
from divisions import vertical_slice, horizontal_slice
from shuffles import horizontal_shuffle, vertical_shuffle


filestring = input("Enter your image filename (image should be located in the /dry directory. Include filename extension: ")
try:
    im = Image.open("dry/" + filestring)
except IOError:
    print("Couldn't find your image, loading test image instead.")
    im = Image.open("dry/armored_skeleton.jpg")

# Print image info.
print(im.format, im.size, im.mode)
# Force image to RGB (all chops will be in RGB for now)
if not im.format == "RGB":
    im = im.convert(mode="RGB")

im.show()
bars = vertical_slice(im)
im2 = vertical_shuffle(bars)
bars = horizontal_slice(im2)

for bar in bars:
    sortme = choice([True, False])
    if sortme:
        bar = sort_horizontal_bar(bar, debug=False)

im2 = horizontal_shuffle(bars)
im2.show()
im2.save("wet/test3.jpg")






