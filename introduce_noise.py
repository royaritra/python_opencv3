#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:16:54 2019

@author: aritra
"""

import cv2
import numpy as np
import random
img= cv2.imread('/home/aritra/python_opencv3/database/lena_color_512.tif')
rows,cols,channels=img.shape
output=np.zeros(img.shape,np.uint8)
p=.05
for i in range(rows):
    for j in range(cols):
        r=random.random()
        if(r<p/2):
            #pepper noise
            output[i][j]=[0,0,0]
        elif(r<p):
            #for salt
            output[i][j]=[255,255,255]
        else:
            output[i][j]=img[i][j]

cv2.imwrite('/home/aritra/python_opencv3/database/lenna-512-noise.jpg',output)
cv2.imshow('noisy_lenna',output)
k=cv2.waitKey(0)
if(k==27):
    cv2.destroyAllWindows()
                    
        
