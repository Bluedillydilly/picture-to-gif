import numpy as np # For array functions and such
from PIL import Image # For creation of images
import imageio as imio # For appending images together to form an animated gif
import time # For timing how long entire program takes to execute
import variable_function.py


def main():
    rando_n_frames_gif( int(input("Number of frames of the gif:\n")), str(input("Name of gif: ")+'.gif'))

def rando_n_frames_gif(num_frames, gif_name):

    # variables for frame creation and writing, as well as gif creation and writing
    frames = [None] * num_frames
    for i in range(num_frames):
        frames[i] = (np.random.rand(side_size(), side_size(), 3)*255).astype(np.uint8)
    imio.mimsave(gif_name, frames, 'GIF', duration=0.0833)

def pic_to_desired(start_image, target_image):
    pass    

def rando_to_desired(target_image):
    pic_to_desired(
            Image.fromarray( 
                np.random.rand(target_image.size[0], target_image.size[1]), 3 ), 'RGB')

'''
    Checks the similarity between two images
'''
def check_similarity(image_1, image_2):
    seed = (np.random.random()*10) %

start_time = time.time()
main()
print("Time to complete: {}".format(time.time()-start_time))
