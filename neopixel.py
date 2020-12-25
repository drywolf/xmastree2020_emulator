
from browser import window

class NeoPixel:
    def __init__(self, board, count, auto_write):
        pass

    def show(self):
        pass

    def __getitem__(self, key):
        return 0

    def __setitem__(self, index, rgb):
        window.set_LED_value(index, rgb)
