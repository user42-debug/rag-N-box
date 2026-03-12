from picamera2 import Picamera2
from PIL import Image

class Picture:
    def __init__(self):
        self.picam2 = Picamera2()
        self.picam2.start()
        self.img = Image.fromarray(self.picam2.capture_array())

    def show(self):
        self.img.show()