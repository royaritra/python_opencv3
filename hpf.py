#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:16:59 2019

@author: aritra
"""

import cv2
img=cv2.imread('/home/aritra/python_opencv3/database/5.1.11.tiff')
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
edge_laplacian=cv2.Laplacian(img,-1,ksize=1, scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)

edge_sobel_x=cv2.Sobel(img,-1,dx=1,dy=0,ksize=5,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
edge_sobel_y=cv2.Sobel(img,-1,dx=0,dy=1,ksize=5,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
edge_sobel=edge_sobel_x + edge_sobel_y

edge_scharr_x=cv2.Scharr(img,-1,dx=1,dy=0,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
edge_scharr_y=cv2.Scharr(img,-1,dx=0,dy=1,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
edge_scharr=edge_scharr_x+edge_scharr_y
names=['original','edge_laplacian','edge_sobel','edge_scharr']
output=[img,edge_laplacian,edge_sobel,edge_scharr]

for i in range(len(output)):
    cv2.imshow(names[i],output[i])
k=cv2.waitKey(0)
if(k==27):
    cv2.destroyAllWindows()