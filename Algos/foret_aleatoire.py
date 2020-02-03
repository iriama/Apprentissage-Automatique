from classifieur import classifier
from sklearn.ensemble import RandomForestClassifier

classifier(RandomForestClassifier(max_depth=2, random_state=0))