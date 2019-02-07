"""
   Module doc string
"""

import cv2 as cv
from PIL import Image
import utilities as var

def check_similarity(image_1, image_2):
    """
        Checks the similarity between two images.
        A wrapper function for when I have multiple image comparison functions
    """
    percent_similar = 0
    # seed = (np.random.random()*10) % # when I have multiple image similarity checking methods
    percent_similar = histogram_method(image_1, image_2)
    return percent_similar

def histogram_method(image_1, image_2):
    """
        Checks how similar two images are by comparing their histogram color distributions are.
        Images don't have to be same size.
        Returns an double precision float [0,1]
        1 = 100% match between the two pictures. Images are effectively the same
        0 = 0% match between the two pictures
    """
    h1 = cv.calcHist(cv.imread(image_1), [0], None, [256], [0, 256])
    h2 = cv.calcHist(cv.imread(image_2), [0], None, [256], [0, 256])
    compare_value = cv.compareHist(h1, h2, 0)

    decimal_places = 2
    factor = 10 ** decimal_places
    percent_similar = round(compare_value*factor)/factor
    return percent_similar

def pixel_by_pixel(image_1, image_2):
    """
        Checks how similar (%) two images are by pixel-by-pixel comparisons.
        Averages the sum of total differences to get average difference of one image from another.
        Images must be the same size.

        Is this really need? WIP

    """
    for col in range(Image.open(image_2).size[0]):
        for row in range(Image.open(image_2).size[1]):
            col+row


def test():
    """
        Main function for the module.
    """
    pic_one = "1.png"
    pic_two = "2.png"
    percent_sim = check_similarity(pic_one, pic_two)
    print(percent_sim)

test()
