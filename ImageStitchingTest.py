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

print(img2.size[1]) #rows
print(img2.size[0]) #columns

rows = img1.size[1]
img1cols = img1.size[0]

img2cols = img2.size[0]
#no img2row variable since the number of rows will be the same for both images

#pixel[col, row]

count = 0

if(img1cols > img2cols):
    cols = img2cols #use the image with the least number of columns for indexing
        #this shouldnt be an issue if all of the images are of the same size
else:
    cols = img1cols #catch case in case the images are of the same size

match = True
found = False

while(match!=True):
    for j in range(0, cols): #columns
        for i in range(0, rows): #rows
            if (pixels1[(img1cols-1) -j, i] != pixels2[j, i]):
                match = False
                break
        if (match!= True):
            break


print(count)





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
