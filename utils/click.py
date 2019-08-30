import pyautogui


class Click:
    '''
    Helper class that adds an abstraction layer for click
    functionality.
    '''

    x: int
    y: int

    def this(x: int, y: int):
        '''
        Clicks markex point
        '''
        raise NotImplementedError
