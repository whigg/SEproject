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
print(img1.size[0]) #columns

rows = img1.size[1]
img1cols = img1.size[0]

img2cols = img2.size[0]
#no img2row variable since the number of rows will be the same for both images

#pixel[col, row]

if(img1cols > img2cols):
    cols = img2cols #use the image with the least number of columns for indexing
        #this shouldnt be an issue if all of the images are of the same size
else:
    cols = img1cols #catch case in case the images are of the same size

#print(rows)
c=1
fail = False
while(fail!= True):
    for i in range(0,c):
        #print('.....')
        #print(i)
        for j in range(0,rows):
            #print('AAAA')
            if(pixels1[cols-i, j] != pixels2[i,j]):
                if (c<cols-1):
                    print(j)
                    c+=1
                    break
                else:
                    fail = True
                    break

print(fail)
