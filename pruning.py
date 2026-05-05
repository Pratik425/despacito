# Pruning
import cv2
import numpy as np

img = cv2.imread('Test_1.jpg', 0)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
pruned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

cv2.imshow('Pruned', pruned)
cv2.waitKey(0)
cv2.destroyAllWindows()