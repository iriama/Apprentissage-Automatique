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


def analyser_donnees(pathName, algo, imgType):
    X,y = init_data(pathName)

    with open('donnees.csv', 'a', newline='') as csvfile:
            #spamwriter = csv.writer(csvfile, delimiter=' ',
                                #quotechar='|', quoting=csv.QUOTE_MINIMAL)
            fieldnames = ['type image','nom algo', 'cross validation', 'accuracy']
            spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #spamwriter.writeheader()
            
            for i in algo:
                cross_validation, accuracy = classifier(i.classifieur, X, y)
                spamwriter.writerow({'type image': imgType, 'nom algo': i.name , 'cross validation': cross_validation, 'accuracy': accuracy})
            

bayes = algo('Bayes', GaussianNB())
regression_logistique = algo('regression logistique', LogisticRegression(solver='liblinear', random_state=0))
svc = algo('svc', SVC(kernel='linear', C=1))
foret_aleatoire = algo('foret_aleatoire', RandomForestClassifier(max_depth=2, random_state=0))

algo = [bayes, regression_logistique, svc, foret_aleatoire]
pathName = '../traitement-images/sortie/c+g/'

analyser_donnees(pathName,algo, 'c+g')