import cv2
import matplotlib.pyplot as plt
img = cv2.imread("BZ7LGZSXCFHOXAN2XCTAM4QRPQ.jpg")

plt.imshow(img[:,:,::-1])
plt.show()