# multiplication.py
# populer la base de données en manipulant les images de base (noir et blanc, rotation et ajout de bruit aléatoire)

from os import path, makedirs
from PIL import Image as pImage
from utils import load_paths, add_suffix
import numpy as np
import sys

IN_PATH = '../donnees-projet/Data'
# IN_PATH = './sortie/test'
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
        
        transformed_path = add_suffix(IN_PATH, OUT_PATH, image_path, '_' + fnc.__name__)
        makedirs(path.dirname(transformed_path), exist_ok=True)
        transformed.save(transformed_path)

        result.append(transformed_path)


    return result

def copy(image):
    return image

def grayscale(image):
    return image.convert('L')

def blue(img):

    hsv = img.convert('HSV')

    pixdata = hsv.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            
            h, s, v = pixdata[x, y]

            if not (h >= 125 and h <= 155 and s >= 50 and v >= 50):
                pixdata[x, y] = (0, 0, 0)

    return hsv.convert('RGB')

images_original = transform(images_path, copy)
images_grayscale = transform(images_path, grayscale)
images_blue = transform(images_path, blue)