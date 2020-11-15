import numpy as np
import mahotas
import mahotas.demos
from skimage import data
from skimage.color import rgb2xyz, xyz2rgb
from PIL import Image


xyzImage = np.load("xyzImage_new.npy")
img2 = Image.fromarray(xyzImage)
img2.show()
img2.save("XYZ_Image.tif")


img_rgb = xyz2rgb(xyzImage)
img_rgb *= 255

img_rgb = img_rgb.astype('uint8')

print(type(img_rgb))
img = Image.fromarray(img_rgb)
img.show()
img.save("RGB_Image.tif")