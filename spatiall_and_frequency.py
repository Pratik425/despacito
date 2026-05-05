# Spatial & Frequency Domain Filtering
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Test_3.jpg', 0)

# Spatial filters
gaussian = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpen = cv2.filter2D(img, -1, kernel)

# Frequency domain (DFT)
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

# Low pass
mask = np.zeros((rows, cols), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
img_back = np.fft.ifft2(np.fft.ifftshift(dft_shift * mask))
img_back = np.abs(img_back)

# High pass
mask = np.ones((rows, cols), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 0
img_high = np.fft.ifft2(np.fft.ifftshift(dft_shift * mask))
img_high = np.abs(img_high)

plt.imshow(img, cmap='gray'); plt.show()