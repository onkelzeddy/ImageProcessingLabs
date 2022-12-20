import random
import numpy as np
import math
from PIL import Image

sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/SaltAndPapper.jpg').convert('RGB'))

maxColorNumber = 0

for i in range (len(sample)):
    for j in range(len(sample[0])):
        for l in range(len(sample[0][0])):
            if (sample[i][j][l] > maxColorNumber):
                maxColorNumber = sample[i][j][l]
        for l in range(len(sample[0][0])):
            sample[i][j][l] = maxColorNumber
        maxColorNumber = 0

ksize = 3

geomean_res = 1

geomean = np.zeros_like(sample)

for i in range(len(sample)):
    for j in range(len(sample[0])):
        for l in range(-ksize,ksize):
            for s in range(-ksize,ksize):
                if ((i+l>=0 and j+s>=0) and (i+l<=len(sample)-1 and j+s<=len(sample[0])-1)):
                    if(sample[i+l][j+s][0] > 30):
                        geomean_res *= float(sample[i+l][j+s][0])**(1/((2*ksize)**(2)))
                    else:
                        geomean_res *= 30**(1/((2*(ksize))**(2)))
        
        geomean[i][j][0] = int(geomean_res)
        geomean[i][j][1] = int(geomean_res)
        geomean[i][j][2] = int(geomean_res)

        geomean_res = 1
                    

                    

newImage = Image.fromarray(geomean,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/geom.jpg')
