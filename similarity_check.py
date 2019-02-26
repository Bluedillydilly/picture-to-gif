"""
   Module doc string
"""

import cv2 as cv
import utilities as var
from numpy import subtract, multiply, ones, zeros, matrix, sum

def check_similarity(image_1, image_2):
    """
        Checks the similarity between two images.
        A wrapper function for when I have multiple image comparison functions
    """
    percent_similar = 0
    # seed = (np.random.random()*10) % # when I have multiple image similarity checking methods
    percent_similar = histogram_method(image_1, image_2)
    return percent_similar

def histogram_method(arr_1, arr_2):
    """
        Checks how similar two images are by comparing their histogram color distributions are.
        Images don't have to be same size.
        Returns an double precision float [0,1]
        1 = 100% match between the two pictures. Images are effectively the same
        0 = 0% match between the two pictures
    """
    
    blue1 = cv.calcHist([arr_1], [0], None, [256], [0, 256])
    blue2 = cv.calcHist([arr_2], [0], None, [256], [0, 256])
    compare_value = [cv.compareHist(blue1, blue2, 0), 0, 0]

    green1 = cv.calcHist([arr_1], [1], None, [256], [0, 256])
    green2 = cv.calcHist([arr_2], [1], None, [256], [0, 256])
    compare_value[1] = cv.compareHist(green1, green2, 0)

    red1 = cv.calcHist([arr_1], [2], None, [256], [0, 256])
    red2 = cv.calcHist([arr_2], [2], None, [256], [0, 256])
    compare_value[2] = cv.compareHist(red1, red2, 0)

    decimal_places = 2
    factor = 10 ** decimal_places
    percent_similar = sum(compare_value)/3
    return percent_similar
    
def diff_s(arr_1, arr_2):
    diff = subtract(arr_1, arr_2)
    diff_square = multiply(diff, diff)
    diff_square_sum = sum(diff_square)
    max_value = 256*256*256*3*arr_1.size
    return diff_square_sum / max_value

def pixel_by_pixel(image_1, image_2):
    """
        Checks how similar (%) two images are by pixel-by-pixel comparisons.
        Averages the sum of total differences to get average difference of one image from another.
        Images must be the same size.

        Is this really need? WIP

    """
    pass

def test():
    """
        Main function for the module.
    """
    pic_one = "1.png"
    pic_two = "2.png"
    percent_sim = histogram_method(cv.imread(pic_one), cv.imread(pic_two))
    print(percent_sim)

test()
