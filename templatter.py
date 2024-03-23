from globalimports import*

class TemplateDetect(object):
    def __init__(self):
        self.color_bounds = {
            "green": {
                "lower": np.array([40, 200, 200]),
                "upper": np.array([80, 255, 255])
            },
            "red": {
                "lower": np.array([0, 200, 200]), # what we originally had: [0, 100, 100]
                "upper": np.array([10, 255, 255]) 
            },
            "blue": {
                "lower": np.array([100, 10, 10]), # originally had: 100, 50, 50
                "upper": np.array([140, 255, 255])
            },
            "black": {
                "lower": np.array([0, 0, 0]),
                "upper": np.array([50, 50, 50])
            },
        }
    def draw_marker(self, image, coordinates, radius=1, color=(0, 255, 0), thickness=5):
        ''' Draws a marker on a coordinate to help with tracking, debugging, and testing of coordinates. '''
        # Draw a circle on the output image
        output_image = image
        cv2.circle(output_image, coordinates, radius, color, thickness)
        return output_image
    def draw_rect(self, image, start, end, color=(0, 255, 0), thickness=2):
        '''
            draws a rectangle, this helps us when debugging and trying to 
            determine how the BBOX coordinates supplied to us looks like, this
            won't be used for production, but it's a useful method, so 
            whatever, here.    
        '''
        img = cv2.rectangle(image, start, end, color, thickness)
        return img
    def detect_rect(self, image, color="green"):
        '''
            detects a rectangle based off of the color supplied
            and determines the start and end coordinates, this is
            essential for the user-defined BBOX.
        
        '''
        # Convert the image to the HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for the green color
        lower_green = self.color_bounds[color]["lower"]
        upper_green = self.color_bounds[color]["upper"]

        # Threshold the image to get a binary mask
        mask = cv2.inRange(hsv_image, lower_green, upper_green)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter out small contours
        contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

        if contours:
            # Get the bounding box of the largest contour
            x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
            start_coordinates = (x, y)
            end_coordinates = (x + w, y + h)
            return start_coordinates, end_coordinates
        else:
            return None

