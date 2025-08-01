import cv2
import numpy as np

def nothing(x):
    pass


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('Red', 'image', 0, 255, nothing)
cv2.createTrackbar('Green', 'image', 0, 255, nothing)
cv2.createTrackbar('Blue', 'image', 0, 255, nothing)

while True:
    cv2.imshow('image', img)

    r = cv2.getTrackbarPos('Red', 'image')
    g = cv2.getTrackbarPos('Green', 'image')
    b = cv2.getTrackbarPos('Blue', 'image')

    img[:] = [b, g, r]

    if cv2.waitKey(1) == 27:
        break
