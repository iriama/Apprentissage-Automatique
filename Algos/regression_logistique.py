from sklearn.linear_model import LogisticRegression
from initialisation_donnees import init_data

X,y = init_data()

clf = LogisticRegression(random_state=0).fit(X, y)
clf.predict(X[:2, :])

clf.predict_proba(X[:2, :])

print(clf.score(X, y))
