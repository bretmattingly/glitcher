__author__ = 'bretmattingly'

from PIL import Image
from random import shuffle


def horizontal_slice(image):
    """
    Utility function for slicing up an image horizontally. Currently only equal, user-defined slices.
    :param image: PIL.Image to slice horizontally
    :return: ordered list of bars (PIL.Images)
    """
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


def vertical_slice(image):
    """
    Utility function for slicing an image into vertical bars. Currently only slices into even bars of user-defined width
    :param image: PIL.Image to slice horizontally.
    :return: ordered list of bars (PIL.Images)
    """
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
