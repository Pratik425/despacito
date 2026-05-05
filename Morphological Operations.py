# Morphological Operations
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Test_1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(gray, kernel, iterations=1)
dilation = cv2.dilate(gray, kernel, iterations=1)
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

plt.imshow(gray, cmap='gray'); plt.show()