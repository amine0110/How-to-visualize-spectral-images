import numpy as np
from PIL import Image

"""img_w, img_h = 200, 200
data = np.zeros((img_h, img_w, 3), dtype=np.uint8)
data[100, 100] = [255, 0, 0]
img = Image.fromarray(data)
img.save('test.png')
img.show()"""

last_image = np.zeros((4200, 6000, 3))
path1 = "tiffs\MetaCow380nm.tif"
path2 = "tiffs\MetaCow400nm.tif"
path3 = "tiffs\MetaCow430nm.tif"
image1 = Image.open(path1)
image2 = Image.open(path2)
image3 = Image.open(path3)



image_matrix1 = np.asarray(image1)
image_matrix2 = np.asarray(image2)
image_matrix3 = np.asarray(image3)
print(image_matrix1.shape)

image_1 = (image_matrix1/256).astype('uint8')
image_2 = (image_matrix2/256).astype('uint8')
image_3 = (image_matrix3/256).astype('uint8')
print(image_1.shape)

last_image[:, :, 0] = image_1
last_image[:, :, 1] = image_2
last_image[:, :, 2] = image_3

last_image = last_image.astype('uint8')

#last_image[:, :, 1] = image_2[:, :]
#last_image[:, :, 2] = image_3[:, :]
print(last_image.shape)
img1 = Image.fromarray(last_image)
img2 = Image.fromarray(image_1)
img1.show()
img2.show()








