#from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

def classifier(classifieur, X, y, foldersCount=10, testSize=0.2):
    #cross-validation
    scores = cross_val_score(classifieur, X, y, cv=foldersCount)
    score_final = "%0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
    print("Accuracy: ",score_final)
    
    return score_final

'''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testSize)
    classifieur.fit(X_train, y_train)
    y_predits = classifieur.predict(X_test)
    
    print("Taux de réussite : ", accuracy_score(y_test,y_predits))
'''