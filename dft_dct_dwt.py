# Transform Domain
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt

img = cv2.imread('Test_3.jpg', 0)

# DFT
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
magnitude = 20*np.log(np.abs(dft_shift)+1)

# DCT
img_float = np.float32(img)/255.0
dct = cv2.dct(img_float)

# DWT
coeffs = pywt.dwt2(img, 'haar')
LL, (LH, HL, HH) = coeffs

plt.imshow(magnitude, cmap='gray'); plt.show()