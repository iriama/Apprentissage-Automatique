# -*- coding: utf-8 -*-

from PIL import Image
import os
import numpy as np

PATH = '../traitement-images/sortie/c+g/'

class myData :
    classe = []
    matrice = []
    
    def addclasse(self, element):
        self.classe.append(element)
    def addmatrice(self, element):
        self.matrice.append(element)
    
data = myData()

def init_data() :
    for element in os.listdir(PATH + 'Mer/'):
        try:
            img = Image.open(PATH + 'Mer/' + element)
            M = np.array(img)
            data.addclasse(0) #initialisation classe Mer
            data.addmatrice(M)
        except IOError:
            print ('Erreur sur ouverture du fichier ')
        
    
    
    for element in os.listdir(PATH + 'Ailleurs/'):
        try:
            img = Image.open(PATH + 'Ailleurs/' + element)
            M = np.array(img)
            data.addclasse(1) #initialisation classe Ailleurs
            data.addmatrice(M)
        except IOError:
            print ('Erreur sur ouverture du fichier ')
    
    
    np_M = np.array(data.matrice)
    np_M = np_M.reshape(np_M.shape[0], np_M.shape[1] * np_M.shape[2] * np_M.shape[3])
    
    X = np_M
    y = data.classe
    
    return X,y