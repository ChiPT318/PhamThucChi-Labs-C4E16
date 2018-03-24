from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

html = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html, "html.parser")
div = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
# print(div.prettify())

tr_list = div.find_all("tr", {"class": ["r_item ", "r_item_a"]})
# print(tr_list)
datas = []
for tr in tr_list:
    data = {}
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        titles = ["Title", "quy 1", "quy 2", "quy 3", "quy 4", "tang truong"]
        for title in titles:
            if td_list.index(td) == titles.index(title):
                data[title] = td.string
            else:
                continue
    datas.append(data)


print(datas)
pyexcel.save_as(records=datas, dest_file_name="Cafefin.xls")
