# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:12:58 2020

@author: a0923
"""
import cv2

img_path = r'C:\Users\a0923\Desktop\python\cupoy\1\data\lena.png'

# 以彩色圖片的方式載入
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

(B,G,R) = cv2.split(img)

# 以灰階圖片的方式載入
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)




# 為了要不斷顯示圖片，所以使用一個迴圈
while True:
    # 顯示彩圖
    cv2.imshow('bgr', img)
    # 顯示灰圖
    cv2.imshow('gray', img_gray)
    
    cv2.imshow('b', B)
    cv2.imshow('g', G)
    cv2.imshow('r', R)  
    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
