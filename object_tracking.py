#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:55:13 2019

@author: aritra
"""

import cv2
import numpy as np
cap= cv2.VideoCapture(0)
def nothing(x):
        pass
cv2.namedWindow('trackbar')
cv2.createTrackbar('L_H_B','trackbar',0,177, nothing)
cv2.createTrackbar('U_H_B','trackbar',0,177, nothing)
cv2.createTrackbar('L_S_B','trackbar',0,255, nothing)
cv2.createTrackbar('U_S_B','trackbar',0,255, nothing)
cv2.createTrackbar('L_V_B','trackbar',0,255, nothing)
cv2.createTrackbar('U_V_B','trackbar',0,255, nothing)
while(True):
    ret,frame=cap.read()
    cv2.imshow('original',frame)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', hsv)
    
    
    L_H_B = cv2.getTrackbarPos('L_H_B','trackbar')
    U_H_B = cv2.getTrackbarPos('U_H_B','trackbar')
    L_S_B = cv2.getTrackbarPos('L_S_B','trackbar')
    U_S_B = cv2.getTrackbarPos('U_S_B','trackbar')
    L_V_B = cv2.getTrackbarPos('L_V_B','trackbar')
    U_V_B = cv2.getTrackbarPos('U_V_B','trackbar')
    lower_blue=np.array([L_H_B,L_S_B,L_V_B]) #8,157,21 for orange 25,101,28 for green
    upper_blue=np.array([U_H_B,U_S_B,U_V_B]) #20,255,255 for orange 101,255,255 for green
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    cv2.imshow('MASK',mask)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('result',res)
    k=cv2.waitKey(1)
    if(k==27):
        break
cap.release()
cv2.destroyAllWindows()