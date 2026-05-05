# Boundary Extraction
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Test_2.jpg', 0)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
eroded = cv2.erode(binary, kernel)
boundary = cv2.subtract(binary, eroded)

plt.imshow(boundary, cmap='gray'); plt.show()