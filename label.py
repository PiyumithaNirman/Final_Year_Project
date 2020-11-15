import csv
from datetime import time

import pandas as pd
import numpy as np

df = pd.read_csv('Budget-Revenue - Sheet1.csv')
df.head()
print (df)

# format_df = list(np.around(np.array(df['value']), 1))
# format_df = df['race_label']
format_df = df['Finance_Label']

# format_df = df['imdb_score']

print format_df


def label_race(format_df):
    for x in format_df:

        if x < 1:
            return 'FLOP'
        if 1 <= x <= 1.25:
            return 'HIT'
        if 1.25 < x < 1.75:
            return 'AVERAGE'
        if 1.75 <= x < 2.0:
            return 'SUPER_HIT'


# def label_race(format_df):
#     for x in format_df:
#
#         if x <= 5:
#             return 'CLASS-1'
#         if 5 < x <= 6.5:
#             return 'CLASS-2'
#         if 6.5 < x <= 7.5:
#             return 'CLASS-3'
#         if 7.5 < x <= 10:
#             return 'CLASS-4'
#

# if 2 > x :
#     return 'BLOCKBUSTER'


df.apply(lambda row: label_race(row), axis=1)

df['IMDb_Label'] = df.apply(lambda row: label_race(row), axis=1)

print (df.__len__())
print df
df.to_csv(index=False, path_or_buf='./final.csv')
# display updated DataFrame
df.head()
