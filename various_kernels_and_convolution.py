#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:29:23 2019

@author: aritra
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('/home/aritra/python_opencv3/database/lena_color_512.tif')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

k_identity= np.float32([[0,0,0],[0,1,0],[0,0,0]])
k_edge_1= np.float32([[1,0,-1],[0,0,0],[-1,0,1]])
k_edge_2= np.float32([[0,1,0],[1,-4,1],[0,1,0]])
k_edge_3= np.float32([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
k_sharpen= np.float32([[0,-1,0],[-1,5,-1],[0,-1,0]])
k_box_blur= np.ones((3,3),np.float32)/9
k_gaussian_blur= np.float32([[1,2,1],[2,4,2],[1,2,1]])/16
images=['img','k_identity','k_edge_1','k_edge_2','k_edge_3','k_sharpen','k_box_blur','k_gaussian_blur']
output_identity=cv2.filter2D(img,-1,k_identity)
output_edge_1=cv2.filter2D(img,-1,k_edge_1)
output_edge_2=cv2.filter2D(img,-1,k_edge_2)
output_edge_3=cv2.filter2D(img,-1,k_edge_3)
output_sharpen=cv2.filter2D(img,-1,k_sharpen)
output_box_blur=cv2.filter2D(img,-1,k_box_blur)
output_gaussian_blur=cv2.filter2D(img,-1,k_gaussian_blur)
output=[img,output_identity,output_edge_1,output_edge_2,output_edge_3,output_sharpen,output_box_blur,output_gaussian_blur]


for i in range(8):
   cv2.imshow(images[i],output[i])
k=cv2.waitKey(0)
if(k==27):
    cv2.destroyAllWindows()
    