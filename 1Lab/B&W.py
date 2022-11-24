from PIL import Image
import numpy as np
sample = np.array(Image.open('/home/onkelzeddy/Workspace/ImageProcessing/37df66ec6110e0cf7dffe0a9799ee7bf.jpg').convert('RGB'))
print(len(sample[0][0]))
maxColorNumber = 0

for i in range (len(sample)):
    for j in range(len(sample[0])):
        for l in range(len(sample[0][0])):
            if (sample[i][j][l] > maxColorNumber):
                maxColorNumber = sample[i][j][l]
        for l in range(len(sample[0][0])):
            sample[i][j][l] = maxColorNumber
        maxColorNumber = 0


newImage = Image.fromarray(sample,'RGB')
newImage.save('/home/onkelzeddy/Workspace/ImageProcessing/newImage.jpg')