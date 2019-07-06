#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:35:43 2019

@author: aritra
"""


import cv2
import numpy as np
img=cv2.imread('/home/aritra/python_opencv3/database/lenna-512-noise.jpg')
box=cv2.boxFilter(img,-1,(53,53))
blur=cv2.blur(img,(53,53))
gaussian_blur=cv2.GaussianBlur(img,(53,53),0)
images=['original','box','blur','gaussian_blur']
output=[img,box,blur,gaussian_blur]
for i in range(4):
    cv2.imshow(images[i],output[i])
k=cv2.waitKey(0)
if(k==27):
    cv2.destroyAllWindows()