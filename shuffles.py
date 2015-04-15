__author__ = 'bretmattingly'

from PIL import Image
from random import shuffle


def horizontal_shuffle(bars):
    """
    Horizontally shuffle an image into bars. Currently only supports bars of even length.
    :param bars: List of bars (PIL.Images) to shuffle, i.e., like those generated from divisions.horizontal_slice)
    :return shuffled image
    """
    barwidth, barheight = bars[0].size
    wet = Image.new("RGB", (barwidth, barheight*len(bars)), (255,255,255))
    shuffle(bars)

    for k, bar in enumerate(bars):
        corner = (0, k*barheight)
        wet.paste(bar, corner)

    return wet


def vertical_shuffle(bars):
    """
    Vertically shuffle an image into bars. Currently only supports bars of even length.
    :param bars: List of bars (PIL.Images) to shuffle, i.e., like those generated from divisions.vertical_slice)
    :return shuffled image
    """
    barwidth, barheight = bars[0].size
    wet = Image.new("RGB", (barwidth*len(bars), barheight), (255,255,255))

    shuffle(bars)
    for k, bar in enumerate(bars):
        corner = (k*barwidth, 0)
        wet.paste(bar, corner)

    return wet

