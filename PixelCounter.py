from PIL import Image
im = Image.open('dogImage.jpgBINARY.PNG')

PixList = im.getcolors()

for pixel in PixList:
    if pixel[1] == 0:
        print ("Black: ", pixel[0])
        
    elif pixel[1] == 255:     
        print ("White: ", pixel[0])
    
    else:
        print ("Non B/W Pixel detected!!")