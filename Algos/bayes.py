from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.model_selection import cross_val_score
from initialisation_donnees import init_data

#recuperation données
X,y = init_data()


clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, X, y, cv=10)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classifieur = GaussianNB()
classifieur2 = svm.SVC(kernel='linear', C=1)
classifieur.fit(X_train, y_train)
classifieur2.fit(X_train, y_train)

y_predits = classifieur.predict(X_test)
y_predits2 = classifieur2.predict(X_test)


print("Taux de réussite : ", accuracy_score(y_test,y_predits))
print("Taux de réussite : ", accuracy_score(y_test,y_predits2))
