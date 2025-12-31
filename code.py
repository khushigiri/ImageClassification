import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X = np.load("X.npy")
y = np.load("y.npy")

model = SVC(kernel="linear")
model.fit(X, y)

predictions = model.predict(X)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y, predictions))
