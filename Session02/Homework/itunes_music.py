from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"

html = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
ul = soup.find("ul","")
# print(ul.prettify())

li_list = ul.find_all("li")

datas = []
for li in li_list:
    data = {}
    a = li.h4.a
    data["Artist"] = a.string
    b = li.h3.a
    data["Songs"] = b.string

    datas.append(data)
print(datas)
pyexcel.save_as(records=datas, dest_file_name="TopItunes.xls")
