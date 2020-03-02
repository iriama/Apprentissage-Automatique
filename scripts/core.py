import sys
sys.path.insert(1, '../Algos')
sys.path.insert(2, '../traitement-images')

from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier
from initialisation_donnees import init_data
import os
import numpy as np
from PIL import Image
from multiplication import multiplier
from normalisation import normaliser
from pathlib import Path
import shutil
from timeit import default_timer as timer

MODEL_PATH = '../models/bayes.joblib'
NRM_PATH = "./normalisation/"
MLT_PATH = "./multiplication"

def predict(image_path, wanted_class, wanted_label=''):
    
    start = timer()
    
    nrm_dir = Path(NRM_PATH)
    mlt_dir = Path(MLT_PATH)

    # cleanup
    if nrm_dir.exists() and nrm_dir.is_dir():
        shutil.rmtree(nrm_dir)

    if mlt_dir.exists() and mlt_dir.is_dir():
        shutil.rmtree(mlt_dir)

    # Traitement image
    multiplier(image_path, MLT_PATH, True, False)
    normaliser(MLT_PATH, NRM_PATH)
    
    classifieur2 = load(MODEL_PATH)
    matrice = []

    for element in os.listdir(NRM_PATH):
        try:
            img = Image.open(NRM_PATH + element)
            matrice.append(np.array(img))
        except IOError:
            print ('Erreur sur ouverture du fichier ')
    
    #Xt = M
    np_M = np.array(matrice)
    np_M = np_M.reshape(np_M.shape[0], np_M.shape[1] * np_M.shape[2] * np_M.shape[3])
    Yt = classifieur2.predict(np_M)
    percent = np.sum(Yt == wanted_class)/len(Yt)

    print('Predictions : ', Yt)

    print('> Probabilité de la classe %s (%d): %0.2f' % (wanted_label, wanted_class, percent))

    print('  Prediction: %s (%d) = %s' % (wanted_label, wanted_class, ('Vrai' if percent >= 0.5 else 'Faux')))
    end = timer()
    print('Temps d\'execution (IO inclus) : %0.4f ms' % (end - start))

    return percent