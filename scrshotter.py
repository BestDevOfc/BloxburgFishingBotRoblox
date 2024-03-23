import os
import math


class ScreenShotter(object):
    def __init__(self):
        ...
    def take_screenshot(self, start=None, end=None, fname=None):
        '''
            Takes a full window screenshot or a rectangular region
            using mac's built-in command "screencapture"
        
        '''
        try:
            if start == None or end == None or fname == None:
                os.system("screencapture -x GamePlay.png")    
                return
            x = math.floor((start[0]/2))
            y = math.floor((start[1]/2))
            width = math.floor(end[0]/2-x/2)
            height = math.floor(end[1]/2)-y
            # print(f"screencapture -R{x},{y},{width},{height}")
            os.system(f"screencapture -x -R{x},{y},{width},{height} {fname}")
        except Exception as err:
            print(f"When taking screenshot: {err}")