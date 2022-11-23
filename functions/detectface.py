import cv2
from init import cam

# noinspection PyUnresolvedReferences
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")


def detect_face(gray_image):
    # noinspection PyUnresolvedReferences
    faces = faceCascade.detectMultiScale(
        gray_image,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(15, 15),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if len(faces) > 0:
        x, y, w, h = faces[0]
        cam.set_face(x, y, w, h)
