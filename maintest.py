__author__ = 'bretmattinglyii'
__version__ = 'v0.1'

'''
A simple experiment in databending some images.
'''

from PIL import Image
from random import shuffle

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
    wet = Image.new(image.mode, image.size, (255,255,255))

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
try:
    im = Image.open("dry/aztec_eagle.jpg")
except IOError:
    print("File not found, you done messed up")
    exit()

print(im.format, im.size, im.mode)
# im.show()
horizontal_shuffle(im)

