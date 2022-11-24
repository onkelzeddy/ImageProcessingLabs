from PIL import Image
import numpy as np

sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/37df66ec6110e0cf7dffe0a9799ee7bf.jpg').convert('RGB'))

sampleBlackAndWhite = sample
maxColorNumber = 0

for i in range (len(sampleBlackAndWhite)):
    for j in range(len(sampleBlackAndWhite[0])):
        for l in range(len(sampleBlackAndWhite[0][0])):
            if (sampleBlackAndWhite[i][j][l] > maxColorNumber):
                maxColorNumber = sampleBlackAndWhite[i][j][l]
        for l in range(len(sampleBlackAndWhite[0][0])):
            sampleBlackAndWhite[i][j][l] = maxColorNumber
        maxColorNumber = 0

maxLumen = 0
minLumen = 255

for i in range (len(sampleBlackAndWhite)):
    for j in range(len(sampleBlackAndWhite[0])):
        if (sampleBlackAndWhite[i][j][0]>maxLumen):
            maxLumen = sampleBlackAndWhite[i][j][0]

        if (sampleBlackAndWhite[i][j][0]<minLumen):
            minLumen = sampleBlackAndWhite[i][j][0]

difference = maxLumen - minLumen

if(150<difference<= 255 ):
    module = 10

if(75<difference<= 150 ):
    module = 20

if(0<difference<= 75 ):
    module = 30

middleColor = (maxLumen + minLumen)/2

for i in range (len(sampleBlackAndWhite)):
    for j in range(len(sampleBlackAndWhite[0])):
        if(max(sample[i][j])>middleColor):
            if (sample[i][j][0]+module > 255):
                sample[i][j][0] = 255
            else:    
                sample[i][j][0]=sample[i][j][0]+module
            
            if (sample[i][j][1]+module > 255):
                sample[i][j][1] = 255
            else:    
                sample[i][j][1]=sample[i][j][1]+module

            if (sample[i][j][2]+module > 255):
                sample[i][j][2] = 255
            else:    
                sample[i][j][2]=sample[i][j][2]+module
            

        if(max(sample[i][j])<middleColor):
            if(sample[i][j][0]-module < 0):
                sample[i][j][0] = 0
            else:
                sample[i][j][0]=sample[i][j][0]-module

            if(sample[i][j][1]-module < 0):
                sample[i][j][1] = 0
            else:
                sample[i][j][1]=sample[i][j][1]-module

            if(sample[i][j][2]-module < 0):
                sample[i][j][2] = 0
            else:
                sample[i][j][2]=sample[i][j][2]-module


newImage = Image.fromarray(sample,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/newImageContrast.jpg')