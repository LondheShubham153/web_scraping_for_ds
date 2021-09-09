from bs4 import BeautifulSoup
import requests
import pandas as pd

# step 1 get the raw html data

url = "https://www.imdb.com/chart/top"

res = requests.get(url=url)

# step 2 parse data by beautifulSoup

soup = BeautifulSoup(res.text, features="html.parser")

all_tr = soup.findChildren("tr")

# creating data structures
title_list = []
year_list = []
rating_list = []

movie_data = {}

# step 3 get movie title inside TR Table row and Td Table data
for movie in all_tr:
    try:
        title_list.append(movie.find("td",{"class":"titleColumn"}).find("a").contents[0])
        year_list.append(movie.find("td",{"class":"titleColumn"}).find("span",{"class":"secondaryInfo"}).contents[0])
        rating_list.append(movie.find("td",{"class":"ratingColumn imdbRating"}).find("strong").contents[0])
    except:
        continue

#step 4 organise the data to data structures list and dictionaries

movie_data["title"] = title_list
movie_data["year"] = year_list
movie_data["rating"] = rating_list

#step 5 create a dataframe using pandas
df = pd.DataFrame(movie_data)

#step 6 create a csv or excel file

print("populating csv file")
df.to_csv("top_movies.csv")

print("populating excel file")
df.to_excel("top_movies.xlsx", engine='openpyxl')
