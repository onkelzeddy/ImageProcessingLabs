from cmath import sqrt
from PIL import Image
import numpy as np

sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/image.jpg').convert('RGB'))
maxColorNumber = 0

for i in range (len(sample)):
    for j in range(len(sample[0])):
        for l in range(len(sample[0][0])):
            if (sample[i][j][l] > maxColorNumber):
                maxColorNumber = sample[i][j][l]
        for l in range(len(sample[0][0])):
            sample[i][j][l] = maxColorNumber
        maxColorNumber = 0




u = np.zeros(len(sample)*len(sample[0]))
u = u.reshape(len(sample),len(sample[0]))

g = np.zeros(len(sample)*len(sample[0]))
g = g.reshape(len(sample),len(sample[0]))
counterForPixels = 0

for i in range (0, len(sample)):
    for j in range (0, len(sample[0])):
        
        for l in range(-5,5):
            for s in range(-5,5):
                if ((i+l>=0 and j+s>=0) and (i+l<=len(sample)-1 and j+s<=len(sample[0])-1)):
                    counterForPixels+=1
                    u[i][j] = u[i][j] + sample[i+l][j+s][0]
        u[i][j] = u[i][j] * ((counterForPixels)**(-1))

        counterForPixels = 0
        
        for l in range(-5,5):
            for s in range(-5,5):
                if ((i+l>=0 and j+s>=0) and (i+l<len(sample) and j+s<len(sample[0]))):
                    counterForPixels+=1
                    g[i][j] = g[i][j] + (sample[i+l][j+s][0] - u[i][j])**2

        g[i][j] = (abs(g[i][j])*(counterForPixels**(-1)))**0.5
        
        counterForPixels = 0


T = np.zeros(len(sample)*len(sample[0]))
T = T.reshape(len(sample),len(sample[0]))

for i in range (0, len(sample)):
    for j in range (0, len(sample[0])):
        T[i][j] = u[i][j] + (3)*g[i][j]
    


for i in range (0, len(sample)):
    for j in range (0, len(sample[0])):
        if(min(T[i]) < sample[i][j][0]):
            sample[i][j][0] = 0
            sample[i][j][1] = 0
            sample[i][j][2] = 0
        else:
            sample[i][j][0] = 255
            sample[i][j][1] = 255
            sample[i][j][2] = 255

newImage = Image.fromarray(sample,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/newImageAdBin.jpg')