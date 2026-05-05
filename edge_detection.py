# Edge Detection
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Test_1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
sobel = cv2.magnitude(sobelx, sobely)

# Prewitt
kernelx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
prewitt = cv2.filter2D(gray, -1, kernelx) + cv2.filter2D(gray, -1, kernely)

# Canny
canny = cv2.Canny(gray, 100, 200)

plt.imshow(canny, cmap='gray'); plt.show()