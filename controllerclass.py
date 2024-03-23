from globalimports import*
from ocroperations import*
from Bloxburg.styletemplates import*

class ControllerClass(object):
    def __init__(self):
        self.size = pyautogui.size()

    def locate_and_hold(self, img_path, delay: int=0.2):
        position = pyautogui.locateCenterOnScreen(f"{img_path}", confidence=0.8)
        x = int(position[0]/2)
        y = int(position[1]/2)
        position = (x, y)
        pyautogui.mouseDown(position)
        time.sleep(delay)
        pyautogui.mouseUp(position)

    def click_center(self, delay=True):
        center_x = int(self.size.width/2)
        center_y = int(self.size.height/2)
        center_position = (center_x, center_y)
        pyautogui.click(center_position)
        if delay:
            time.sleep(1)
        else:
            time.sleep(0.1)