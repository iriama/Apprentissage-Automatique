# multiplication.py
# populer la base de données en manipulant les images de base
# noir et blanc
# essayer d'isoler le bleu
# rotation 180
# rotation sur l'axe horizontal
# 200x200 depuis le centre
# inversion des couleurs

from os import path, makedirs
from PIL import Image as pImage
from PIL import ImageOps
from utils import load_paths, add_suffix
import numpy as np
import sys

IN_PATH = '../donnees-projet/Data'
#IN_PATH = './sortie/test'
OUT_PATH = './sortie/multiplication'

print('- Dossier entrée : "%s"' % IN_PATH)
print('- Dossier sortie : "%s"' % OUT_PATH)

# Tableau de chemins des fichiers images à traiter
images_path = load_paths(IN_PATH)

# Créer le dossier de sortie s'il n'existe pas
makedirs(OUT_PATH, exist_ok=True)

def transform(paths, fnc):

    result = []

    for image_path in paths:
        image = pImage.open(image_path)
        print('"%s" => %s' % (image_path, fnc.__name__))
        transformed = fnc(image)

        in_path = path.dirname(path.dirname(image_path))

        transformed_path = add_suffix(in_path, OUT_PATH, image_path, '_' + fnc.__name__)
        makedirs(path.dirname(transformed_path), exist_ok=True)
        transformed.save(transformed_path)

        result.append(transformed_path)


    return result

def copy(image):
    return image

def grayscale(image):
    return image.convert('L')

def blue(image):

    hsv = image.convert('HSV')

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


# Couleurs
images_original = transform(images_path, copy)
images_grayscale = transform(images_path, grayscale)
images_blue = transform(images_path, blue)
images_invert = transform(images_path, invert)

# Rotation/position
images_rotate_180 = transform(images_path + images_grayscale + images_blue + images_invert, rotation_180)
images_flip = transform(images_path + images_grayscale + images_blue + images_invert, flip)
images_crop = transform(images_path + images_grayscale + images_blue + images_invert, crop)
