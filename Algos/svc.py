from classifieur import classifier
from sklearn.svm import SVC

classifier(SVC(kernel='linear', C=1))