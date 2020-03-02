from classifieur import classifier
from sklearn.ensemble import RandomForestClassifier

# Accuracy:  0.66 (+/- 0.07)
classifier('../traitement-images/sortie/final/', RandomForestClassifier(max_depth=2, random_state=0), '../models/random_forest.joblib')