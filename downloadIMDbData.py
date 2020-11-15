# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from imdb import IMDb
from bs4 import BeautifulSoup as Soup
from requests import get
import pandas as pd
import collections

ia = IMDb()
main = ['Life of Pi (2012)', 'Spectre', 'The Dark Knight Rises ', 'John Carter', 'Spider-Man 3', 'Tangled',
        'Avengers: Age of Ultron', 'Harry Potter and the Half-Blood Prince', 'Batman v Superman: Dawn of Justice',
        'Superman Returns', 'Quantum of Solace', 'Pirates of the Caribbean: Dead Man\'s Chest', 'The Lone Ranger']

movie_list = ['Avatar ',
              "Pirates of the Caribbean: At World's End",
              'Spectre',
              'The Dark Knight Rises',
              'John Carter',
              'Spider-Man 3',
              'Tangled',
              'Avengers: Age of Ultron',
              'Harry Potter and the Half-Blood Prince',
              'Batman v Superman: Dawn of Justice',
              'Superman Returns',
              'Quantum of Solace',
              "Pirates of the Caribbean: Dead Man's Chest",
              'The Lone Ranger',
              'Man of Steel',
              'The Chronicles of Narnia: Prince Caspian',
              'The Avengers',
              'Pirates of the Caribbean: On Stranger Tides',
              'Men in Black 3',
              'The Hobbit: The Battle of the Five Armies',
              'The Amazing Spider-Man',
              'The Hobbit: The Desolation of Smaug',
              'The Golden Compass',
              'King Kong',
              'Titanic',
              'Captain America: Civil War',
              'Battleship',
              'Jurassic World',
              'Skyfall',
              'Spider-Man 2',
              'Iron Man 3',
              'Alice in Wonderland',
              'Transformers: Dark of the Moon',
              'Avatar',
              "Pirates of the Caribbean: At World's End",
              'Spectre',
              'The Dark Knight Rises',
              'John Carter',
              'Spider-Man 3',
              'Tangled',
              'Avengers: Age of Ultron',
              'Harry Potter and the Half-Blood Prince',
              'Batman v Superman: Dawn of Justice',
              'Superman Returns',
              'Quantum of Solace',
              "Pirates of the Caribbean: Dead Man's Chest",
              'The Lone Ranger',
              'Man of Steel',
              'The Chronicles of Narnia: Prince Caspian',
              'The Avengers',
              'Pirates of the Caribbean: On Stranger Tides',
              'Men in Black 3',
              'The Hobbit: The Battle of the Five Armies',
              'The Amazing Spider-Man',
              'The Hobbit: The Desolation of Smaug',
              'The Golden Compass',
              'King Kong',
              'Titanic',
              'Captain America: Civil War',
              'Battleship',
              'Jurassic World',
              'Skyfall',
              'Spider-Man 2',
              'Iron Man 3',
              'Alice in Wonderland',
              'X-Men: The Last Stand',
              'Monsters University',
              'Transformers: Revenge of the Fallen',
              'Transformers: Age of Extinction',
              'Oz the Great and Powerful',
              'The Amazing Spider-Man',
              'TRON: Legacy',
              'Cars 2',
              'Green Lantern',
              'Toy Story 3',
              'Terminator Salvation',
              'Furious 7',
              'World War Z',
              'X-Men: Days of Future Past',
              'Star Trek Into Darkness',
              'Jack the Giant Slayer',
              'The Great Gatsby',
              'Prince of Persia: The Sands of Time',
              'Pacific Rim',
              'Transformers: Dark of the Moon',
              'Indiana Jones and the Kingdom of the Crystal Skull']

movie_list = []

dataset = pd.read_csv('/home/nspython/Downloads/movie_metadata.csv')
dirc = dataset['director_name']
real_movie_data = dataset['movie_title'].astype(str)
real_movie_dir = dataset['director_name'].astype(str)
count = 0
for x in real_movie_data:
    movie = ia.search_movie(x)[0]
    movie_id = movie.movieID
    name = movie['title']
    movie = ia.get_movie(movie.movieID)
    dic = movie['directors'][0]['name']
    print(x + " " + dataset['director_name'][count] + " " + dic)
    if dic == dataset['director_name'][count]:
        movie_list.append(x)
    count = count + 1

