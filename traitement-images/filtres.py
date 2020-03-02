# -*- coding: utf-8 -*-
from PIL import Image as pImage
from PIL import ImageOps

def copy(image):
    return image

def grayscale(image):
    return image.convert('L')

def blue(image):

    hsv = image.convert('RGB').convert('HSV')

    pixdata = hsv.load()

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            
            h, s, v = pixdata[x, y]

            if not (h >= 125 and h <= 155 and s >= 50 and v >= 50):
                pixdata[x, y] = (0, 0, 0)

    return hsv.convert('RGB')


def rotation_180(image):
    return image.rotate(180)

def flip(image):
    return image.transpose(pImage.FLIP_LEFT_RIGHT)

def invert(image):
    return ImageOps.invert(image.convert('RGB'))

def crop(image):
    

    width, height = image.size 

    new_width = min(width/4, 100)
    new_height = min(height/4, 100)

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    
    return image.crop((left, top, right, bottom))