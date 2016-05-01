###############################################
# Name: Taylor Murphy
# AutoThresholding Tester
###############################################
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Start AutoThresholding Tester ################################################
imgRaw = cv2.imread('DI evapo 2fps-000000.png', 0)
imgRaw = cv2.GaussianBlur(imgRaw , (9, 9), -10)

imgBin = cv2.adaptiveThreshold(imgRaw, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)

cv2.imwrite('DI evapo 2fps-000000BIN.png', imgBin)


#End AutoThresholding Tester ##################################################
