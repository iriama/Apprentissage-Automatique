from os import walk, path
from PIL import Image as pImage

def load_paths(in_folder):
    images_path = []

    for currentpath, folders, files in walk(in_folder):
        for file in files:
            image_path = path.join(currentpath, file)
            images_path.append(image_path)
    
    return images_path

def add_suffix(in_path, out_path, source_path, suffix):

    path_split = path.basename(source_path).split('.')
    name = path_split[0]
    extension = path_split[1]

    folder = out_path + path.dirname(source_path).replace(in_path, '')

    return path.join(folder, name + suffix + '.' + extension)

