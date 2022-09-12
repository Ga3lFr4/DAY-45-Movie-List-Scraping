import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, 'lxml')

names_of_movies = soup.find_all(name="h3", class_="title")

movie_list = []

for movie in names_of_movies:
    movie_title = movie.getText()
    movie_list.append(movie_title)

with open("movies.txt", "a", encoding="utf-8") as file:
    for _ in range(len(movie_list)):
        file.write(movie_list[-1] + "\n")
        movie_list.pop()



