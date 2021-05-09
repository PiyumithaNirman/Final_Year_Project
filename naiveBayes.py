import csv

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import xgboost as xgb
from sklearn.svm import SVC

df = pd.read_csv('Label_With_IMDb_Rate - Sheet1.csv')
results = []

x = df.drop('IMDb_Label', axis=1)
y = df['IMDb_Label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# classifier = GaussianNB()
classifier = RandomForestClassifier(n_estimators=100)
# classifier = LogisticRegression(random_state = 0)
# classifier = SVC(kernel='rbf')
# classifier = xgb.XGBClassifier()
classifier.fit(x_train, y_train)

# GaussianNB(priors=None, var_smoothing=1e-09)

y_pred = classifier.predict(x_test)
print y_pred

accuracy = accuracy_score(y_test, y_pred)
print accuracy

# save the model to disk
filename = 'finalized_model_IMDb.sav'
pickle.dump(classifier, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(x_test, y_test)
print(result)

with open("pre1.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        results.append(row)  # shape of dataset
    print (results)
    prediction = loaded_model.predict(results)
print(prediction)
pd.DataFrame(prediction).to_csv('prediction.csv')
