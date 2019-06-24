#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:03:49 2019

@author: aritra
"""

import cv2
cap= cv2.VideoCapture('/home/aritra/Documents/python/database/akiyo_qcif.y4m')
while(True):
    #capturing frame by frame
    ret,frame=cap.read()
    #converting into b/w
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #display resulting frame
    cv2.imshow('image',grey)
    k=cv2.waitKey(0)
    if  k==97:
        break
cap.release()
cv2.destroyAllWindows()
    