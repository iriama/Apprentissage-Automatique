# multiplication.py
# populer la base de données en manipulant les images de base (noir et blanc, rotation et ajout de bruit aléatoire)

from os import path, makedirs
from PIL import Image as pImage
from utils import load_paths, add_suffix

IN_PATH = './sortie/normalisation'
OUT_PATH = './sortie/multiplication'

print('- Dossier entrée : "%s"' % IN_PATH)
print('- Dossier sortie : "%s"' % OUT_PATH)

# Tableau de chemins des fichiers images à traiter
images_path = load_paths(IN_PATH)

# Créer le dossier de sortie s'il n'existe pas
makedirs(OUT_PATH, exist_ok=True)

# Traite les images
for image_path in images_path:
    image = pImage.open(image_path)


    print('> Multiplication de l\'image "%s"' % image_path)

    # Original
    image_original_path = add_suffix(IN_PATH, OUT_PATH, image_path, '_original')
    makedirs(path.dirname(image_original_path), exist_ok=True)
    image.save(image_original_path)

    print('  Copie simple de l\'image originale "%s"' % image_original_path)
    
    # Noir et blanc
    image_grayscale = image.convert('LA')
    image_grayscale_path = add_suffix(IN_PATH, OUT_PATH, image_path, '_grayscale')
    makedirs(path.dirname(image_grayscale_path), exist_ok=True)
    image_grayscale.save(image_grayscale_path)

    print('  Filtre noir et blanc %s' % image_grayscale_path)

    input()
