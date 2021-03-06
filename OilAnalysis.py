# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:16:41 2016
@author: Austin Cullar, Kem Andrew, Taylor Murphy
Software Engineering Project
Oil Dispersal Analysis
Dr. Colmaneres
"""

#The following section of code opens a folder of image files in the directory
#of this python script, converts it to binary, and saves the results in another
#directory.

##  NOTE  ##
#Depending on how the GUI ends up looking, we could offer a text box for the
#user to specify the folder name in which all of the images he/she is providing
#will be stored. This would allow us to avoid the hard-coding of a particular
#folder name. (Such as 'Images', as I have done below.)


from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
import glob

result_folder = 'BinaryImages'  #name for folder in which all resulting binary images will be saved.
images_folder = 'OilFilled'     #name for folder in which all original images will be kept.
binary_images = []              #list to hold all binary images
binaryImageNames = []           #list to hold all file names in the binary images folder
imageData = []                  #list to hold touples which hold data for each image
Bpixels = 0                     #variable to hold number of black pixels
Wpixels = 0                     #variable to hold number of white pixels
size = 128, 128

filenames = os.listdir(images_folder)               #getting names of all files in the Images directory

os.chdir(images_folder)                             #changing directory to 'Images" folder

for i in range(len(filenames)):
    image_file = Image.open(filenames[i])           #open color image

    
    image_file = image_file.convert('L')            #convert to pure black and white (next two lines)
    image_file = image_file.point(lambda x: 0 if x < 128 else 255, '1')

    binary_images.append(image_file)                #adding new binary image to binary_images list


os.chdir('..')                                      #backing out of images_folder

if not os.path.exists(result_folder):               #if the result_folder does not exist, create it
    os.makedirs(result_folder)

os.chdir(result_folder)                             #change directories to result folder

for i in range(len(binary_images)):                 #save all binary images in the result_folder
    
    image_file = binary_images[i]
    #image_file.save('result' + str(i) + '.png')
    image_file.save(filenames[i] + 'BINARY.png')

os.chdir('..')                                      #backing out of result_folder
os.chdir('BinaryImages')                            #change directories to BinaryImages

binaryImageNames = os.listdir(os.getcwd())
#print('\n'.join(binaryImageNames))

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(binaryImageNames[i])
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + ".thumbnail", "JPEG")

for i in range(len(binaryImageNames)):

    im = Image.open(binaryImageNames[i])
    print(binaryImageNames[i])

    PixList = im.getcolors()
    #print(PixList)

    for pixel in PixList:

        if pixel[1] == 0:
            Bpixels = pixel[0]
            print ("Black: ", pixel[0])

        elif pixel[1] == 255:
            Wpixels = pixel[0]
            print ("White: ", pixel[0])

        else:
            print ("Non B/W Pixel detected!!")

    #imageData.append((binaryImageNames[i], Bpixels, Wpixels))
    #print('\n'.join(imageData))
    
    
###  At this point, imageData contains information about all images in the
###  specified images file. Now comes the graph construction.


#x coordinate will be the positions in sequence of each image
#x = range(0,7)

#y coordinate will be the number of black pixels
#y = [i[1] for i in imageData]
#print(y)

#plt.plot(x, y)
#plt.axis([0, 25, 800000, 1400000])
#plt.xlabel("Position in Sequence")
#plt.ylabel("Pixels")
#plt.show()