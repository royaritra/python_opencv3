#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 00:53:22 2019

@author: aritra
"""

import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    #print(frame.shape)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([94,13,0])
    upper_blue=np.array([142,210,207])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    kernel=np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    dilation = cv2.dilate(mask,kernel,iterations = 1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    mask2=mask+blackhat+tophat
    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Erosion',erosion)
    cv2.imshow('Dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    cv2.imshow('tophat',tophat)
    cv2.imshow('blackhat',blackhat)
    cv2.imshow('mask2',mask2)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()