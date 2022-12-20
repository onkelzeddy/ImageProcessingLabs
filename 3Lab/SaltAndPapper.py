import random
import numpy as np
from PIL import Image

sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/image.jpg').convert('RGB'))

x,y = [len(sample),len(sample[0])]

random.seed(5)

maxColorNumber = 0

for i in range (len(sample)):
    for j in range(len(sample[0])):
        for l in range(len(sample[0][0])):
            if (sample[i][j][l] > maxColorNumber):
                maxColorNumber = sample[i][j][l]
        for l in range(len(sample[0][0])):
            sample[i][j][l] = maxColorNumber
        maxColorNumber = 0

NumberOfPixels = random.randint(700, 8000)

for i in range(NumberOfPixels):
    
    xForNoise = random.randint(0,x-1)

    yForNoise = random.randint(0,y-1)

    sample[xForNoise][yForNoise][0] = 255
    sample[xForNoise][yForNoise][1] = 255
    sample[xForNoise][yForNoise][2] = 255


random.seed(15)

NumberOfPixels = random.randint(700, 8000)

for i in range(NumberOfPixels):
    
    xForNoise = random.randint(0,x-1)

    yForNoise = random.randint(0,y-1)

    sample[xForNoise][yForNoise][0] = 0
    sample[xForNoise][yForNoise][1] = 0
    sample[xForNoise][yForNoise][2] = 0


newImage = Image.fromarray(sample,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/SaltAndPapper.jpg')