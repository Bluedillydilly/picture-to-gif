import cv2 as cv

'''
Checks how similar two images are by comparing their histogram color distributions are.
'''
def histogram_method(i1, i2):
    print(type(cv.imread(i1, 1)))
    return cv.compareHist(cv.imread(i1, 1), cv.imread(i2, 1),  5)

def test():
    print( histogram_method('1.png','2.png') )

test()
