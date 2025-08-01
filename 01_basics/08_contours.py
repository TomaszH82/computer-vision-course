import cv2
import numpy as np
import imutils

orginal_img = cv2.imread(r'assets\python.png')
img = orginal_img.copy()
# cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

#maska
thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

#wykrywanie kontur
contuours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
print("liczba kontur:" + str(len(contuours)))

img_cnt = cv2.drawContours(img.copy(), contuours[11], -1, 255, 2)
cv2.imshow('img_cnt', img_cnt)

#pole konturów
area = cv2.contourArea(contuours[4], oriented=True)
print(area)

max_area = 0
for idx, contour in enumerate(contuours):
    area = cv2.contourArea(contour, oriented=True)
    if area > max_area:
        max_area = area
        idx_flag_area = idx

print(f'Najwieksza area: {max_area} \nPole: {idx_flag_area}')

perimeter = cv2.arcLength(contuours[11], True)
print("perimeter: " + str(perimeter))

cv2.waitKey(0)
