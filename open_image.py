# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
def main():
    #print(cv2.__version__)
    impath = "/home/aritra/Documents/python/database/lena_color_256.tif"
    img_color=cv2.imread(impath,1)
    #print(img_color)
    img_unchanged=cv2.imread(impath,-1)

    img_greyscale = cv2.imread(impath,0)
    #for resize of window
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img_greyscale)
    cv2.imshow('Lena_color', img_color)
    cv2.imshow('Lena_unchanged',img_unchanged)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()