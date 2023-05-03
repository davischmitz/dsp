# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:36:24 2018

@author: Jean Schmith
"""

import cv2
img = cv2.imread("lena.jpg")

# Monta o retangulo para ser o alvo do corte.
y = 50
x = 50
h = 100
w = 100

crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
