
from cmath import pi
from unittest import result
from PIL import Image
from numpy import size
from pyparsing import col
import math

def drawCrew(pix, x, y, color, width):
  #pix[x + img.size[1] * y] = (255,255,255)

  lighter = (int(color[0] / 2), int(color[1] / 2), int(color[2] / 2))
  #background
  pix[x + width * (y)] = lighter
  pix[x + width * (y)+1] =lighter
  pix[x + width * (y)+2] =lighter
  pix[x + width * (y)+3] =lighter
  pix[x + width * (y)+4] =lighter
  pix[x + width * (y)+5] =lighter
  pix[x + width * (y+1)] =lighter
  pix[x + width * (y+1)+1] =lighter
  pix[x + width * (y+2)] =lighter
  pix[x + width * (y+3)] =lighter
  pix[x + width * (y+4)] =lighter
  pix[x + width * (y+4)+1] =lighter
  pix[x + width * (y+4)+3] =lighter
  pix[x + width * (y+5)] =lighter
  pix[x + width * (y+5)+1] =lighter
  pix[x + width * (y+5)+2] =lighter
  pix[x + width * (y+5)+3] =lighter
  pix[x + width * (y+5)+4] =lighter
  pix[x + width * (y+5)+5] =lighter
  pix[x + width * (y+4)+5] =lighter
  pix[x + width * (y+3)+5] =lighter
  pix[x + width * (y+2)+5] =lighter
  pix[x + width * (y+1)+5] =lighter

  #crewmate
  pix[x + width * (y+1) + 2] = color
  pix[x + width * (y+1) + 3] = color
  pix[x + width * (y+1) + 4] = color

  pix[x + width * (y+2) + 1] = color
  pix[x + width * (y+2) + 2] = color

  range = (int(color[0] / 4 + 180), int(color[1] / 4 + 180), int(color[2] / 4 + 180))
  pix[x + width * (y+2) + 3] = range
  pix[x + width * (y+2) + 4] = range

  pix[x + width * (y+3) + 1] = color
  pix[x + width * (y+3) + 2] = color
  pix[x + width * (y+3) + 3] = color
  pix[x + width * (y+3) + 4] = color

  #print(len(pix))
  #print(x + img.size[1] * (y+4) + 2)
  pix[x + width * (y+4) + 2] = color
  pix[x + width * (y+4) + 4] = color


def editTL(pix):
  pix[0] = (255,255,255)

def drawMe(img):
  pix = list(img.getdata())
  pix[0] = (255, 255, 255)
  pix[1] = (255, 255, 255)
  pix[2] = (255, 255, 255)
  pix[3] = (255, 255, 255)
  pix[4] = (255, 255, 255)
  pix[5] = (255, 255, 255)
  pix[img.size[1]] = (255,255,255)
  pix[img.size[1] * 2 - 1] = (255,255,255)
  pix[img.size[1] * 2] = (255,255,255)
  pix[img.size[1] * 3 - 1] = (255,255,255)
  pix[img.size[1] * 3] = (255,255,255)
  pix[img.size[1] * 4 - 1] = (255,255,255)
  pix[img.size[1] * 4] = (255,255,255)
  pix[img.size[1] * 5 - 1] = (255,255,255)
  pix[img.size[1] * 5] = (255,255,255)


  img2 = Image.new(img.mode, img.size)
  img2.putdata(pix)

  return(img2)

im = Image.open("64x64.png")

#print(list(im.getdata()))

pixval = list(im.getdata())

#print(pixval[0][0])
pixval[0] = (255, 255, 0)
im2 = Image.new(im.mode, im.size)

im2 = drawMe(im)

#print(list(im2.getdata()))

#im2.save('result.png', 'PNG')

color = (255,0,0)
im = Image.open("lenna.png")
pixval = list(im.getdata())

im2 = Image.new(im.mode, (im.size[0] * 6, im.size[1] * 6))
pix = list(im2.getdata())

i = 0
j = 0

while(j < im.size[1]):
  while(i < im.size[0]):
    drawCrew(pix, i * 6, j * 6, pixval[i + j * im.size[0]], im.size[0]*6)
    i += 1
    print(i + j * im.size[0])
  i = 0
  j += 1

im2.putdata(pix)
im2.save('result.png', 'PNG')

