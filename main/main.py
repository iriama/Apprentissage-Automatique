import sys
sys.path.insert(1, '../Algos')
sys.path.insert(2, '../traitement-images')

from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier
from initialisation_donnees import init_data
import os
import numpy as np
from PIL import Image
from normalisation import normaliser

pathName = '../traitement-images/sortie/c+rf/'

X,y = init_data(pathName)
classifieur = RandomForestClassifier(max_depth=2, random_state=0)

classifieur.fit(X,y)
dump(classifieur, 'monclf.joblib')

def predict_main(rep):
    classifieur2 = load('monclf.joblib')
    matrice = []
    #normaliser()
    for element in os.listdir(rep):
        try:
            img = Image.open(rep + element)
            matrice.append(np.array(img))
        except IOError:
            print ('Erreur sur ouverture du fichier ')
    
    #Xt = M
    np_M = np.array(matrice)
    np_M = np_M.reshape(np_M.shape[0], np_M.shape[1] * np_M.shape[2] * np_M.shape[3])
    Yt = classifieur2.predict(np_M)
    print('Classe image : ',Yt)
    return Yt

predict_main('imgTest/')