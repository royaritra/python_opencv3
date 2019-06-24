#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:34:18 2019

@author: aritra
"""


import cv2
cap= cv2.VideoCapture(0)
while(True):
    #capturing frame by frame
    ret,frame=cap.read()
    print(ret)
    ret=cap.set(3,480)
    ret=cap.set(4,480)
    #converting into b/w
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #display resulting frame
    cv2.imshow('image',grey)
    cv2.imwrite('img1.jpg',grey)
    k=cv2.waitKey(0)
    if  k==97:
        break
cap.release()
cv2.destroyAllWindows()
    