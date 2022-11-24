from PIL import Image
import numpy as np
sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/37df66ec6110e0cf7dffe0a9799ee7bf.jpg').convert('RGB'))
#sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/8.jpg').convert('RGB'))
sampleCopy = sample
halfColorNumber = 0

for j in range (1, len(sample[0])-2):
    for i in range(1, len(sample)-2):
        for m in range(3):
            for l in range(-1,2):
                for s in range(-1,2):
                    if ((l!=0 or s!=0) & (i+l>=0 and j+s>=0) & i+l<len(sample) and j+s<len(sample[0])):
                        halfColorNumber = halfColorNumber + sample[i+l][j+s][m]
            
            halfColorNumber = (halfColorNumber + sample[i][j][m])/9

            if(halfColorNumber > 250):
                halfColorNumber = 240
            
            sampleCopy[i][j][m] = halfColorNumber

            halfColorNumber = 0


newImage = Image.fromarray(sampleCopy,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/newImageHalf.jpg')