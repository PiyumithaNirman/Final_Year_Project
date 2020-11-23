import pandas as pd

dataset = pd.read_csv("Final IMDb Lebel set - Sheet1.csv")

dataset.head()

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# number = LabelEncoder()
nameencoder = LabelEncoder()
actor1encoder = LabelEncoder()
actor2encoder = LabelEncoder()
actor3encoder = LabelEncoder()
genresencoder = LabelEncoder()
imdbscoreencoder = LabelEncoder()
budgetencoder = LabelEncoder()
grossencoder = LabelEncoder()
profitencoder = LabelEncoder()

dataset['director_name'] = nameencoder.fit_transform(dataset['director_name'])
dataset['actor_1_name'] = actor1encoder.fit_transform(dataset['actor_1_name'])
dataset['actor_2_name'] = actor2encoder.fit_transform(dataset['actor_2_name'].astype(str))
dataset['actor_3_name'] = actor3encoder.fit_transform(dataset['actor_3_name'].astype(str))
dataset['country'] = actor1encoder.fit_transform(dataset['country'])

dataset['Action'] = 0
dataset['Adventure'] = 0
dataset['Sci-Fi'] = 0
dataset['Romance'] = 0
dataset['Animation'] = 0
dataset['Mystery'] = 0
dataset['Fantasy'] = 0
dataset['Family'] = 0
dataset['Comedy'] = 0
dataset['Crime'] = 0

count = 0
movie_names = dataset['movie_title']
movie_genres = dataset['genres']
for index in dataset.index:
    list_genre = dataset.loc[index, 'genres'].split("|")
    for ge in list_genre:
        if ge in dataset:
            dataset.loc[index, ge] = 1

dataset.drop('Horror', axis=1, inplace=True)

dataset.to_csv('output2.csv')

data = pd.read_csv("output.csv")

data['country'] = actor1encoder.fit_transform(data['country'])
