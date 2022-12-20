import math

import numpy as np
from PIL import Image

sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/ErlangNoise.jpg').convert('RGB'))

def expan(a, b, c, d):
    standartDeviationForCord = ((((a - ((a+b+c+d)/4))**2) + ((b - ((a+b+c+d)/4))**2) + ((c - ((a+b+c+d)/4))**2) + ((d - ((a+b+c+d)/4))**2))/4)**0.5

    standartDeviationForValue = ((((float(sample[a][b][0]) - (float((sample[a][b][0]) + float(sample[c][d][0]))/2))**2) + ((float(sample[c][d][0]) - ((float(sample[a][b][0]) + float(sample[c][d][0]))/2))**2))/2)**0.5


    return math.e**(((((a-c)**2) + ((b-d)**2))/((-2)*(standartDeviationForCord**2))) + ((abs(float(sample[a][b][0]) - float(sample[c][d][0]))**2)/((-2)*(standartDeviationForCord**2))))

def expan2(a, b, c, d,sigma_d,sigma_r):
    return math.e**(((((a-c)**2) + ((b-d)**2))/((-2)*(sigma_d**2))) + ((abs(float(sample[a][b][0]) - float(sample[c][d][0]))**2)/((-2)*(sigma_r**2))))

sampleD = sample
wLower = 0.0
wUper = 0.0

for i in range (0,len(sample)):
    for j in range(0,len(sample[0])):
        for l in range(-5,5):
            for s in range(-5,5):
                if ((i+l>=0 and j+s>=0) and (i+l<=len(sample)-1 and j+s<=len(sample[0])-1) and  (l!=0 and s!=0)):
                    wLower += expan2(i,j,i+l,j+s,2,150)

                    wUper += (expan2(i,j,i+l,j+s,2,150)*sample[i+l][j+s][0])



        sampleD[i][j][0] = wUper/wLower
        sampleD[i][j][1] = wUper/wLower
        sampleD[i][j][2] = wUper/wLower

        wLower = 0
        wUper = 0


newImage = Image.fromarray(sampleD,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/Bilateral.jpg')

        