import time # For timing how long entire program takes to execute
import gif_creator

def main():
    pass

def main_testing():
    print("Testing mode entered.")
    gif_creator.rando_n_frames_gif( int(input("Number of frames of the gif:\n")), str(input("Name of gif: ")+'.gif'))


start_time = time.time()
#main()
main_testing()
print("Time to complete: {}".format(time.time()-start_time))
