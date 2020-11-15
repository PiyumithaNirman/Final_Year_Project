import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv('Label_Set_IMDb - Sheet1.csv')

x = df.drop('IMDb_Label', axis=1)
y = df['IMDb_Label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

classifier = GaussianNB()
classifier.fit(x_train, y_train)

GaussianNB(priors=None, var_smoothing=1e-09)

y_pred = classifier.predict(x_test)
print y_pred

accuracy = accuracy_score(y_test, y_pred) * 100
print accuracy
