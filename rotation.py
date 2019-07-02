#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:23:18 2019

@author: aritra
"""

import cv2
import numpy as np
img=cv2.imread('/home/aritra/python_opencv3/database/lena_color_512.tif')
print(img.shape)
rows,cols,dep=img.shape
M1 = cv2.getRotationMatrix2D((cols/3,rows/2),45,1)
#cv2.getRotationMatrix2D()
M2 = cv2.getRotationMatrix2D((cols/3,rows/2),45,2)
dst1 = cv2.warpAffine(img,M1,(cols,rows))
dst2 = cv2.warpAffine(img,M2,(cols,rows))
cv2.imshow('img',img)
cv2.imshow('dest_1',dst1)
cv2.imshow('dest_2',dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()