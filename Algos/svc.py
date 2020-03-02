from classifieur import classifier
from sklearn.svm import SVC

classifier('../traitement-images/sortie/final/', SVC(kernel='linear', C=1), '../models/svc.joblib')