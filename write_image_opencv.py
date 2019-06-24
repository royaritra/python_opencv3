#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:26:47 2019

@author: aritra
"""
import cv2
imgpath= "/home/aritra/Documents/python/database/lena_color_256.tif"
img=cv2.imread(imgpath,0);
cv2.imshow('new_image',img);
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==97:
    cv2.imwrite('lenna_greyscale.png',img)
    print("done saving")
    cv2.destroyAllWindows()
