import csv
import pickle

import pandas as pd

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('Label_With_Finance_Rate - Sheet1.csv')
results = []

print("Shape:", data.shape)

# column names
print("\nFeatures:", data.columns)

# storing the feature matrix (X) and response vector (y)
X = data[data.columns[:-1]]
y = data[data.columns[-1]]

# printing first 5 rows of feature matrix
print("\nFeature matrix:\n", X.head())

# printing first 5 values of response vector
print("\nResponse vector:\n", y.head())

# splitting X and y into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# printing the shapes of the new X objects
print(X_train.shape)
print(X_test.shape)

# printing the shapes of the new y objects
print(y_train.shape)
print(y_test.shape)

# training the model on training set

knn = KNeighborsClassifier(n_neighbors=3)
# knn = RandomForestClassifier(n_estimators=100)
# knn = SVC(kernel='rbf')
# knn = GaussianNB()
# knn = DecisionTreeClassifier()
kk
knn.fit(X_train, y_train)

# making predictions on the testing set
y_pred = knn.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)

print("kNN model accuracy 1:", metrics.accuracy_score(y_test, y_pred))

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(knn, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
# sample = [
#     [30, 4662, 858373000, 2019, 356000000, 2.39, 181, 8.4, 23, 21, 1, 4, 14, 361, 88, 2, 40, 113, 93, 46, 0, 7, 53, 475,
#      63, 3, 29, 3, 5, 78, 2, 41, 55, 104, 11, 1, 2, 16, 343, 17, 1, 0, 1, 189, 42, 3, 3, 13],
#     [22, 4348, 334201140, 2017, 175000000, 2.39, 133, 7.4, 224, 24, 0, 0, 4, 417, 12, 0, 19, 24, 452, 78, 1, 61, 41,
#      634, 85, 2, 38, 2, 148, 43, 1, 77, 105, 321, 22, 0, 0, 4, 298, 32, 0, 0, 1, 239, 56, 0, 0, 4]]
with open("pre.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        results.append(row)  # shape of dataset
    print (results)
    prediction = loaded_model.predict(results)
print(prediction)
print(result)

# preds = knn.predict(sample)
# pred_species = [iris.target_names[p] for p in prediction]
# print("Predictions:", pred_species)
