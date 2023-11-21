import requests
from bs4 import BeautifulSoup


empire100 = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(empire100, "html.parser")
movieList = []


article = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
for i in article:
    movieList.append(i.text)

newList = movieList[::-1]


for j in newList:
    with open("movie.txt", "a") as file:
        content = file.write(f"{j}\n")


