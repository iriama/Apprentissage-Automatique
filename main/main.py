from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier
from initialisation_donnees import init_data

pathName = '../traitement-images/sortie/c+rf/'

X,y = init_data(pathName)
classifieur = RandomForestClassifier(max_depth=2, random_state=0)

classifieur.fit(X,y)
dump(classifieur, 'monclf.joblib')

def predict_main(rep):
    classifieur2 = load('monclf.joblib')