import numpy as np # For array functions and such
from PIL import Image # For creation of images
import imageio as imio # For appending images together to form an animated gif
import time # For timing how long entire program takes to execute

def main():
    rando_n_frames_gif( int(input("Number of frames of the gif:\n")), str(input("Name of gif: ")+'.gif'))
    get_to_image(str(input("File name to image-morph to(include file extension):")))

def rando_n_frames_gif(num_frames, gif_name):
    # variables for frame creation and writing, as well as gif creation and writing
    frames = [None] * num_frames
    for i in range(num_frames):
        frames[i] = (np.random.rand(side_size(), side_size(), 3)*255).astype(np.uint8)
    imio.mimsave(gif_name, frames, 'GIF', duration=0.0833)

def get_to_image(file_name):
    target = imio.imread(file_name)

def side_size():
    return 1024

def gif_location():
    return 'rando.gif'

def frame_extension():
    return '.png'

start_time = time.time()
main()
print("Time to complete: {}".format(time.time()-start_time))
