import sys
sys.path.insert(1, '../Data')
import Mer

from PIL import Image

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import os
for element in os.listdir('../Data/Mer/'):
    Image.open(element);


donnees = load_iris()
X = donnees.data
y = donnees.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

classifieur = GaussianNB()
classifieur.fit(X_train, y_train)
y_predits = classifieur.predict(X_test)
print("Taux de réussite : ", accuracy_score(y_test,y_predits))