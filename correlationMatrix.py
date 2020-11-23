from Tkinter import Image

import pandas as pd
from pandas.tests.sparse.frame.test_to_from_scipy import scipy

df = pd.read_csv('new.csv')
dft = pd.DataFrame(df, columns=['Movie_Title', 'Movie_years', 'Content_Ratio', 'Aspect_Ratio', 'Movie_actor_1_credit',
                                'Actor_1_Oscar_Awards', 'Actor_1_Other_Awards', 'Movie_actor_2_credit',
                                'Actor_2_Oscar_Awards', 'Actor_2_Other_Awards', 'Movie_actor_3_credit',
                                'Actor_3_Oscar_Awards', 'Actor_3_Other_Awards', 'Movie_director_credit',
                                'Director_Oscar_Awards', 'Director_Other_Awards', 'Movie_writter_credit',
                                'Movie_Writter_Oscar_Awards', 'Music_Writter_Other_Awards', 'Movie_music_credit',
                                'Music_Oscar_Awards', 'Music_Other_Awards', 'Movie_cinematography_credit',
                                'Cinematograpy_Oscar_Awards', 'Cinematograpy_Other_Awards', 'Budget', 'Movie_ratings'
                                ])

print(dft.describe())
corrMatrix = dft.corr() * 100
print (corrMatrix)

corrMatrix.to_csv('fsada.csv')
scipy.misc.imsave('outfile.jpg', corrMatrix)