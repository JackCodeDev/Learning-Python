import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_web = response.text
soup = BeautifulSoup(movie_web, "html.parser")
movie_title = [title.getText() for title in soup.find_all(name="h3", class_="title")][::-1]
print(movie_title)
with open("movie.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_title:
        file.write(f"{movie}\n")

