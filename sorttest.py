__author__ = 'bretmattinglyii'
__version__ = 'v0.1'

from PIL import Image
from random import shuffle
from numpy import asarray



def sort_horizontal_bar(bar):
    pixels = bar.load()
    width, height = bar.size
    rows = []
    for y in range(im.size[0]):
        for x in range(im.size[1]):
            rows[y].apppend(pixels[x, y])
    for row in rows:
        row.sort()
    bar.show()

"""
Utility function for slicing up an image horizontally.
:param image to slice horizontally
:return ordered list of bars (pillow.Images)
"""
def horizontal_slice(image):
    width, height = image.size
    evendivisors = []
    for i in range(5, height):
        if height % i == 0:
            evendivisors.append(i)
    pass

    print("Even divisors are: ")
    print(evendivisors)
    chosendivisor = int(input("Choose your divisor: "))
    print(chosendivisor)
    numbars = int(height/chosendivisor)
    barheight = chosendivisor
    bars = []
    wet = Image.new(image.mode, image.size, (255, 255, 255))

    for j in range(0, numbars):
        barleft = 0
        barupper = (barheight * j)
        barright = int(width)
        barlower = barupper + barheight
        print((barleft, barupper, barright, barlower))
        box = (barleft, barupper, barright, barlower)
        bar = image.crop(box)
        bar.load()
        bars.append(bar)
        # bar.save("wet/bar" + str(j) + ".jpg") # debugging only
        # Make a bar, put it an array, shuffle the array, reprint.
    return bars

try:
    im = Image.open("dry/armored_skeleton.jpg")
except IOError:
    print("File not found, you done messed up")
    exit()

print(im.format, im.size, im.mode)
# im.show()
bars = horizontal_slice(im)
sort_horizontal_bar(bars[0])


