from email.mime import image

import numpy as np
import cv2

def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f'x={x}, t={y}')

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (0, 50, 255), 2)


img = cv2.imread(filename=r'assets\tesla.jpg')

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break
