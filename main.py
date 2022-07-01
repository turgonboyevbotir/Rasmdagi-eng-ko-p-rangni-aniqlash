import numpy as np
import matplotlib.pyplot as plt 
import cv2
import os
from collections import Counter
from sklearn.cluster import KMeans
from skimage.color import rgb2lab, deltaE_cie76



img = cv2.imread('download.jpg')
print(f"Rasmni holati {type(img)}")
print("Rasm o'chami {}".format(img.shape))
plt.imshow(img)


