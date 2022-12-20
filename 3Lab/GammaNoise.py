import random
import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plot 

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

x, y, z = np.shape(sample)

noise = np.zeros(shape=(sample.shape[0],sample.shape[1],sample.shape[2]))

erlang = np.zeros(256)

a = 2

b = 5

sum = 0

for i in range(0,256):
    step = float(i) * 0.1

    if(step >= 0 ):                                
        erlang[i] =   math.e**(-a * step) * ((a**b ) * step**(b-1))/math.factorial(int(b-1))
    else:
        erlang[i] = 0

x = np.linspace(0, 256, 256)
y = erlang

fig, ax = plot.subplots()

ax.bar(x, y)

plot.show()

d = np.cumsum(erlang)

for i in range(x):
    for j in range(y):
        random_number = np.random.rand()
        count = -10

        for k in d:
            if random_number <= k:
                for f in range(z):
                    noise[i][j][f] = count * 20

                break

            count += 1


for i in range(x):
    for j in range(y):
        for f in range(z):
            sample[i][j][f] += noise[i][j][f]

newImage = Image.fromarray(sample,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/ErlangNoise.jpg')