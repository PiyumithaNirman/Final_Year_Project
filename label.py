import pandas as pd

df = pd.read_csv('Final IMDb Lebel set - Sheet1.csv')
df.head()
print (df)

# format_df = list(np.around(np.array(df['value']), 1))
format_df = df['Movie_ratings']

# format_df = df['imdb_score']

print format_df


def label_race(format_df):
    for x in format_df:

        if x <= 5:
            return 'CLASS-1'
        if 5 < x <= 6.5:
            return 'CLASS-2'
        if 6.5 < x <= 7.5:
            return 'CLASS-3'
        if 7.5 < x <= 10:
            return 'CLASS-4'


# if 2 > x :
#     return 'BLOCKBUSTER'


df.apply(lambda row: label_race(row), axis=1)

df['IMDb_Label'] = df.apply(lambda row: label_race(row), axis=1)

print (df.__len__())
print df
df.to_csv(index=False, path_or_buf='./final.csv')
# display updated DataFrame
df.head()