Movie_Names = []
Movie_ratings = []
Movie_years = []
Movie_director = []
Movie_actor_1_name = []
Movie_actor_2_name = []
Movie_actor_3_name = []
Movie_director_credit = []
Movie_actor_1_credit = []
Movie_actor_2_credit = []
Movie_actor_3_credit = []

count = 0


def get_person_creadit(person_name):
    print(person_name)
    person = ia.search_person(person_name)[0]
    url = get("https://www.imdb.com/name/nm" + person.personID)
    request = url.text

    Soup_data = Soup(request, 'html.parser')

    creaits = Soup_data.findAll('div', {'class': 'filmo-row'})
    creaits_year = []
    for i in creaits:
        if i.span.text[2:6] != '\n':
            creaits_year.append(int(i.span.text[2:6]))

            ctr = collections.Counter(creaits_year)
    sum = 0
    for i in ctr:
        if i < movie_year:
            sum = sum + ctr[i]

    return sum


for movieName in movie_list:
    print(movieName)

    movie = ia.search_movie(movieName)[0]
    movie_id = movie.movieID
    movie = ia.get_movie(movie_id)
    # if(movie['directors']):
    #   movie_dic = movie['directors']
    movie_year = movie['year']
    # if(movie['cast']):
    #   movie_cast = movie['cast']
    Movie_rating = movie['rating']

    dataRow = dataset.loc[dataset['movie_title'].astype(str) == movieName]

    director_name = dataRow['director_name'].astype(str)[count]
    actor_1_name = dataRow['actor_1_name'].astype(str)[count]
    actor_2_name = dataRow['actor_2_name'].astype(str)[count]
    actor_3_name = dataRow['actor_3_name'].astype(str)[count]

    director_credit = get_person_creadit(director_name[count])
    actor_1_credit = get_person_creadit(actor_1_name[count])
    actor_2_credit = get_person_creadit(actor_2_name[count])
    actor_3_credit = get_person_creadit(actor_3_name[count])

    Movie_Names.append(movieName)  # append movie name
    Movie_years.append(movie_year)  # append movie year
    Movie_ratings.append(Movie_rating)  # append movie rating
    Movie_director.append(director_name)  # append movie directoer
    Movie_director_credit.append(director_credit)
    Movie_actor_1_name.append(actor_1_name)  # append movie casting
    Movie_actor_1_credit.append(actor_1_credit)
    Movie_actor_2_name.append(actor_2_name)  # append movie casting
    Movie_actor_2_credit.append(actor_2_credit)
    Movie_actor_3_name.append(actor_3_name)  # append movie casting
    Movie_actor_3_credit.append(actor_3_credit)
    count = count + 1

data = list(zip(Movie_Names, Movie_years, Movie_ratings, Movie_director, Movie_director_credit, Movie_actor_1_name,
                Movie_actor_1_credit, Movie_actor_2_name, Movie_actor_2_credit, Movie_actor_3_name,
                Movie_actor_3_credit))

df = pd.DataFrame(data,
                  columns=['Movie_Names', 'Movie_years', 'Movie_ratings', 'Movie_director', 'Movie_director_credit',
                           'Movie_actor_1_name', 'Movie_actor_1_credit', 'Movie_actor_2_name', 'Movie_actor_2_credit',
                           'Movie_actor_3_name', 'Movie_actor_3_credit'])

df.to_csv(index=False, path_or_buf='./output.csv')
# main.append({'name':'Life of Pi (2012)','year':movie_year, })


# edit create csv dataset marge
dataset_create = pd.read_csv('/home/nspython/Downloads/output.csv')
dataset_pro = pd.read_csv('/home/nspython/Downloads/imdbpro.csv')

new_dataset = pd.merge(dataset_create, dataset_pro, left_on='Movie_Names', right_on=('movie_name'), how=('left'))

new_dataset.to_csv(index=False, path_or_buf='./final.csv')
"""
Created on Fri Oct 23 19:41:27 2020

@author: nspiumal
"""
import pandas as pd

dataset = pd.read_csv('/home/nspiumal/Downloads/archive/movie_metadata.csv')
dataset = dataset.drop('Unnamed: 28', 1)
dataset = dataset.drop('color', 1)
dataset = dataset.drop('movie_imdb_link', 1)
clean_dataset = dataset.dropna(axis='index', how='any')
clean_dataset.to_csv('/home/nspiumal/Downloads/archive/movie_metadata1.csv')
