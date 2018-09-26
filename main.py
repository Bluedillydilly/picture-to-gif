import numpy as np # For array functions and such
from PIL import Image # For creation of images
import imageio as imio # For appending images together to form an animated gif
import time # For timing how long entire program takes to execute

def main():
    # variables for frame creation and writing, as well as gif creation and writing
    w, h = 1024,1024
    all_images = []
    total_num_frames = 30
    frame_extension = '.png'
    gif_location = 'rando.gif'
    
    # creation of frames and appending frames to the gif
    with imio.get_writer( gif_location , mode='I') as writer:
        for i in range( total_num_frames):
            file_path = str(i)+frame_extension
            Image.fromarray(
                (np.random.rand( w, h, 3)*255).astype( 
                    np.int8 ) ,'RGB').save(
                        file_path, 'PNG')
            writer.append_data(imio.imread(file_path ))

start_time = time.time()
main()
print("Time to complete: {}".format(time.time()-start_time))
