# normalisation.py
# rédimensionner les images à classifier à la même taille
# https://machinelearningmastery.com/how-to-load-and-manipulate-images-for-deep-learning-in-python-with-pil-pillow/

from os import listdir, walk, path, makedirs
from matplotlib import image as mImage
from PIL import Image as pImage

IN_PATH = '../donnees-projet/Data'
OUT_PATH = './sortie/normalisation'

print('- Dossier entrée : "%s"' % IN_PATH)
print('- Dossier sortie : "%s"' % OUT_PATH)

# Tableau de chemins des fichiers images à traiter
images_path = []

# Parcours le dossier et sous-dossiers Data pour peupler le tableau images_path
for currentpath, folders, files in walk(IN_PATH):
    for file in files:
        image_path = path.join(currentpath, file)
        images_path.append(image_path)

# Créer le dossier de sortie s'il n'existe pas
makedirs(OUT_PATH, exist_ok=True)

# Traite les images
for image_path in images_path:
    image = pImage.open(image_path)
    image_resized = image.resize((200, 200))
    print('> Image redimensionnée "%s" : %s => %s' % (image_path, image.size, image_resized.size))
    # image_resized.show()
    image_resized_path = OUT_PATH + image_path.replace(IN_PATH, '')
    makedirs(path.dirname(image_resized_path), exist_ok=True)
    image_resized.save(image_resized_path)
    print('  Sauvegardée sous "%s"' % image_resized_path)