from globalimports import*

class OCROperations(object):
    def __init__(self):
        ...
    def extract_coordinates(self, img, start, end):
        '''
            Extracts a region from an image in the shape of a rectangle
        
        '''
        x1, y1 = start
        x2, y2 = end

        # Extract the portion of the image using the coordinates
        extracted_portion = img[y1:y2, x1:x2]

        return extracted_portion
    def binarize_image(self, img, threshold_value=128):
        th, img = cv2.threshold(img, 128, 192, cv2.THRESH_OTSU)

        return img
    def preprocess_image(self, img):
        '''
        custom function to pre-process game images for OCR-ing
        '''
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = self.binarize_image(img)
        return img
