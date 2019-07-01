#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:12:44 2019

@author: aritra
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/aritra/python_opencv3/database/sudoku-original.jpg',0)
img1=cv2.medianBlur(img,5)
th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th2=cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

while(True):
    cv2.imshow('original',img)
    cv2.imshow('blurred',img1)
    cv2.imshow('Adaptive Mean',th1)
    cv2.imshow('Gaussian',th2)
    k=cv2.waitKey(5)
    if(k==27):
        break
cv2.destroyAllWindows()
