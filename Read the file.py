"""In this file we will load the text file that contains the color matching
function for CIE1931 and 2 degrees so we will use it to convert the image
from the multispectral image to a xyz image."""
import numpy as np
file = open("CIE1931_2deg.txt", "r")
data = []

for row in file:
    data.append([float(x) for x in row.split()])

t = np.transpose(data)
print(data, t)
