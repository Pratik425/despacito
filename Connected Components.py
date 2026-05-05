# Connected Components
import cv2
import numpy as np

img = cv2.imread('Test_3.jpg', 0)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

num_labels, labels = cv2.connectedComponents(binary)
label_img = np.uint8(255 * labels / np.max(labels))

cv2.imshow('Labels', label_img)
cv2.waitKey(0)
cv2.destroyAllWindows()