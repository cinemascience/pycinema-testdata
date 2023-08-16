import random
import numpy
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im = Image.new(mode="RGB", size=(500, 500))
ImageFont.load_default()
il = ImageDraw.Draw(im)
il.rectangle([(0,0), (499, 499)], outline=(255,255,255), width=10)

numcols = 10
numrows = 20
numinset = 4

types = ['single', 'set', 'random']
values = [[round(random.uniform(-1000.0, 1000.0), 2)], [round(x,2) for x in numpy.random.uniform(-10.0, 10.0, numinset)]]

# create column names and types
colnames = []
coltypes = []
for i in range(0, numcols):
    colnames.append("col_" + str(i))
    # create a random set of column types
    coltypes.append(random.randint(0,2))

# overwrite columns
# coltypes = [2, 0]

# the last value is a file value
colnames.append("FILE")

print(",".join(map(str, colnames)))

# create the rows of data
for r in range(0, numrows):
    # initialize
    row = []

    for i in range(0, numcols):
        if types[coltypes[i]] == "single":
            row.append(values[coltypes[i]][0])

        elif types[coltypes[i]] == "set":
            idx = random.randint(0,numinset-1)
            row.append(values[1][idx])

        else:
            # random
            row.append(round(random.uniform(-100.00, 100.00), 2))

    # create a new image
    il.rectangle([(100,100), (400, 400)], fill=(0,0,0))
    il.text((250, 250), str(r) + ".png", fill=(255, 255, 255))
    im.save(str(r) + ".png")
    # add the test image as the last element        
    row.append(str(r) + ".png")
    print(",".join(map(str, row)))

