import pandas as pd

df = pd.read_csv('Label_With_Finace_Rate.csv')
dft = pd.DataFrame(df, columns=['Distributor', 'Theaters', 'Movie_Gross', 'Movie_years', 'Movie_budget',
                                'Movie_aspect_ratio',
                                'Movie_runtime', 'Movie_ratings', 'Movie_director',
                                'Movie_director_credit', 'Movie_director_awords_Oscars', 'Movie_director_awords_win',
                                'Movie_director_awords_nominations', 'Movie_actor_1_name', 'Movie_actor_1_credit',
                                'Movie_actor_1_awords_Oscars', 'Movie_actor_1_awords_win', 'Movie_actor_1_awords_nominations',
                                'Movie_actor_2_name', 'Movie_actor_2_credit', 'Movie_actor_2_awords_Oscars',
                                'Movie_actor_2_awords_win', 'Movie_actor_2_awords_nominations', 'Movie_actor_3_name',
                                'Movie_actor_3_credit', 'Movie_actor_3_awords_Oscars', 'Movie_actor_3_awords_win',
                                'Movie_actor_3_awords_nominations', 'Movie_music_names',
                                'Movie_music_credit', 'Movie_music_awords_Oscars', 'Movie_music_awords_win',
                                'Movie_music_awords_nominations', 'Movie_writter_names', 'Movie_writter_credit',
                                'Movie_writter_awords_Oscars', 'Movie_writter_awords_wins', 'Movie_writter_awords_nominations',
                                'Movie_cinematography_name', 'Movie_cinematography_credit', 'Movie_cinematography_aword_Oscars',
                                'Movie_cinematography_aword_win', 'Movie_cinematography_aword_nominations',
                                'Movie_costume_name', 'Movie_costume_credit', 'Movie_costume_aword_Oscars',
                                'Movie_costume_aword_win', 'Movie_costume_aword_nominations'
                                ])


print(dft.describe())
corrMatrix = dft.corr() * 100
print (corrMatrix)

corrMatrix.to_csv('fsada.csv')
