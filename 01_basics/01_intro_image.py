import cv2
print(cv2.__version__)


image = cv2.imread(filename=r'/01_basics/assets/bear.jpg')
cv2.imshow('image2', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
