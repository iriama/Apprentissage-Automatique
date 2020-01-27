from PIL import Image

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import os
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score


class myData :
    classe = []
    matrice = []
    
    def addclasse(self, element):
        self.classe.append(element)
    def addmatrice(self, element):
        self.matrice.append(element)
    
data = myData()


for element in os.listdir('../traitement-images/sortie/normalisation/Mer/'):
    try:
        img = Image.open('../traitement-images/sortie/normalisation/Mer/' + element)
        M = np.array(img)
        data.addclasse(0)
        data.addmatrice(M)
    except IOError:
        print ('Erreur sur ouverture du fichier ')
    


for element in os.listdir('../traitement-images/sortie/normalisation/Ailleurs/'):
    try:
        img = Image.open('../traitement-images/sortie/normalisation/Ailleurs/' + element)
        M = np.array(img)
        data.addclasse(1)
        data.addmatrice(M)
    except IOError:
        print ('Erreur sur ouverture du fichier ')


np_M = np.array(data.matrice)
np_M = np_M.reshape(np_M.shape[0], np_M.shape[1] * np_M.shape[2] * np_M.shape[3])
#print(np_M.shape)


X = np_M
y = data.classe

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, X, y, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classifieur = GaussianNB()
classifieur.fit(X_train, y_train)
y_predits = classifieur.predict(X_test)

print("Taux de réussite : ", accuracy_score(y_test,y_predits))
