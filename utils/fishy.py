# Third-party libraries
import cv2

# Local libraries
from utils.click import Click
from utils.image import Image


class Fishbot():
    '''
    Takes in two arguments when initalized
    - image_small: (str) a filepath to image to find
    - image_large: (str) a filepath to image to find in

    '''

    image_small: None
    image_large: None
    path_image_large: str
    path_image_small: str
    method: None
    cv2_instance: cv2

    def __init__(self, image_small: str, image_large: str):
        # Set internal variables
        self.path_image_small = image_small
        self.path_image_large = image_large
        self.cv2_instance = cv2
        self.method = cv2.TM_SQDIFF_NORMED

        # Read internal images
        self.internal_read_images(
            search=self.path_image_small,
            target=self.path_image_large
        )

    def internal_read_images(self, search: str, target: str) -> None:
        '''
        Takes in two arguements:
        - search:  (str) image to search for
        - query:   (str) image to search in
        '''

        # Read the images from the file
        self.image_small = cv2.imread(filename=search)
        self.image_large = cv2.imread(filename=target)

    def internal_scan(self, _image_small, _image_large, _method):
        '''
        Work in project
        Scans and opens image with target currently
        '''

        result = cv2.matchTemplate(_image_small, _image_large, _method)

        # Minimum squared difference
        mn, _, mnLoc, _ = cv2.minMaxLoc(result)

        # Draw the rectangle:
        # Extract the coordinates of our best match
        MPx, MPy = mnLoc

        # Get the size of the template. This is the same size as the match.
        trows, tcols = _image_small.shape[:2]

        # Draw the rectangle on _image_large
        self.cv2_instance.rectangle(
            _image_large,
            (MPx, MPy),
            (MPx+tcols, MPy+trows),
            (0, 0, 255),
            2
        )

        # Display the original image with the rectangle around the match.
        self.cv2_instance.imshow('output', _image_large)

        # The image is only displayed if we call this
        self.cv2_instance.waitKey(0)

    def start(self):
        '''
        Starts the fishbot
        '''

        # TODO:
        # Add subprocess capture process
        # Add GUI panel? -> Future maybe

        self.internal_scan(
            _image_small=self.image_small,
            _image_large=self.image_large,
            _method=self.method
        )
