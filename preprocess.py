import pandas as pd
import csv

# READ THE DATA FILES
from sklearn.preprocessing import LabelEncoder

csv_file = open('Final IMDb Lebel set - Sheet1.csv')
df = pd.read_csv(csv_file)

df['Movie_actor_1_credit'] = df['Movie_actor_1_credit'].fillna(
    df.groupby('Aspect_Ratio')['Movie_actor_1_credit'].transform('mean'))
df['Movie_actor_1_credit'] = df['Movie_actor_1_credit'].fillna(df['Movie_actor_1_credit'].mean())

df['Budget'] = df['Budget'].replace('[\$,]', '', regex=True).astype(float)

Content_Ratio = LabelEncoder()
df['Content_Ratio'] = Content_Ratio.fit_transform(df['Content_Ratio'])


def label_race(x):
    if x <= 5:
        return 'CLASS-1'
    if 5 < x <= 6.5:
        return 'CLASS-2'
    if 6.5 < x <= 7.5:
        return 'CLASS-3'
    if 7.5 < x <= 10:
        return 'CLASS-4'


count = 0
movie_genres = df['Movie_ratings']
for index in df.index:
    Movie_ratings = df.loc[index, 'Movie_ratings']
    print(Movie_ratings)
    df.loc[index, "IMDb_Label"] = label_race(Movie_ratings)

print (df)

df.to_csv('new.csv')
df.