from PIL import Image
import numpy as np

r = range(400,710,10)

w = 6000
h = 4200
last_image = np.zeros((h, w, len(r)))

for i, num in enumerate(r):
    path = "tiffs\MetaCow" + str(num) + "nm.tif"
    image = Image.open(path)
    image_array = np.asarray(image)
    #print(i)
    #print('image_array.shape  = ', image_array.shape)
    #print('last_image[:][:][num].shape = ', last_image[:][:][i].shape)
    #print('last_image[:,:,num].shape = ', last_image[:,:,i].shape)
    #print('last_image.shape = ', last_image.shape)
    last_image[:,:,i] = image_array

image8 = (last_image/256).astype('uint8')
print(image8[800][952])