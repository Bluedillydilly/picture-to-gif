import time # For timing how long entire program takes to execute
from gif_creator import rando_n_frames_gif

def main():
    pass

def user_frames():
    """
    Gets the number of frames the user wants the gif to be.
    """
    return int(input("Number of frames of the gif:\n"))

def user_file_name():
    """
    Gets the name the user wants the gif to be.
    """
    return str(input("Name of gif: ")+'.gif')

def main_testing():
    """
    Mode for testing.
    """
    print("Testing mode entered.")
    frames = user_frames()
    start_time = time.time()
    rando_n_frames_gif(frames, user_file_name())
    print("Time to complete: {}".format(time.time()-start_time))


#main()
main_testing()
