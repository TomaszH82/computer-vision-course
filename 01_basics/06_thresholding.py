import cv2
import numpy as np

img = cv2.imread(r'assets\grey.png', 0)
print(img)
# cv2.imshow('img', img)

#
# thresh_binary = cv2.threshold(img,150,255,cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh_binary', thresh_binary)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

for thresh in [0, 50, 100, 150, 200]:
    thresh_binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow(f'thresh_binary: {thresh}', thresh_binary)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

cv2.waitKey(0)