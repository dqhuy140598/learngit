import cv2
import matplotlib.pyplot as plt
img = cv2.imread("BZ7LGZSXCFHOXAN2XCTAM4QRPQ.jpg")
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2RGB)
import numpy as np
black = np.zeros((400,500),dtype=np.uint8)
white = 255 * np.ones((400,500),dtype=np.uint8)
total = np.hstack((black,white))



plt.imshow(img[:,:,::-1])
plt.show()