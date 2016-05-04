# -*- coding: utf-8 -*-
"""
Austin Cullar
05/01/2016
This script will be used to test my image stitching algorithm.
"""

from PIL import Image
import os
import string

#print(os.listdir(os.getcwd()))
#os.chdir('StitchingTestImages')
#print(os.listdir(os.getcwd()))
filenames = os.listdir(os.getcwd())

#img1 = Image.open(filenames[0])
#img2 = Image.open(filenames[1])

img1 = Image.open('TestImage - Copy.jpg')
img2 = Image.open('TestImage - Copy (2).jpg')

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
iterFail = False
hardFail = False
while(hardFail!= True):
	iterFail = False
	for i in range(0,c):

		for j in range(0,(rows-1)):
			if(pixels1[((cols-1)-c+i), j] != pixels2[i,j]): #if the pixels are not equal,
				iterFail = True 			#the iteration fails
				if (i<(cols-1)):			#if you have not yet exhausted the number of columns,
					c+=1					#increment c first
				elif(i==(cols-1)):			#else if you HAVE exhausted the number of columns,
					hardFail = True			#hard fail, images contain no overlap
			
			else:							#
				print('pixels match!')		
				sys.exit()
			if(iterFail == True):
				break
		if (iterFail == True):
			break
print(hardFail)
