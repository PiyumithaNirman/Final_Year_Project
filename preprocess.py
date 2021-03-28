import pandas as pd

# READ THE DATA FILES
from sklearn.preprocessing import LabelEncoder

csv_file = open('Final IMDb Data.csv')
df = pd.read_csv(csv_file)

df = df.drop_duplicates()

df['Screen_Count'] = df['Screen_Count'].fillna(
    df.groupby('Movie_Title')['Screen_Count'].transform('mean'))
df['Screen_Count'] = df['Screen_Count'].fillna(df['Screen_Count'].mean())
df['Screen_Count'] = df['Screen_Count'].round()

df['Aspect_Ratio'] = df['Aspect_Ratio'].fillna(
    df.groupby('Movie_Title')['Aspect_Ratio'].transform('mean'))
df['Aspect_Ratio'] = df['Aspect_Ratio'].fillna(df['Aspect_Ratio'].mean())

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
