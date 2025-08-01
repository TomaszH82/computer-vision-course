import numpy as np
import cv2

orginal_image = cv2.imread(filename=r'/01_basics/assets/python.png')
img = orginal_image.copy()

# cv2.imshow('logo', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

height, width = img.shape[:2]
print(f'Wysokość: {height}')
print(f'Szerokość: {width}')

# cv2.line(img=img, pt1=(0, 0), pt2=(width, height), color=(255, 0, 0), thickness=2)
# cv2.imshow('line', img)
# cv2.waitKey(0)

#
# cv2.rectangle(img, pt1=(200, 50),pt2=(400,230) , color=(0, 0, 255), thickness=2)
# cv2.imshow('rectangle', img)
# cv2.waitKey(0)

# cv2.circle(img,center=(300,140),radius=90,color=(255,0,0),thickness=5)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = orginal_image.copy()
# pts = np.array([[300,140],[200,200],[200,50],[300,50]], np.int32).reshape((-1, 1, 2))
# cv2.polylines(img, [pts], False, (255,0,255), 2)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = orginal_image.copy()
cv2.putText(
    img,
    text='Python',
    org=(20, 40),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1,
    color=(255, 20, 20),
    thickness=3,
)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()