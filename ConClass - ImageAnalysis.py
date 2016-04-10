###############################################
# Name: Taylor Murphy
# Image Analysis Controller Class
###############################################
from PIL import Image
import os

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
        self.rawDataDir = "5-13 m4-3 300nm ipa evapo"
        self.binDataDir = "BINARIES"
        
        if not os.path.exists(self.binDataDir):                     #if binDataDir does not exist, create it
            os.makedirs(self.binDataDir)

        self.rawImageNames = os.listdir(self.rawDataDir)            #get list of all image names in binDataDir
        #print('\n'.join(self.rawImageNames))        
        
    def ImageConverter(self):
        os.chdir(self.rawDataDir)                                   #changing directory to rawDataDir

        for i in range(len(self.rawImageNames)):
            self.rawDataDir = Image.open(self.rawImageNames[i])     #open raw color image
            self.rawDataDir = self.rawDataDir.convert('L')          #convert to pure black and white (next two lines)
            self.rawDataDir = self.rawDataDir.point(lambda x: 0 if x < 128 else 255, '1')
            self.binImages.append(self.rawDataDir)                  #adding new binary image to binImages list

        os.chdir('..')                                              #backing out of rawDataDir
        os.chdir(self.binDataDir)                                   #change directories to binDataDir

        for i in range(len(self.binImages)):                        #save all binary images in binDataDir
            self.rawDataDir = self.binImages[i]
            self.rawDataDir.save(self.rawImageNames[i] + ' BIN.png')

        os.chdir('..')                                              #backing out of binDataDir
                
    def PixelCounter(self):
        self.binImageNames = os.listdir(self.binDataDir)        
        os.chdir(self.binDataDir)                                   #change directorie to binDataDir
       
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
    
    def AutoThreshold(self):
        return 0
        
    def Stitcher(self):
        return 0        
               
#End IAController #############################################################
        


#Start Tester #################################################################

experiment = IAController()
experiment.ImageConverter()
experiment.PixelCounter()
experiment.AutoThreshold()
experiment.Stitcher()



#End Tester ###################################################################        