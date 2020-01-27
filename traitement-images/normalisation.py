# normalisation.py
# redimensionner les images au même format (200x200)
# https://machinelearningmastery.com/how-to-load-and-manipulate-images-for-deep-learning-in-python-with-pil-pillow/

from os import path, makedirs
from PIL import Image as pImage
from utils import load_paths

IN_PATH = '../donnees-projet/Data'
OUT_PATH = './sortie/normalisation'

print('- Dossier entrée : "%s"' % IN_PATH)
print('- Dossier sortie : "%s"' % OUT_PATH)

# Tableau de chemins des fichiers images à traiter
images_path = load_paths(IN_PATH)

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