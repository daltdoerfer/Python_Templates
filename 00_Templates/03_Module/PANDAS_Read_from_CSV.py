# https://stackoverflow.com/questions/41472015/knearest-neighbors-in-sklearn-valueerror-query-data-dimension-must-match-trai

import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors

df = pd.read_csv('KMeans_letter_recog.csv')

'''
X = np.array(df.drop(['Letter'], 1))
y = np.array(df['Letter'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2) #20% data used

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test) #test
print(accuracy) #this works fine

example = np.array([7,4,3,2,4,5,3,6,7,4,2,3,5,6,8,4])
example = X.reshape(len(example), -1)

prediction = clf.predict(example)
print(prediction) #error
'''