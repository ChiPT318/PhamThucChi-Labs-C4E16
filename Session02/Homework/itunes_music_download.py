from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"

html = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
ul = soup.find("ul","")
# print(ul.prettify())

li_list = ul.find_all("li")

datas = []
for li in li_list:
    a = li.h3.a
    song = a.string
    datas.append(song)

options = {
"default_search" : "ytsearch",

}

dl = YoutubeDL(options)
dl.download(datas)
