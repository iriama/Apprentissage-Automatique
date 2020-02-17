# multiplication.py
# populer la base de donnees en manipulant les images de base
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

IN_PATH = '../donnees-projet/Data'
#IN_PATH = './sortie/test'
OUT_PATH = './sortie/crop'

print('- Dossier entree : "%s"' % IN_PATH)
print('- Dossier sortie : "%s"' % OUT_PATH)

# Tableau de chemins des fichiers images a  traiter
images_path = load_paths(IN_PATH)

# Creer le dossier de sortie s'il n'existe pas
makedirs(OUT_PATH, exist_ok=True)

def transform(paths, fnc, arg=None):

    name = fnc.__name__

    if arg is not None:
        name += "_" + str(arg)

    result = []

    for image_path in paths:
        image = pImage.open(image_path)
        print('"%s" => %s' % (image_path, name))

        if arg is not None:
            transformed = fnc(image)
        else:
            transformed = fnc(image)

        in_path = path.dirname(path.dirname(image_path))

        transformed_path = add_suffix(in_path, OUT_PATH, image_path, '_' + name)
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


def rotate(image, degree):
    return image.rotate(degree, expand=1)


def rotation_180(image):
    return rotate(image, 180)

def rotation_90(image):
    return rotate(image, 90)

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
#images_original = transform(images_path, copy)
#images_grayscale = transform(images_path, grayscale)
#images_blue = transform(images_path, blue)
#images_invert = transform(images_path, invert)

# Rotation/position
#images_rotate_180 = transform(images_path, rotation_180)# + images_grayscale + images_blue + images_invert, rotation_180)
#images_flip = transform(images_path, flip)# + images_grayscale + images_blue + images_invert, flip)
#images_crop = transform(images_path, crop) # + images_grayscale + images_blue + images_invert, crop)

# v2
#images_original = transform(images_path, copy)
#images_rotate_90 = transform(images_path, rotation_90)
#images_rotate_180 = transform(images_path, rotation_180)

# multi-rotate

images_original = transform(images_path, copy)
transform(images_path, crop)
'''
for i in range(10, 360, 10):
    transform(images_path, crop, i)
    '''