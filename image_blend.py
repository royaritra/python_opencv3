#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 21:42:28 2019

@author: aritra
"""
import cv2
img1=cv2.imread('database/4.1.03.tiff')
img2=cv2.imread('database/4.1.04.tiff')
dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
dst2=cv2.addWeighted(img1,0.7,img2,0.3,50)
cv2.imshow('result',dst)
cv2.imshow('result2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
