from classifieur import classifier
from sklearn.linear_model import LogisticRegression
from initialisation_donnees import init_data


pathName = '../traitement-images/sortie/c+i/'
X,y = init_data(pathName)

classifier(LogisticRegression(solver='liblinear', random_state=0), X,y)