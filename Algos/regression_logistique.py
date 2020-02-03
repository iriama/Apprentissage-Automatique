from classifieur import classifier
from sklearn.linear_model import LogisticRegression

classifier(LogisticRegression(solver='liblinear', random_state=0))