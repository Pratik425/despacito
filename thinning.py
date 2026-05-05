# Thinning
import cv2
import numpy as np

img = cv2.imread('Test_3.png', 0)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

skeleton = np.zeros(binary.shape, np.uint8)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

while True:
    eroded = cv2.erode(binary, element)
    temp = cv2.dilate(eroded, element)
    temp = cv2.subtract(binary, temp)
    skeleton = cv2.bitwise_or(skeleton, temp)
    binary = eroded.copy()
    if cv2.countNonZero(binary) == 0:
        break

cv2.imshow('Skeleton', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()