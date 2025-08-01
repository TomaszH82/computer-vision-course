import cv2
import numpy as np
import imutils

img = cv2.imread(r'assets\guido.jpg')
img = imutils.resize(img, width=500)
cv2.imshow('img', img)


canny = cv2.Canny(img, threshold1=250, threshold2=250)
cv2.imshow('canny', canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

for thresh in [0, 25, 50, 75, 100, 125, 150, 200, 225, 250]:
    canny = cv2.Canny(img, threshold1=thresh, threshold2=thresh)
    cv2.imshow(f'canny:{thresh}', canny)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
cv2.waitKey(0)