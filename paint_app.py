#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:30:39 2019

@author: aritra
"""

import cv2
import numpy as np
img= np.zeros((660,660,3),np.uint8)
cv2.namedWindow('image')
drawing=False

def nothing(x):
    pass
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar('switch', 'image',0,1,nothing)
reset = '1 : RESET CANVAS'
cv2.createTrackbar('reset', 'image',0,1,nothing)

while(True):
    cv2.imshow('image',img)
    k= cv2.waitKey(1)
    if k==27:
        #cv2.destroyAllWindows()
        break
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    s=cv2.getTrackbarPos('switch','image')
   # print(s)
    reset=cv2.getTrackbarPos('reset','image')
    if s==1:
        def draw_circle(event,x,y,flag,param):
            global drawing
            if event==cv2.EVENT_LBUTTONDOWN:
                drawing=True
            elif event==cv2.EVENT_MOUSEMOVE:
                if drawing==True:
                    cv2.circle(img,(x,y),10,(r,g,b),-1)
            elif event == cv2.EVENT_LBUTTONUP:
                drawing = False
        if reset==1:
            img1= np.zeros((660,660,3),np.uint8)
            cv2.imshow('image',img1)
        cv2.setMouseCallback('image',draw_circle)
        
            
cv2.destroyAllWindows()