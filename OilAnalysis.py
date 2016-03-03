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

from PIL import Image
import os

binary_images = []

#getting names of all files in the Images directory
filenames = os.listdir('Images')
print(filenames)

#changing directory to 'Images" folder
os.chdir('Images')

image_file = Image.open("k3.jpg") #open color image

image_file = image_file.convert('1') #convert to black and white

binary_images.append(image_file)
print(binary_images)
#image_file.save('result.png')

#######################################################################

#attempting to read all file names in the images directory

