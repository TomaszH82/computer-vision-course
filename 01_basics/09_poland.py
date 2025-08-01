import cv2

img = cv2.imread(r'assets\poland.png')
# cv2.imshow('img', img)

img = cv2.copyMakeBorder(img, top=20, left=20, bottom=20, right=20, borderType=cv2.BORDER_CONSTANT, value=(255, 255, 255)   )
cv2.imshow('img', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('thresh', thresh)

contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
print(len(contours))

img = cv2.drawContours(img, contours[0], -1, (0, 255, 0), 3)
cv2.imshow('img', img)


contour = contours[0]
leftmost = contour[contour[:, :, 0].argmin()][0]
rightmost = contour[contour[:, :, 0].argmax()][0]
topmost = contour[contour[:, :, 1].argmin()][0]
bottommost = contour[contour[:, :, 1].argmax()][0]

for point in [leftmost, rightmost, topmost, bottommost]:
    cv2.circle(img, (int(point[0]), int(point[1])), 5, (0, 0, 255), -1)
cv2.imshow('img', img)




cv2.waitKey(0)