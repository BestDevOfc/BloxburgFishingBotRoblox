import time
import cv2
import keyboard

from templatter import*
from ocroperations import*
from scrshotter import*


class FishingBot(object):
    def __init__(self, timg):
        if "Logs" not in os.listdir():
            os.mkdir("Logs")
        self.flog: IO = open(f"Logs/Logs.txt", 'w', encoding=ENCODING)
        self.template_img = timg
        self.coordinates: dict = {
            "pullButton": (),
            "moneyCoordinates": ((), ()) # start, end rectangle region
        }
    def log_msg(self, msg):
        ''' Records the log messages we want to write, makes it less redundant '''
        self.flog.write(f"[ {msg} ]\n")
        self.flog.flush()


    def calc_threshold(self, img):
        '''
            Calculates number of pixels found after pre-processing,
            if no gray pixels are found then we assume that the
            Bob is underwater, we could remove more noise by perhaps increasing the 
            blur's kernel size, this can be made more configurable via a config before
            the code is released to the public.
        
        '''
        try:
            hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # Define the lower and upper bounds for blue color in HSV
            lower_blue = np.array([10, 20, 20])
            upper_blue = np.array([130, 255, 255])

            # Create a mask to identify blue-colored pixels
            mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

            # Replace blue-colored pixels with black
            img[mask > 0] = [0, 0, 0]

            
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # increasing this would reduce more noise, keep it rougly same size as the "string" of the rod
            img = cv2.GaussianBlur(img, (5, 5), 0)
            _, img = cv2.threshold(img, 10, 25, cv2.THRESH_BINARY)
            freq_tbl = {}
            for row in img:
                for pixel in row:
                    intensity = pixel
                    if intensity not in freq_tbl.keys():
                        freq_tbl[intensity] = 0
                    else:
                        freq_tbl[intensity] += 1
            cv2.imwrite(f"ComputerVision_.png", img)
            return {
                "freqTbl": freq_tbl,
                "computerVision": img
            }
        except Exception as err:
            self.log_msg(f"Error when calcualting the threshold: {err}")

    def startBot(self):
        '''
        
            After everything's configured it is stitched together and ran
        
        '''
        # instantiation:
        Screenshotter = ScreenShotter()
        # templatted image
        template_img = cv2.imread(self.template_img)

        # grab coordinates from template
        Templatter = TemplateDetect()
        bob_coordinates = Templatter.detect_rect(template_img, "red")
        cast_start, cast_end = Templatter.detect_rect(template_img, "black")

        
        # Calculate the midpoint of x and y coordinates
        center_x = (cast_start[0] + cast_end[0]) // 2
        center_y = (cast_start[1] + cast_end[1]) // 2

        # Center of the rectangle
        cast_coordinates = (int(center_x/2), int(center_y/2))
        self.coordinates["pullButton"] = cast_coordinates

        self.log_msg(f"The bob BBOX coordinates: {bob_coordinates}")
        self.log_msg(f"The cast BBOX coordinates: {cast_coordinates}")
        
        start, end = bob_coordinates



        while True:
            try:
                # User wants to terminate the program:
                if keyboard.is_pressed('q'):
                    self.log_msg(f"Q Key was pressed... Exiting...")
                    break
                    
                    
                Screenshotter.take_screenshot(start, end, "GamePlay.png")
                # read screenshot
                img = cv2.imread("GamePlay.png")
                data = self.calc_threshold(img)
                gameplayed_threshold = data["freqTbl"]
                

                if 25 not in gameplayed_threshold.keys():
                    raise Exception

                time.sleep(0.1)
               

            except Exception as err:
                pyautogui.click(self.coordinates["pullButton"]) # pull
                time.sleep(0.2)
                pyautogui.click(self.coordinates["pullButton"]) # cast
                time.sleep(0.5)


        print(f"{C.RED}[+] - {C.GREEN}[ Completed Farming ! ]")
        self.flog.close()
        return