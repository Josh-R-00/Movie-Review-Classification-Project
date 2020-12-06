import numpy as np
from sklearn.svm import LinearSVC
from Classifier import Array_Data

clf = LinearSVC(random_state=0, tol=1e-4, max_iter=1000)

X_train = Array_Data.getTrainFeatures()
y_train = Array_Data.getTrainLabels()
X_test = Array_Data.getTestFeatures()
y_test = Array_Data.getTestLabels()

clf.fit(X_train, y_train)
print("Finished Fit. Now predicting\n")

print(clf.score(X_test, y_test))

