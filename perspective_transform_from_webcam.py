#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:56:23 2019

@author: aritra
"""
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
def nothing(x):
        pass
cv2.namedWindow('trackbar')
cv2.createTrackbar('U_L_X','trackbar',0,640, nothing) #for upper left x coordinate
cv2.createTrackbar('U_L_Y','trackbar',0,480, nothing) #for upper left y coordinate
cv2.createTrackbar('L_L_X','trackbar',0,640, nothing) #for lower left x coordinate
cv2.createTrackbar('L_L_Y','trackbar',0,480, nothing) #for upper left y coordinate
cv2.createTrackbar('L_R_X','trackbar',0,640, nothing) #for lower right x coordinate
cv2.createTrackbar('L_R_Y','trackbar',0,480, nothing) #for lower right y coordinate
cv2.createTrackbar('U_R_X','trackbar',0,640, nothing) #for upper right x coordinate
cv2.createTrackbar('U_R_Y','trackbar',0,480, nothing) #for upper right y coordinate
while(True):
    ret,frame=cap.read()
    #ret=cap.set(3,512)
    #ret=cap.set(4,512)
    U_L_X=cv2.getTrackbarPos('U_L_X','trackbar')
    U_L_Y=cv2.getTrackbarPos('U_L_Y','trackbar')
    L_L_X=cv2.getTrackbarPos('L_L_X','trackbar')
    L_L_Y=cv2.getTrackbarPos('L_L_Y','trackbar')
    L_R_X=cv2.getTrackbarPos('L_R_X','trackbar')
    L_R_Y=cv2.getTrackbarPos('L_R_Y','trackbar')
    U_R_X=cv2.getTrackbarPos('U_R_X','trackbar')
    U_R_Y=cv2.getTrackbarPos('U_R_Y','trackbar')

    cv2.circle(frame,(U_L_X,U_L_Y),5,(255,0,0),-1)
    cv2.circle(frame,(L_L_X,L_L_Y),5,(0,255,0),-1)
    cv2.circle(frame,(L_R_X,L_R_Y),5,(0,0,255),-1)
    cv2.circle(frame,(U_R_X,U_R_Y),5,(120,53,40),-1)
    pts1=np.float32([[U_L_X,U_L_Y],[U_R_X,U_R_Y],[L_L_X,L_L_Y],[L_R_X,L_R_Y]])
    print(pts1)
    pts2=np.float32([[0,0],[500,0],[0,600],[500,600]])
    M=cv2.getPerspectiveTransform(pts1,pts2)
    res=cv2.warpPerspective(frame,M,(500,600))
    cv2.imshow('original_Feed',frame)
    cv2.imshow('Perspective Corrected', res)
    k=cv2.waitKey(5)
    if(k==27):
        break
cap.release()
cv2.destroyAllWindows()
    
    
    