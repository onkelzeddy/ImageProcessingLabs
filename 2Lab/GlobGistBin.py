import imp
from re import S
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot 

#sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/37df66ec6110e0cf7dffe0a9799ee7bf.jpg').convert('RGB'))
sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/8.jpg').convert('RGB'))

lumenArray = np.zeros(256)

maxColorNumber = 0
T = 0
lumenSum = 0

for i in range (len(sample)):
    for j in range(len(sample[0])):
        for l in range(len(sample[0][0])):
            if (sample[i][j][l] > maxColorNumber):
                maxColorNumber = sample[i][j][l]
        for l in range(len(sample[0][0])):
            sample[i][j][l] = maxColorNumber
        maxColorNumber = 0


for i in range (len(sample)):
    for j in range(len(sample[0])):
        lumenArray[sample[i][j][0]] = lumenArray[sample[i][j][0]] + 1


x = np.linspace(0, 256, 256)
y = lumenArray

fig, ax = plot.subplots()

ax.bar(x, y)

plot.show()

lumenMax = 0
lumenMaxIndex = 0
lumenMin = 260
lumenMinIndex = 0

for i in range (len(lumenArray)):
    if (lumenArray[i] > lumenMax):
        lumenMaxIndex = i
        lumenMax = lumenArray[i]

    if (lumenArray[i] < lumenMin):
        lumenMinIndex = i
        lumenMin = lumenArray[i]

lumenArray[lumenMaxIndex] = lumenArray[lumenMaxIndex] * 0.95

lumenArray[lumenMinIndex] = lumenArray[lumenMinIndex] * 0.95

for i in range (len(lumenArray)):
    lumenSum = lumenSum + lumenArray[i]

for i in range (len(lumenArray)):
    T = T + (lumenArray[i]*i)/lumenSum

print(T)

for i in range (len(sample)):
    for j in range (len(sample[0])):
        if(sample[i][j][0] > T):
            sample[i][j][0] = 255
            sample[i][j][1] = 255
            sample[i][j][2] = 255
        else:
            sample[i][j][0] = 0
            sample[i][j][1] = 0
            sample[i][j][2] = 0


newImage = Image.fromarray(sample,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/newImageGlobBin.jpg')
