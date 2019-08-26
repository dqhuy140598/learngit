import cv2
import matplotlib.pyplot as plt
import numpy as np
# img = cv2.imread("BZ7LGZSXCFHOXAN2XCTAM4QRPQ.jpg")
# grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# rgb = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2RGB)

black_image = np.zeros(shape=(400,600),dtype=np.uint8)
white_image  = 255 * np.ones(shape=(400,600),dtype=np.uint8)


total_image = np.hstack((black_image,white_image))
plt.imshow(total_image)
plt.show()
# plt.imshow(img[:,:,::-1])
# plt.show()q