import cv2 as cv

'''
    Checks the similarity between two images
'''
def check_similarity(image_1, image_2):
    # seed = (np.random.random()*10) % # when I have multiple image similarity checking methods
    return histogram_method(image_1, image_2)

'''
Checks how similar two images are by comparing their histogram color distributions are.
Returns an int [0,100]
    100 = 100% match between the two pictures
    0 = 0% match between the two pictures
'''
def histogram_method(i1, i2):
    h1 = cv.calcHist(cv.imread(i1), [0], None, [256], [0,256])
    h2 = cv.calcHist(cv.imread(i2), [0], None, [256], [0,256])
    compare_value = cv.compareHist(h1, h2, 0)

    two_precision_float = True
    if two_precision_float:
        percent_similar = round(compare_value*100)/100
    else:
        percent_similar = compare_value
    return percent_similar


def test():
    print(check_similarity("1.png","2.png"))

test()
