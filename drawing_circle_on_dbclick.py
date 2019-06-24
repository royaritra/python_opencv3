#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:46:30 2019

@author: aritra
"""

import cv2
import numpy as np
#mouse callback function
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,255,255),-1)
        
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
y=cv2.setMouseCallback('image',draw_circle)
while(True):
    cv2.imshow('image',img)
    k= cv2.waitKey(1)
    if k==97:
        break
cv2.destroyAllWindows()
