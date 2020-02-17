# normalisation.py
# redimensionner les images au meme format (200x200)
# https://machinelearningmastery.com/how-to-load-and-manipulate-images-for-deep-learning-in-python-with-pil-pillow/

from os import path, makedirs
from PIL import Image as pImage
from utils import load_paths


IN_PATH = '../main/imgTest'
OUT_PATH = '../main/imgTest'

print('- Dossier entree : "%s"' % IN_PATH)
print('- Dossier sortie : "%s"' % OUT_PATH)

# Tableau de chemins des fichiers images a  traiter
images_path = load_paths(IN_PATH)

# Creer le dossier de sortie s'il n'existe pas
makedirs(OUT_PATH, exist_ok=True)

# Traite les images
for image_path in images_path:
    image = pImage.open(image_path).convert('RGB')
    image_resized = image.resize((200, 200))
    print('> Image redimensionnee "%s" : %s => %s' % (image_path, image.size, image_resized.size))
    # image_resized.show()
    image_resized_path = OUT_PATH + image_path.replace(IN_PATH, '')
    makedirs(path.dirname(image_resized_path), exist_ok=True)


    name_split = path.basename(image_resized_path).split('.')
    name = name_split[0]
    extension = name_split[1]

    if (extension != 'jpeg'):
        image_resized_path.replace(extension, 'jpeg')

    image_resized.save(image_resized_path, 'JPEG')
    print('  Sauvegardee sous "%s"' % image_resized_path)