# -*- coding: utf-8 -*-
"""

Created on Tue Feb 16 00:16:41 2016

@author: Austin Cullar, Kem Andrew, Taylor Murphy

Software Engineering Project
Oil Dispersal Analysis
Dr. Colmaneres

"""

#The following section of code opens in image file in the directory of the 
#script, converts it to binary, and saves the result in the same directory
#with the name "result".

##  NOTE  ##
#Depending on how the GUI ends up looking, we could offer a text box for the
#user to specify the folder name in which all of the images he/she is providing
#will be stored. This would allow us to avoid the hard-coding of a particular
#folder name. (Such as 'Images', as I have done below.)

from PIL import Image
import os

#list to hold all binary images
binary_images = []

#getting names of all files in the Images directory
filenames = os.listdir('Images')
print(filenames)
#changing directory to 'Images" folder
os.chdir('Images')

for i in range(len(filenames)):
    #open color image
    image_file = Image.open(filenames[i]) 

    #convert to black and white
    image_file = image_file.convert('1') 

    #adding new binary image to binary_images list
    binary_images.append(image_file)

for i in range(len(binary_images)):
    image_file = binary_images[i]
    image_file.save('result' + str(i) + '.png')
#image_file.save('result.png')
#######################################################################

#attempting to read all file names in the images directory

