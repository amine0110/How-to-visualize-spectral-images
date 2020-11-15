from PIL import Image
import numpy as np

file = open("CIE1931_2deg.txt", "r")
r = range(400,710,10)
w = 6000
h = 4200
last_image = np.zeros((h, w, len(r)))
data = []

for row in file:
    data.append([float(x) for x in row.split()])

for i, num in enumerate(r):
    path = "tiffs\MetaCow" + str(num) + "nm.tif"
    image = Image.open(path)
    image_array = np.asarray(image)
    image_array = (image_array / 256).astype('uint8')

    last_image[:, :, i] = image_array

last_image = last_image.astype('uint8')


xyzImage = np.zeros((h, w, 3))

"""result = np.matmul(image8[900][620], data)
print(image8[900][620])
print(result)"""
data_t = np.transpose(data)
for line in range(0,h):
    for column in range(0,w):
        xyzImage[line, column] = np.matmul(data_t, last_image[line, column])
xyzImage = xyzImage.astype('uint8')
np.save("xyzImage_new.npy", xyzImage)
print(xyzImage)