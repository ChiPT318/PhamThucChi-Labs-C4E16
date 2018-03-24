#steps to strip data:
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"

    # 1. download webpage
html = urlopen(url).read().decode('utf-8')
# print(html)

    # Save html link
import urllib.request
urllib.request.urlretrieve(url, "test.html")
            # or
# html_file = open("dantri.html", "wb") #wb opens file in binary mode, w only opens string modes
# html_file.write(html)
# html_file.close

    # 2. Extract ROI - reason of interest
soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

ul = soup.find("ul","ul1 ulnew") #viet nhu nay chi cho attribute class
# print(ul.prettify())


    # 3. Extract info
li_list = ul.find_all("li")
datas = []

for li in li_list:
    data = {}
    a = li.h4.a
    # print(url + a["href"])
    # print(a.string)
    # print("*"*34)
    data["title"] = a.string
    data["link"] = url + a["href"]
    datas.append(data)

print(datas)
pyexcel.save_as(records=datas, dest_file_name="Dantridata.xls")

for li in li_list:
    print(li.prettify)
    print("*"*34)
