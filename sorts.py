__author__ = 'bretmattingly'

from PIL import Image


def sort_horizontal_bar(bar, debug=False):
    """
    Default sorts (by red intensity) a given horizontal bar.
    :param bar: A PIL.Image object (generally a horizontal slice of a larger image)
    :param debug: Boolean whether or not to show the bar after sorting is complete. Default False.
    :return: The bar, pixel sorted in place.
    """
    bar.show()
    pixels = bar.load()
    width, height = bar.size
    bars = []
    for y in range(height):
        thisbar = []
        for x in range(width):
            thisbar.append(pixels[x, y])

        bars.append(thisbar)

    # Now we have a list of lists, which might be a little easier to access.
    # PixelAccess object is, for some reason, not iterable.
    # So we copy it all into a 2D array of rows, sort the rows,
    # Then rewrite the pixels from the sorted rows.
    # Because python sorts tuples by first item, then next, and so on,
    # This is currently sorting by red intensity.

    for y, bartosort in enumerate(bars):
        bartosort.sort()
        for x, pixel in enumerate(bartosort):
            pixels[x, y] = pixel

    if debug:
        bar.show()

    return bar

