# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, "../traitement-images")

from os import path, makedirs
from PIL import Image as pImage
from PIL import ImageOps
from utils import load_paths, add_suffix
import itertools
from filtres import *

IN_PATH = './200x200'
#IN_PATH = './test'
OUT_PATH = './dataset_exp'

images_origin = load_paths(IN_PATH)

def transform(outpath, paths, fnc):

    result = []

    for image_path in paths:
        image = pImage.open(image_path)
        print('"%s" => %s' % (image_path, fnc.__name__))
        transformed = fnc(image)

        in_path = path.dirname(path.dirname(image_path))

        transformed_path = add_suffix(in_path, outpath, image_path, '_' + fnc.__name__)
        makedirs(path.dirname(transformed_path), exist_ok=True)
        transformed.save(transformed_path)

        result.append(transformed_path)


    return result


def to_folder(li):
    total = ""
    for fnc in li:
        total += fnc.__name__ + "+"
    
    return total[:-1]


filtres = [ copy, grayscale, blue, rotation_180, flip, invert, crop ]


combinations = []

for i in range(1, len(filtres)):
    combinations.extend( list(itertools.combinations(filtres, i)) )
    

for combi in combinations:
    outpath = OUT_PATH + "/" + to_folder(combi)
    makedirs(outpath, exist_ok=True)
    total = transform(outpath, images_origin, combi[0])
    
    for filtre in combi:
        if (filtre == combi[0]):
            continue
        total.extend(transform(outpath, total, filtre))