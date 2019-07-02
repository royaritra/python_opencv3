#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:00:10 2019

@author: aritra
"""

import cv2
import numpy as np
img=cv2.imread('/home/aritra/python_opencv3/database/lena_color_512.tif')
print(img.shape)
rows,cols,dep=img.shape
M=np.float32([[1,0,150],[0,1,100]])
dst= cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',img)
cv2.imshow('dest',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()