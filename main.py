
from PIL import Image

im = Image.open("gyrb.png")

print(list(im.getdata()))

pixval = list(im.getdata())

print(pixval[0][0])
pixval[0] = (0, 255, 0)
im2 = Image.new(im.mode, im.size)

#im2 = im2.transform((2,2), Image.EXTENT, (0,0,9,5))

im2.putdata(pixval)
#im2.show()

im2.save('result.png', 'PNG')