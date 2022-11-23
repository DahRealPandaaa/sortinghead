import cv2
from PIL import Image as Pil_Image


class webcam:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.x = 250
        self.y = -5
        self.w = 0
        self.h = 0

    def get_frame(self):
        cv2image = cv2.cvtColor(self.cam.read()[1], cv2.COLOR_BGR2RGB)
        cv2image_gray = cv2.cvtColor(self.cam.read()[1], cv2.COLOR_BGR2GRAY)

        img = Pil_Image.fromarray(cv2image)
        return img, cv2image_gray

    def get_face(self):
        return self.x, self.y - self.h + 10

    def set_face(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __del__(self):
        self.cam.release()
