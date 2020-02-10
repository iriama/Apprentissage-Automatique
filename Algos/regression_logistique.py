from classifieur import classifier
from sklearn.linear_model import LogisticRegression

pathName = '../traitement-images/sortie/c+g/'

classifier(LogisticRegression(solver='liblinear', random_state=0), pathName)