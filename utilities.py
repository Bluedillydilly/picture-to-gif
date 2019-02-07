"""
    Utility functions used in other modules.
"""

def side_size():
    """
        Side lengths of the image. Image is a square.
    """
    return 1024

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
