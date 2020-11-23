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

print (df)

df.to_csv('new.csv')
