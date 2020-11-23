#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:53:29 2020

@author: nspython
"""

from imdb import IMDb
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import collections
import re

ia = IMDb()

Movie_Names = []
Movie_actor_1_name = []
Movie_actor_2_name = []
Movie_actor_3_name = []
Movie_director = []
Movie_writter_names = []
Movie_music_names = []
Movie_cinematography_name = []
Movie_costume_name = []
Movie_years = []
Movie_ratings = []
Movie_director_credit = []
Movie_actor_1_credit = []
Movie_actor_3_credit = []
Movie_actor_2_credit = []
Movie_writter_credit = []
Movie_music_credit = []
Movie_cinematography_credit = []
Movie_costume_credit = []
Movie_actor_1_awords = []
Movie_actor_2_awords = []
Movie_actor_3_awords = []
Movie_director_awords = []
Movie_writter_awords = []
Movie_music_awords = []
Movie_cinematography_aword = []
Movie_costume_aword = []
count = 0

movie_list = ['Spider-Man 3']


def get_person_aword(person_name):
    try:
        print(person_name)
        person = ia.search_person(person_name)[0]
        url = get("https://www.imdb.com/name/nm" + person.personID)
        request = url.text
        Soup_data = BeautifulSoup(request, 'html.parser')
        numbers = []
        aword_text = ''
        for word in Soup_data.findAll('span', {'class': 'awards-blurb'}):
            aword_text = aword_text + word.text
        # aword_text0 = Soup_data.findAll('span',{'class':'awards-blurb'})[0].text
        # aword_text1 = Soup_data.findAll('span',{'class':'awards-blurb'})[1].text
        # aword_text = aword_text0# + aword_text1
        return aword_text
    except IndexError:
        aword_text = 'null'
    finally:
        return aword_text


def get_person_creadit(person_name, name):
    print(name, " ", person_name)
    person = ia.search_person(person_name)[0]
    url = get("https://www.imdb.com/name/nm" + person.personID)
    request = url.text

    Soup_data = BeautifulSoup(request, 'html.parser')
    creaits = Soup_data.findAll('div', {'id': re.compile(name + "-tt*")})
    creaits_year = []
    for i in creaits:
        if (i.span.text[2:6] != '\n'):
            creaits_year.append(int(i.span.text[2:6]))

    ctr = collections.Counter(creaits_year)
    sum = 0
    for i in ctr:
        if (i < movie_year):
            sum = sum + ctr[i]

    return sum


def getmovieactor(movieId):
    print(movieId)
    actor_name_1 = ''
    actor_name_2 = ''
    actor_name_3 = ''
    direction_name = ''
    writter_name = ''
    music_name = ''
    cinematography_name = ''

    writter_credit = 0
    director_credit = 0
    actor_1_credit = 0
    actor_2_credit = 0
    actor_3_credit = 0
    music_credit = 0
    cinematography_credit = 0
    # url = "https://www.imdb.com/title/tt{movieId}/fullcredits"
    page = get("https://www.imdb.com/title/tt{movieId}/fullcredits")
    soup = BeautifulSoup(page.content, 'lxml')
    pattern = []
    # cast
    cast = soup.find_all('table', {'class': 'cast_list'})
    print(cast)
    allcast1 = cast[0].findAll('td', {'class': 'character'})
    allcast2 = cast[0].findAll('td', {'class': 'ellipsis'})
    allcast3 = cast[0].findAll('td', {'class': 'primary_photo'})
    allcast = cast[0].findAll('td')
    for x in allcast1:
        allcast.remove(x)
    for x in allcast2:
        allcast.remove(x)
    for x in allcast3:
        allcast.remove(x)
    print(allcast)
    actor_1_name = allcast[1].text.strip()
    actor_1_credit = get_person_creadit(actor_1_name, 'actor')
    actor_1_aword = get_person_aword(actor_1_name)
    print(actor_1_name, " ", actor_1_credit)

    actor_2_name = allcast[2].text.strip()
    actor_2_credit = get_person_creadit(actor_2_name, 'actor')
    actor_2_aword = get_person_aword(actor_2_name)
    print(actor_2_name, " ", actor_2_credit)

    actor_3_name = allcast[3].text.strip()
    actor_3_credit = get_person_creadit(actor_3_name, 'actor')
    actor_3_aword = get_person_aword(actor_3_name)
    print(actor_3_name, " ", actor_3_credit)

    crew = soup.find_all('table', class_='simpleTable simpleCreditsTable')

    # director
    director = crew[0].find_all('a')
    director_name = director[0].text.strip()
    director_credit = get_person_creadit(director_name, 'director')
    director_aword = get_person_aword(director_name)
    print(direction_name, " ", director_credit)

    # writing
    writing = crew[1].find_all('a')
    writter_name = writing[0].text.strip()
    writter_credit = get_person_creadit(writter_name, 'writer')
    writter_aword = get_person_aword(writter_name)
    print(writter_name, " ", writter_credit)

    # music
    music = crew[3].find_all('a')
    music_name = music[0].text.strip()
    music_credit = get_person_creadit(music_name, 'music_department')
    music_aword = get_person_aword(music_name)
    print(music_name, " ", music_credit)

    # cinematography
    cinematography = crew[4].find_all('a')
    cinematography_name = cinematography[0].text.strip()
    cinematography_credit = get_person_creadit(cinematography_name, 'cinematographer')
    cinematography_aword = get_person_aword(cinematography_name)
    print(cinematography_name, " ", cinematography_credit)

    # Costume
    costume = crew[10].find_all('a')
    costume_name = costume[0].text.strip()
    costume_credit = get_person_creadit(costume_name, 'costume_designer')
    costume_aword = get_person_aword(costume_name)
    print(costume_name, " ", costume_credit)

    return director_name, actor_1_name, actor_2_name, actor_3_name, writter_name, music_name, cinematography_name, costume_name, director_credit, actor_1_credit, actor_2_credit, actor_3_credit, writter_credit, music_credit, cinematography_credit, costume_credit, actor_1_aword, actor_2_aword, actor_3_aword, director_aword, writter_aword, music_aword, cinematography_aword, costume_aword


# add movie detail without aword
for movieName in movie_list:
    print(movieName)

    movie = ia.search_movie(movieName)[0]
    movie_id = movie.movieID
    movie = ia.get_movie(movie_id)
    movie_year = movie['year']
    Movie_rating = movie['rating']

    director_name, actor_1_name, actor_2_name, actor_3_name, writter_name, music_name, cinematography_name, costume_name, director_credit, actor_1_credit, actor_2_credit, actor_3_credit, writter_credit, music_credit, cinematography_credit, costume_credit, actor_1_aword, actor_2_aword, actor_3_aword, director_aword, writter_aword, music_aword, cinematography_aword, costume_aword = getmovieactor(
        movie_id)

    Movie_Names.append(movieName)  # append movie name
    Movie_years.append(movie_year)  # append movie year
    Movie_ratings.append(Movie_rating)  # append movie rating
    Movie_director.append(director_name)  # append movie directoer
    Movie_director_credit.append(director_credit)
    Movie_director_awords.append(director_aword)
    Movie_actor_1_name.append(actor_1_name)  # append movie casting
    Movie_actor_1_credit.append(actor_1_credit)
    Movie_actor_1_awords.append(actor_1_aword)
    Movie_actor_2_name.append(actor_2_name)  # append movie casting
    Movie_actor_2_credit.append(actor_2_credit)
    Movie_actor_2_awords.append(actor_2_aword)
    Movie_actor_3_name.append(actor_3_name)  # append movie casting
    Movie_actor_3_credit.append(actor_3_credit)
    Movie_actor_3_awords.append(actor_3_aword)
    Movie_writter_names.append(writter_name)  # append movie directoer
    Movie_writter_credit.append(writter_credit)
    Movie_writter_awords.append(writter_aword)
    Movie_music_names.append(music_name)
    Movie_music_credit.append(music_credit)
    Movie_music_awords.append(music_aword)
    Movie_costume_name.append(costume_name)
    Movie_costume_credit.append(costume_credit)
    Movie_costume_aword.append(costume_aword)
    Movie_cinematography_name.append(cinematography_name)
    Movie_cinematography_credit.append(cinematography_credit)
    Movie_cinematography_aword.append(cinematography_aword)

    count = count + 1

data = list(zip(Movie_Names, Movie_years, Movie_ratings, Movie_director, Movie_director_credit, Movie_director_awords,
                Movie_actor_1_name, Movie_actor_1_credit, Movie_actor_1_awords, Movie_actor_2_name,
                Movie_actor_2_credit, Movie_actor_2_awords, Movie_actor_3_name, Movie_actor_3_credit,
                Movie_actor_3_awords, Movie_music_names, Movie_music_credit, Movie_music_awords, Movie_writter_names,
                Movie_writter_credit, Movie_writter_awords, Movie_cinematography_name, Movie_cinematography_credit,
                Movie_cinematography_aword, Movie_costume_name, Movie_costume_credit, ))

df = pd.DataFrame(data,
                  columns=['Movie_Names', 'Movie_years', 'Movie_ratings', 'Movie_director', 'Movie_director_credit',
                           'Movie_director_awords', 'Movie_actor_1_name', 'Movie_actor_1_credit',
                           'Movie_actor_1_awords ', 'Movie_actor_2_name', 'Movie_actor_2_credit',
                           'Movie_actor_1_awords ', 'Movie_actor_3_name', 'Movie_actor_3_credit',
                           'Movie_actor_3_awords', 'Movie_music_names', 'Movie_music_credit', 'Movie_music_awords ',
                           'Movie_writter_names', 'Movie_writter_credit', 'Movie_writter_awords',
                           'Movie_cinematography_name', 'Movie_cinematography_credit', 'Movie_cinematography_aword',
                           'Movie_costume_name', 'Movie_costume_credit', ])

df.to_csv(index=False, path_or_buf='./output7.csv')

















