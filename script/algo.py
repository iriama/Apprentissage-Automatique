import sys
sys.path.insert(1, '../Algos')

import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from classifieur import classifier
from initialisation_donnees import init_data


class algo :
    name = ''
    classifieur = 0
    
    def __init__(self, name, classifieur):
        self.name = name
        self.classifieur = classifieur


def analyser_donnees(pathName, algo, bd):
    X,y = init_data(pathName)

    with open('donnees.csv', 'a', newline='') as csvfile:
            #spamwriter = csv.writer(csvfile, delimiter=' ',
                                #quotechar='|', quoting=csv.QUOTE_MINIMAL)
            fieldnames = ['BD','nom algo', 'cross validation']
            spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #spamwriter.writeheader()
            
            for i in algo:
                cross_validation = classifier(i.classifieur, X, y)
                spamwriter.writerow({'BD': bd, 'nom algo': i.name , 'cross validation': cross_validation})
            

bayes = algo('Bayes', GaussianNB())
regression_logistique = algo('regression logistique', LogisticRegression(solver='liblinear', random_state=0))
svc = algo('svc', SVC(kernel='linear', C=1))
foret_aleatoire = algo('foret_aleatoire', RandomForestClassifier(max_depth=2, random_state=0))

algo = [bayes, regression_logistique, svc, foret_aleatoire]
pathName = '../traitement-images/sortie/c+i/'

analyser_donnees(pathName,algo, 'c+i')