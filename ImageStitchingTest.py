# -*- coding: utf-8 -*-
"""
Austin Cullar

05/01/2016

This script will be used to test my image stitching algorithm.
"""

from PIL import Image
import os


#print(os.listdir(os.getcwd()))
os.chdir('StitchingTestImages')
#print(os.listdir(os.getcwd()))
filenames = os.listdir(os.getcwd())

img1 = Image.open(filenames[0])
img2 = Image.open(filenames[1])

pixels1 = img1.load() #ceating a pixel map for first Image
pixels2 = img2.load() #creating a pixel map for second Image

print(img1.size[1]) #rows
print(img1.size[0])# columns

for i in range(img1.size[1]):
    for j in range(img1.size[0]):
        for k in range(img2.size[0]):





"""
for i in range(img.size[0]): #for every pixel:
    for j in range (img.size[1]):
"""
"""


img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 100) # set the colour accordingly

img.show()
"""
