from classifieur import classifier
from sklearn.naive_bayes import GaussianNB

# Accuracy:  0.62 (+/- 0.07)
classifier('../traitement-images/sortie/final/', GaussianNB(), '../models/bayes.joblib')