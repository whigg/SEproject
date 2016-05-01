###############################################
# Name: Taylor Murphy
# Image Analysis Controller Class
###############################################
from PIL import Image
import os
import cv2

#Start IAController ###########################################################
class IAController:
    
    #Class Variables ##########################################################    
    rawDataDir = ""                 #name for folder in which all original raw images will be kept.  
    binDataDir = ""                 #name for folder in which all resulting binary images will be saved.
    
    rawImageNames = []              #list to hold all raw image names
    binImages = []                  #list to hold all binary images
    binImageNames = []              #list to hold all binary image names 
    imageData = []                  #list of tuples containing pixel data for each image    
    ###########################################################################
    
    def __init__(self):                                             #This constructor will be overloaded to allow the GUI to pass directories
        #print("Initialized!")
        self.rawDataDir = "OilFilled"
        self.binDataDir = "BINARIES"
        
        if not os.path.exists(self.binDataDir):                     #if binDataDir does not exist, create it
            os.makedirs(self.binDataDir)

        self.rawImageNames = os.listdir(self.rawDataDir)            #get list of all image names in binDataDir
        #print('\n'.join(self.rawImageNames))        
        
    def ImageConverter(self):
        os.chdir(self.rawDataDir)                                   #changing directory to rawDataDir

        for i in range(len(self.rawImageNames)):
            self.rawDataDir = cv2.imread(self.rawImageNames[i], 0)
            self.rawDataDir = cv2.GaussianBlur(self.rawDataDir , (9, 9), -10)
            self.rawDataDir = cv2.adaptiveThreshold(self.rawDataDir, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)
            self.binImages.append(self.rawDataDir)                  #adding new binary image to binImages list

        os.chdir('..')                                              #backing out of rawDataDir
        os.chdir(self.binDataDir)                                   #change directories to binDataDir

        for i in range(len(self.binImages)):                        #save all binary images in binDataDir
            self.rawDataDir = self.binImages[i]
            cv2.imwrite(self.rawImageNames[i] + ' BIN.png', self.rawDataDir)            
            
        os.chdir('..')                                              #backing out of binDataDir
                
    def PixelCounter(self):
        self.binImageNames = os.listdir(self.binDataDir)        
        os.chdir(self.binDataDir)                                   #change directories to binDataDir
       
        Bpixels = 0                                                 #integer to hold number of black pixels
        Wpixels = 0                                                 #integer to hold number of white pixels        
        
        for i in range(len(self.binImageNames)):

            im = Image.open(self.binImageNames[i])
            print(self.binImageNames[i])

            PixList = im.getcolors()
            #print(PixList)

            for pixel in PixList:

                if pixel[1] == 0:
                    Bpixels = pixel[0]
                    print ("Black: ", Bpixels)

                elif pixel[1] == 255:
                    Wpixels = pixel[0]
                    print ("White: ", Wpixels)

                else:
                    print ("Non B/W Pixel detected!!")
                    
        os.chdir('..')                                              #backing out of binDataDir
        
    def Stitcher(self):
        return 0        
               
#End IAController #############################################################
        


#Start Tester #################################################################

experiment = IAController()
experiment.ImageConverter()
experiment.PixelCounter()
experiment.Stitcher()



#End Tester ###################################################################        