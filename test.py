import cv2
import matplotlib.pyplot as plt
img = cv2.imread("BZ7LGZSXCFHOXAN2XCTAM4QRPQ.jpg")
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2RGB)
plt.imshow(img[:,:,::-1])
plt.show()