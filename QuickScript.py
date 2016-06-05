from PIL import Image
import os
import string

origCols = 1140
#span = 240

os.chdir("StitchingTestImages")
im1 = Image.open('TestImage1.jpg')
im2 = Image.open('TestImage2.jpg')

pix1 = im1.load()
pix2 = im2.load()

im1cols = im1.size[0]
im2cols = im2.size[0]

print(im1cols)
print(im2cols)

if(im1cols > im2cols):
    print('im2cols')
    cols = im2cols #use the image with the least number of columns for indexing
        #this shouldnt be an issue if all of the images are of the same size
else:
    print('im1cols')
    cols = im1cols #catch case in case the images are of the same size
"""
for i in range(0, cols):
    for j in range (0, cols):
        if (pix1[i,0] == pix2[j,0]):
            print('Success!')
            print(i,j)
"""

#need to compare every column of first image to the other

pix1List = []
pix2List = []

for i in range(0, cols):
    curCol = []
    for j in range (0, im1.size[1]):
        curCol.append(pix1[i,j])
    pix1List.append(curCol)

for i in range(0, cols):
    curCol = []
    for j in range (0, im1.size[1]-1):
        curCol.append(pix2[i,j])
    pix2List.append(curCol)

for i in range(0, len(pix1List)):
    for j in range(0, len(pix2List)):
        if (pix1List[i] == pix2List[j]):
            print('success')
            print('column ' + str(i) + ' if image 1 matches column ' + str(j) + ' of image 2.')
