# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14lDv-dHYAuba4hu6SgMMGaXe9Y8hB7dC
"""

pip install imdbpy

pip install bs4

pip install pandas

pip install requests

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
Movie_actor_1_awords_Oscars = []
Movie_actor_2_awords_Oscars = []
Movie_actor_3_awords_Oscars = []
Movie_director_awords_Oscars = []
Movie_writter_awords_Oscars = []
Movie_music_awords_Oscars = []
Movie_cinematography_aword_Oscars = []
Movie_costume_aword_Oscars = []
Movie_actor_1_awords_win = []
Movie_actor_2_awords_win = []
Movie_actor_3_awords_win = []
Movie_director_awords_win = []
Movie_writter_awords_wins = []
Movie_music_awords_win = []
Movie_cinematography_aword_win = []
Movie_costume_aword_win = []
Movie_actor_1_awords_nominations = []
Movie_actor_2_awords_nominations = []
Movie_actor_3_awords_nominations = []
Movie_director_awords_nominations = []
Movie_writter_awords_nominations = []
Movie_music_awords_nominations = []
Movie_cinematography_aword_nominations = []
Movie_costume_aword_nominations = []
count = 0

movie_list = ['Coraline',
              'Year One',
              'Invictus']

def get_person_creadit(person_name,name):
    print(name , " ", person_name)
    person = ia.search_person(person_name)[0]
    url = get("https://www.imdb.com/name/nm"+person.personID)
    request = url.text
    
    
    Soup_data = BeautifulSoup(request,'html.parser')
    creaits = Soup_data.findAll('div',{'id':re.compile(name+"-tt*")})
    creaits_year = []
    for i in creaits:
        if(i.span.text[2:6] != '\n'):
            creaits_year.append(int(i.span.text[2:6]))
        
    
    ctr = collections.Counter(creaits_year)
    sum = 0
    for i in ctr:
        if( i < movie_year):
            sum = sum + ctr[i]
    
    return sum

def get_person_aword(person_name):

  Oscars = 0
  win = 0
  nominations = 0
  try:
      print(person_name)
      person = ia.search_person(person_name)[0]
      url = get("https://www.imdb.com/name/nm"+person.personID)
      request = url.text
      Soup_data = BeautifulSoup(request,'html.parser')
      numbers = []
      aword_text = Soup_data.findAll('span',{'class':'awards-blurb'})
      if ( 2 > len(aword_text)):
        aword_text0 = Soup_data.findAll('span',{'class':'awards-blurb'})[0].text
        res = [int(i) for i in aword_text0.split() if i.isdigit()]
        print("res",res)
        if(len(res) == 1):
          nominations= res[0]
        else:
          win = res[0]
          nominations= res[1]
      if ( 2 == len(aword_text)):
        aword_text0 = Soup_data.findAll('span',{'class':'awards-blurb'})[0].text
        res0 = [int(i) for i in aword_text0.split() if i.isdigit()]
        print("res0",res0)
        Oscars = res0[0]
        aword_text1 = Soup_data.findAll('span',{'class':'awards-blurb'})[1].text
        res1 = [int(i) for i in aword_text1.split() if i.isdigit()]
        print("res1",res1)
        if(len(res1) == 1):
          nominations= res1[0]
        else:
          win = res1[0]
          nominations= res1[1]
      #aword_text = aword_text0# + aword_text1
      return Oscars,win,nominations
  except IndexError:
      aword_text = Oscars,win,nominations
  finally:
      return Oscars,win,nominations

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
    url= F"https://www.imdb.com/title/tt{movieId}/fullcredits/?ref_=tt_ov_st_sm"
    page = get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    pattern=[]
    #cast
    cast =soup.find_all('table', {'class' : 'cast_list'})
    allcast1 = cast[0].findAll('td' , {'class' : 'character'})
    allcast2 = cast[0].findAll('td' , {'class' : 'ellipsis'})
    allcast3 = cast[0].findAll('td' , {'class' : 'primary_photo'})
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
    actor_1_aword_Oscar,actor_1_aword_win,actor_1_aword_nominations = get_person_aword(actor_1_name)
    print(actor_1_name, " ",actor_1_credit)
    
    actor_2_name = allcast[2].text.strip()
    actor_2_credit = get_person_creadit(actor_2_name, 'actor')
    actor_2_aword_Oscar,actor_2_aword_win,actor_2_aword_nominations = get_person_aword(actor_2_name)
    print(actor_2_name, " ",actor_2_credit)
    
    actor_3_name = allcast[3].text.strip()
    actor_3_credit = get_person_creadit(actor_3_name, 'actor')
    actor_3_aword_Oscar,actor_3_aword_win,actor_3_aword_nominations = get_person_aword(actor_3_name)
    print(actor_3_name, " ",actor_3_credit)
    
    
    crew =soup.find_all('table', class_='simpleTable simpleCreditsTable')
    
    #director
    director = crew[0].find_all('a')
    director_name = director[0].text.strip()
    director_credit = get_person_creadit(director_name, 'director')
    director_aword_Oscar, director_aword_win, director_aword_nominations = get_person_aword(director_name)
    print(direction_name, " ",director_credit)
            
    #writing
    writing = crew[1].find_all('a')
    writter_name = writing[0].text.strip()
    writter_credit = get_person_creadit(writter_name,'writer')
    writter_aword_Oscar, writter_aword_win, writter_aword_nominations = get_person_aword(writter_name)
    print(writter_name, " ",writter_credit)
    
    #music 
    music = crew[3].find_all('a')
    music_name = music[0].text.strip()
    music_credit = get_person_creadit(music_name, 'music_department')
    music_aword_Oscar, music_aword_win, music_aword_nominations = get_person_aword(music_name)
    print(music_name, " ",music_credit)
    
    #cinematography 
    cinematography = crew[4].find_all('a')
    cinematography_name = cinematography[0].text.strip()
    cinematography_credit = get_person_creadit(cinematography_name, 'cinematographer')
    cinematography_aword_Oscar, cinematography_aword_win, cinematography_aword_nominations = get_person_aword(cinematography_name)
    print(cinematography_name, " ",cinematography_credit)
    
    #Costume 
    costume = crew[10].find_all('a')
    costume_name = costume[0].text.strip()
    costume_credit = get_person_creadit(costume_name, 'costume_designer')
    costume_aword_Oscar, costume_aword_win, costume_aword_nominations = get_person_aword(costume_name)
    print(costume_name, " ",costume_credit)
    
    return director_name, actor_1_name, actor_2_name, actor_3_name, writter_name, music_name, cinematography_name, costume_name, director_credit, actor_1_credit, actor_2_credit, actor_3_credit, writter_credit, music_credit, cinematography_credit, costume_credit, actor_1_aword_Oscar, actor_2_aword_Oscar, actor_3_aword_Oscar, director_aword_Oscar, writter_aword_Oscar, music_aword_Oscar, cinematography_aword_Oscar, costume_aword_Oscar, actor_1_aword_win, actor_2_aword_win, actor_3_aword_win, director_aword_win, writter_aword_win, music_aword_win, cinematography_aword_win, costume_aword_win, actor_1_aword_nominations, actor_2_aword_nominations, actor_3_aword_nominations, director_aword_nominations, writter_aword_nominations, music_aword_nominations, cinematography_aword_nominations, costume_aword_nominations

#add movie detail without aword 
for movieName in movie_list:
    print(movieName)

    movie = ia.search_movie(movieName)[0]
    movie_id = movie.movieID
    print(movie_id)
    movie = ia.get_movie(movie_id)
    movie_year = movie['year']
    Movie_rating = movie['rating']
    
    director_name, actor_1_name, actor_2_name, actor_3_name, writter_name, music_name, cinematography_name, costume_name, director_credit, actor_1_credit, actor_2_credit, actor_3_credit, writter_credit, music_credit, cinematography_credit, costume_credit , actor_1_aword_Oscar, actor_2_aword_Oscar, actor_3_aword_Oscar, director_aword_Oscar, writter_aword_Oscar, music_aword_Oscar, cinematography_aword_Oscar, costume_aword_Oscar, actor_1_aword_win, actor_2_aword_win, actor_3_aword_win, director_aword_win, writter_aword_win, music_aword_win, cinematography_aword_win, costume_aword_win, actor_1_aword_nominations, actor_2_aword_nominations, actor_3_aword_nominations, director_aword_nominations, writter_aword_nominations, music_aword_nominations, cinematography_aword_nominations, costume_aword_nominations = getmovieactor(movie_id)
      
    Movie_Names.append(movieName) #append movie name
    Movie_years.append(movie_year)#append movie year
    Movie_ratings.append(Movie_rating)#append movie rating
    Movie_director.append(director_name)#append movie directoer
    Movie_director_credit.append(director_credit)
    Movie_director_awords_Oscars.append(director_aword_Oscar)
    Movie_director_awords_win.append(director_aword_win)
    Movie_director_awords_nominations.append(director_aword_nominations)
    Movie_actor_1_name.append(actor_1_name)#append movie casting
    Movie_actor_1_credit.append(actor_1_credit)
    Movie_actor_1_awords_Oscars.append(actor_1_aword_Oscar)
    Movie_actor_1_awords_win.append(actor_1_aword_win)
    Movie_actor_1_awords_nominations.append(actor_1_aword_nominations)
    Movie_actor_2_name.append(actor_2_name)#append movie casting
    Movie_actor_2_credit.append(actor_2_credit)
    Movie_actor_2_awords_Oscars.append(actor_2_aword_Oscar)
    Movie_actor_2_awords_win.append(actor_2_aword_win)
    Movie_actor_2_awords_nominations.append(actor_2_aword_nominations)
    Movie_actor_3_name.append(actor_3_name)#append movie casting
    Movie_actor_3_credit.append(actor_3_credit)
    Movie_actor_3_awords_Oscars.append(actor_3_aword_Oscar)
    Movie_actor_3_awords_win.append(actor_3_aword_win)
    Movie_actor_3_awords_nominations.append(actor_3_aword_Oscar)
    Movie_writter_names.append(writter_name)#append movie directoer
    Movie_writter_credit.append(writter_credit)
    Movie_writter_awords_Oscars.append(writter_aword_Oscar)
    Movie_writter_awords_wins.append(writter_aword_win)
    Movie_writter_awords_nominations.append(writter_aword_nominations)
    Movie_music_names.append(music_name)
    Movie_music_credit.append(music_credit)
    Movie_music_awords_Oscars.append(music_aword_Oscar)
    Movie_music_awords_win.append(music_aword_win)
    Movie_music_awords_nominations.append(music_aword_nominations)
    Movie_costume_name.append(costume_name)
    Movie_costume_credit.append(costume_credit)
    Movie_costume_aword_Oscars.append(costume_aword_Oscar)
    Movie_costume_aword_win.append(costume_aword_win)
    Movie_costume_aword_nominations.append(costume_aword_nominations)
    Movie_cinematography_name.append(cinematography_name)
    Movie_cinematography_credit.append(cinematography_credit)
    Movie_cinematography_aword_Oscars.append(cinematography_aword_Oscar)
    Movie_cinematography_aword_win.append(cinematography_aword_win)
    Movie_cinematography_aword_nominations.append(cinematography_aword_nominations)

    
    count = count + 1

data = list(zip(Movie_Names,Movie_years, Movie_ratings, Movie_director, Movie_director_credit, Movie_director_awords_Oscars, Movie_director_awords_win, Movie_director_awords_nominations, Movie_actor_1_name, Movie_actor_1_credit, Movie_actor_1_awords_Oscars, Movie_actor_1_awords_win , Movie_actor_1_awords_nominations , Movie_actor_2_name, Movie_actor_2_credit, Movie_actor_2_awords_Oscars , Movie_actor_2_awords_win , Movie_actor_2_awords_nominations ,  Movie_actor_3_name, Movie_actor_3_credit, Movie_actor_3_awords_Oscars , Movie_actor_3_awords_win , Movie_actor_3_awords_nominations , Movie_music_names, Movie_music_credit, Movie_music_awords_Oscars , Movie_music_awords_win , Movie_music_awords_nominations , Movie_writter_names, Movie_writter_credit, Movie_writter_awords_Oscars , Movie_writter_awords_wins , Movie_writter_awords_nominations ,Movie_cinematography_name, Movie_cinematography_credit, Movie_cinematography_aword_Oscars , Movie_cinematography_aword_win , Movie_cinematography_aword_nominations , Movie_costume_name,Movie_costume_credit,Movie_costume_aword_Oscars, Movie_costume_aword_win, Movie_costume_aword_nominations))
    
df = pd.DataFrame(data, columns=['Movie_Names', 'Movie_years', 'Movie_ratings', 'Movie_director', 'Movie_director_credit', 'Movie_director_awords_Oscars', 'Movie_director_awords_win', 'Movie_director_awords_nominations', 'Movie_actor_1_name', 'Movie_actor_1_credit',  'Movie_actor_1_awords_Oscars', 'Movie_actor_1_awords_win' , 'Movie_actor_1_awords_nominations' , 'Movie_actor_2_name', 'Movie_actor_2_credit', 'Movie_actor_2_awords_Oscars' , 'Movie_actor_2_awords_win' , 'Movie_actor_2_awords_nominations' , 'Movie_actor_3_name', 'Movie_actor_3_credit', 'Movie_actor_3_awords_Oscars' , 'Movie_actor_3_awords_win' , 'Movie_actor_3_awords_nominations' , 'Movie_music_names', 'Movie_music_credit', 'Movie_music_awords_Oscars' , 'Movie_music_awords_win' , 'Movie_music_awords_nominations' , 'Movie_writter_names', 'Movie_writter_credit', 'Movie_writter_awords_Oscars' , 'Movie_writter_awords_wins' , 'Movie_writter_awords_nominations' , 'Movie_cinematography_name', 'Movie_cinematography_credit', 'Movie_cinematography_aword_Oscars' , 'Movie_cinematography_aword_win' , 'Movie_cinematography_aword_nominations' , 'Movie_costume_name','Movie_costume_credit', 'Movie_costume_aword_Oscars', 'Movie_costume_aword_win', 'Movie_costume_aword_nominations' ])
      

df.to_csv(index=False, path_or_buf='../../Downloads/output7.csv')