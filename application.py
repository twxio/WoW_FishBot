from utils.fishy import Fishbot


if __name__ == '__main__':
    # TODO: Remove test data
    small = 'images/bobber.png'
    large = 'images/screenshot2.png'

    fishBot = Fishbot(image_small=small, image_large=large)
    fishBot.start()
