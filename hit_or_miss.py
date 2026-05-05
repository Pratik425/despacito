# Hit-or-Miss Transform
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Test_3.png', 0)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.array([[0,1,0],[1,-1,1],[0,1,0]], dtype=np.int8)

hitmiss = cv2.morphologyEx(binary, cv2.MORPH_HITMISS, kernel)

plt.imshow(hitmiss, cmap='gray'); plt.show()