import cv2
import numpy as np

img = cv2.imread(r'assets\checkbox.png' )
# cv2.imshow('image', img)


img = cv2.copyMakeBorder(
    img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=(255, 255, 255)
)

# cv2.imshow('img_br', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img_gray', gray)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# cv2.imshow('img_blur', blurred)

thresh = cv2.threshold(blurred, thresh=75, maxval=200, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[INFO] contours: {len(contours)}')

img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[0]], contourIdx=-1, color=(0, 255, 222), thickness=2)
# cv2.imshow('img_cnt', img_cnt)


#wyszukanie kontur z zaznaczonym checkboxem
cheked_idx = None
total= 0
for idx in [1,2]:
    #wygenerowanie maski
    mask = np.zeros(shape=gray.shape, dtype=np.uint8)
    cv2.drawContours(mask, [contours[idx]], -1, 255, -1)
    # cv2.imshow(f'mask {idx} :', mask)

    mask_inv = cv2.bitwise_not(mask)
    # cv2.imshow(f'mask_inv {idx} :', mask_inv)

    answer = cv2.add(gray, mask_inv)
    # cv2.imshow(f'answer {idx} :', answer)

    answer_inv = cv2.bitwise_not(src=answer)
    cv2.imshow(f'answer_inv {idx} :', answer_inv)

    cnt = cv2.countNonZero(answer_inv)
    if cnt > total:
        cheked_idx = idx
print(f'[INFO] cheked idx: {cheked_idx}')

img = cv2.drawContours(img, contours=[contours[cheked_idx]] ,contourIdx=-1, color=(0, 255, 222), thickness=2)
cv2.imshow('img', img)



cv2.waitKey(0)
