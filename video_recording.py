# camera script
# written by Jessica Reemeyer May 2022

import os
from time import strftime
from picamera import PiCamera

# set up camera
# (there are many custom settings available, but I found the automatic settings worked best)
camera = PiCamera()
camera.framerate = 10
camera.resolution = (1280,720)
camera.exposure_mode = 'auto' 

# set up file path
vidDir = '/home/pi/fish_videos'
if os.path.isdir(vidDir) == False:
    os.mkdir(vidDir)  
filename=os.path.join(vidDir,strftime('%Y-%m-%d_%H-%M-%S'))
videofilename=filename+'.h264'

# record video
camera.start_recording(videofilename, format='h264', quality=1)
# the numerical value below corresponds to the length of the video in seconds
camera.wait_recording(1440) 
camera.stop_recording()
camera.close()


