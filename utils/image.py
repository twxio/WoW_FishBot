import pyscreenshot as ImageGrab


class Image:
    '''
    Helper class that adds an abstraction layer for image
    functionality.
    '''

    def capture() -> dict:
        '''
        Captures a temporary image of the wow subprocess

        Returns a x,y containing dictionary

        Example: {
            'x': x_coordinate,
            'y': y_coordinate
        }
        '''
        _image: ImageGrab.grab()
        raise NotImplementedError
