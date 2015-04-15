__author__ = 'bretmattinglyii'
__version__ = 'v0.1'

'''
A simple experiment in databending some images.
'''

from PIL import Image
from random import shuffle
from numpy import asarray

"""
Horizontally shuffle an image into even bars.
:param image PIL Image object to shuffle.
:return shuffled image
"""
def horizontal_shuffle(image):
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

    shuffle(bars)
    for k, bar in enumerate(bars):
        corner = (0, k*barheight)
        wet.paste(bar, corner)

    wet.save("wet/output.jpg")
    return wet

'''
Vertically shuffle an image into even bars.
:param image PIL Image object to shuffle
:return shuffled image
'''
def vertical_shuffle(image):
    width, height = image.size
    evendivisors = []
    for i in range(5, width):
        if width % i == 0:
            evendivisors.append(i)
    pass

    print("Even divisors are: ")
    print(evendivisors)
    chosendivisor = int(input("Choose your divisor: "))
    print(chosendivisor)
    numbars = int(width/chosendivisor)
    barwidth = chosendivisor
    bars = []
    wet = Image.new(image.mode, image.size, (255, 255, 255))

    for j in range(0, numbars):
        barleft = (barwidth * j)
        barupper = 0
        barright = barleft + barwidth
        barlower = int(height)
        #left, upper, right, lower
        box = (barleft, barupper, barright, barlower)
        bar = image.crop(box)
        bar.load()
        bars.append(bar)
        # bar.save("wet/bar" + str(j) + ".jpg") # debugging only
        # Make a bar, put it an array, shuffle the array, reprint.

    shuffle(bars)
    for k, bar in enumerate(bars):
        corner = (k*barwidth, 0)
        wet.paste(bar, corner)

    wet.save("wet/output2.jpg")


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

"""
Utility function for slicing up an image vertically
:param image to slice horizontally
:return ordered list of bars (pillow.Images)
"""
def vertical_slice(image):
    width, height = image.size
    evendivisors = []
    for i in range(5, width):
        if width % i == 0:
            evendivisors.append(i)

    print("Even divisors are: ")
    print(evendivisors)
    chosendivisor = int(input("Choose your divisor: "))
    print(chosendivisor)
    numbars = int(width/chosendivisor)
    barwidth = chosendivisor
    bars = []
    wet = Image.new(image.mode, image.size, (255, 255, 255))

    for j in range(0, numbars):
        barleft = (barwidth * j)
        barupper = 0
        barright = barleft + barwidth
        barlower = int(height)
        #left, upper, right, lower
        box = (barleft, barupper, barright, barlower)
        bar = image.crop(box)
        bar.load()
        bars.append(bar)
        # bar.save("wet/bar" + str(j) + ".jpg") # debugging only
        # Make a bar, put it an array, shuffle the array, reprint.
    return bars


def sort_horizontal_bar(bar):
    width, height = bar.size
    data = asarray(bar)
    print(data)
    pass

try:
    im = Image.open("dry/armored_skeleton.jpg")
except IOError:
    print("File not found, you done messed up")
    exit()

print(im.format, im.size, im.mode)
# im.show()
horizontal_shuffle(im)
bars = vertical_slice(im)
sort_horizontal_bar(bars[0])



