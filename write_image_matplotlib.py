#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:06:03 2019

@author: aritra
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
imgpath= "/home/aritra/Documents/python/database/lena_color_256.tif"
img = cv2.imread(imgpath,1)
#print(img)
#for converting into bgr from rgb
img2 = img[:,:,::-1]
#print('next')
#print(img2)
plt.imshow(img2,  interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()