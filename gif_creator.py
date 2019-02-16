"""
    Does some stuff.
"""

import cv2 as cv
from numpy import random, uint8, full, multiply, add # For array functions and such
from PIL import Image # For creation of images
import imageio as imio # For appending images together to form an animated gif
from similarity_check import check_similarity
from utilities import *

def rando_n_frames_gif(num_frames, gif_name):
    """
    Creates a gif that is 'num_frames' frames long.
    Gif is saved as 'gif_name', '.gif' is included in the name.
    Each frame is random noise.
    @param num_frames  The total number of frames, or total number of images in the gif
    @param gif_name  The file location of the gif.
    """
    # variables for frame creation and writing, as well as gif creation and writing
    frames = [random_n_array() * num_frames for i in range(num_frames)]
    imio.mimsave(gif_name, frames, 'GIF', duration=desired_gif_fps(10))
    return frames

def pic_to_desired(start_image, target_image):
    """
    adds random noise multiples to the start_image.
    Does this i times to reach a target similarity to target_image.
    @param start_img image to start the transition from. Opened via cv.imread()
    @param target_image The target image for start_img to reach. Opened via cv.imread()
    """
    i = 0 #iterations
    current_img = cv.imread(start_image) # opens start_image
    target_img = cv.imread(target_image)
    (height, width) = current_img.shape[:2] # get height and width of the image
    scalar = full((width, height, 3), 1) # initalize to all 1s
    transition = [current_img]
    sim_changes = [check_similarity(current_img, target_img)]
    while check_similarity(current_img, target_img) < min_similarity():
        i += 1
        current_img = add(current_img,
                          multiply(scalar,
                                   (random.rand(width, height, 3)*255).astype(uint8)))
        transition.append(current_img)
        current_sim = check_similarity(current_img, target_image)
        sim_changes.append(current_sim)
        change_scalar(scalar, transition[i-1], current_img, target_img)

def change_scalar(scalar, previous, current, target):
    """
    Changes scalar vector
    """
    for i in scalar.shape[0]:
        for j in scalar.shape[1]:
            for value in scalar.shape[2]:
                change = current[i][j][value] - previous[i][j][value]
                #min(target[i][j][value]-current[i][j][value], target[i][j][value]-previous[i][j][value])



def rando_to_desired(target):
    """
    Wrapper that uses pic_to_desire to go from a random image of noise to the target_image
    @param target_image the desired image to be have an image similar to it be outputted.
    """
    rgb_size = 3 # R G B values dimensions
    pic_to_desired(
        Image.fromarray(
            random.rand(target.size[0], target.size[1]), rgb_size), 'RGB')
