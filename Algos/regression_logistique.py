from classifieur import classifier
from sklearn.linear_model import LogisticRegression

classifier('../traitement-images/sortie/final/', LogisticRegression(solver='liblinear', random_state=0), '../models/logistic_regression.joblib')