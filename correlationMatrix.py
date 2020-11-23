import pandas as pd

df = pd.read_csv('Label_Set_Finance -Correlation.csv')
dft = pd.DataFrame(df, columns=['Movie_actor_3_credit', 'Director_Other_Awards',
                                'Movie_ratings'])

print(dft.describe())
corrMatrix = dft.corr() * 100
print (corrMatrix)

corrMatrix.to_csv('fsada.csv')
