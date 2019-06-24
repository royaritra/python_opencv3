#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 00:12:58 2019

@author: aritra
"""
import numpy as np
import cv2
img=np.zeros((512,512,3), np.uint8)
img1=cv2.line(img,(0,0),(511,511),(0,255,0),5)
#img2=cv2.imwrite('draw.jpg',img)
img1=cv2.rectangle(img1,(241,17),(510,52),(255,0,0),5)
img1=cv2.circle(img1,(256,256),75,(0,0,255),5)
img1=cv2.ellipse(img1,(256,256),(45,85),90,0,360,(0,45,125),5)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(255,255,255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img1)
k=cv2.waitKey(0)
if k==97:
    cv2.destroyAllWindows()