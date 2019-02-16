"""
Utility functions used in other modules.
"""
from numpy import random, uint8

i_channels = 3

def random_n_array():
    """
    Creates a square array with sides length s_l of random noise.
    Values [0,1).
    3d array; third dimension is number of channels for the image. Most have 3, PNG got 4; alpha.
    """
    s_l = side_size()
    return (random.rand(s_l, s_l, i_channels)*255).astype(uint8)

def side_size():
    """
        Side lengths of the image. Image is a square.
    """
    return 256

def desired_gif_fps(target_fps):
    """
        IDK bruh
    """
    return target_fps/60

def gif_location():
    """
        where to save gif to
    """
    return 'rando.gif'

def frame_extension():
    """
        the file extension
    """
    return '.png'

def min_similarity():
    """
        similarity needed between images to call them 'the same'
    """
    return 0.90
