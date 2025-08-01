import cv2
import numpy as np
import imutils

img = cv2.imread(r'assets\view.jpg')
logo = cv2.imread(r'assets\python.png')
logo = imutils.resize(logo, height=150)

# cv2.imshow('image', img)
# cv2.imshow('logo', logo)
# cv2.waitKey(0)

rows, cols, channels = logo.shape
roi = img[:rows, :cols]
# cv2.imshow('roi', roi)
# cv2.waitKey(0)

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)


mask = cv2.threshold(src=gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('mask', mask)
# cv2.waitKey(0)

mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask_inv', mask_inv)
# cv2.waitKey(0)

img_bg = cv2.bitwise_and(roi, roi, mask=mask)
img_fg = cv2.bitwise_and(logo, logo, mask=mask_inv)
# cv2.imshow('img_bg', img_bg)
# cv2.imshow('img_fg', img_fg)
# cv2.waitKey(0)


dst = cv2.add(img_bg, img_fg)
img[:rows, :cols] = dst
cv2.imshow('dst', img)
cv2.waitKey(0)