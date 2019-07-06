#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:15:56 2019

@author: aritra
"""

import cv2
noisy=cv2.imread('/home/aritra/python_opencv3/database/lenna-512-noise.jpg')
denoised=cv2.medianBlur(noisy,5)
while(True):
    cv2.imshow('noisy',noisy)
    cv2.imshow('denoised',denoised)
    k=cv2.waitKey(0)
    if(k==27):
        break
cv2.destroyAllWindows()