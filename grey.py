#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:12:44 2019

@author: aritra
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/aritra/python_opencv3/database/sudoku-original.jpg',0)
while(True):
    cv2.imshow('img',img)
    k=cv2.waitKey(1)
    if(k==27):
        break
cv2.destroyAllWindows()
