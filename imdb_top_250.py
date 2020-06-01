# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 04:05:27 2020

@author: User
"""
import requests 
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

min_rating = float(input("Please, enter min. rating value: "))

column = soup.find_all("td",{"class":"titleColumn"})
rating = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for col,rat in zip(column,rating):
    col = col.text
    rat = rat.text
    
    col = col.strip()
    rat = rat.strip()
    
    col = col.replace("\n","")
    rat = rat.replace("\n","")
    
    if (float(rat) > min_rating):
        print("Movie is {} and Rating is {}".format(col,rat))
    



