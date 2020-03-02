from sklearn.model_selection import cross_val_score
from joblib import dump
from initialisation_donnees import init_data

def classifier(dataset_path, classifieur, dump_path='', foldersCount=10, testSize=0.2):

    X, y = init_data(dataset_path)

    #cross-validation
    scores = cross_val_score(classifieur, X, y, cv=foldersCount)
    score_final = "%0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
    print("Accuracy: ",score_final)

    if dump_path:
        # fititng
        classifieur.fit(X, y)
        # saving
        dump(classifieur, dump_path) 
    
    return score_final