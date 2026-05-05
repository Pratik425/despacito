# Thickening
import cv2
import numpy as np

img = cv2.imread('Test_1.jpg', 0)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
thick = cv2.dilate(binary, kernel, iterations=2)

cv2.imshow('Thickened', thick)
cv2.waitKey(0)
cv2.destroyAllWindows()