import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movies = []
for movie in all_movies:
    movies.append(movie.getText())
movies.reverse()
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

# Write your code below this line 👇


