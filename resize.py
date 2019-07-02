#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:20:48 2019

@author: aritra
"""
import cv2
import numpy as np
img=cv2.imread('/home/aritra/python_opencv3/database/lena_color_512.tif')
zoom_area=cv2.resize(img,None, fx=2,fy=2,interpolation=cv2.INTER_AREA)
zoom_cubic=cv2.resize(img,None, fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
zoom_linear=cv2.resize(img,None, fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
shrink_area=cv2.resize(img,None, fx=.5,fy=.5,interpolation=cv2.INTER_AREA)
shrink_cubic=cv2.resize(img,None, fx=.5,fy=.5,interpolation=cv2.INTER_CUBIC)
shrink_linear=cv2.resize(img,None, fx=.5,fy=.5,interpolation=cv2.INTER_LINEAR)
images=[img,zoom_area,zoom_cubic,zoom_linear,shrink_area,shrink_cubic,shrink_linear]
while(True):
    
    cv2.imshow('img',images[0])
    cv2.imshow('zoom_area',images[1])
    cv2.imshow('zoom_cubic',images[2])
    cv2.imshow('zoom_linear',images[3])
    cv2.imshow('shrink_area',images[4])
    cv2.imshow('shrink_cubic',images[5])
    cv2.imshow('shrink_linear',images[6])


    k=cv2.waitKey(5)
    if(k==27):
        break
cv2.destroyAllWindows()

