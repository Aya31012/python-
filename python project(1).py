import requests
from bs4 import BeautifulSoup as bs
import csv
from itertools import zip_longest

Name = []
Price = []

url = requests.get("https://ar.shein.com/Toddler-Girls-Clothing-c-2058.html?ici=ar_tab03navbar07&scici=navbar_KidsHomePage~~tab03navbar07~~7~~real_2058~~~~0&src_module=topcat&src_tab_page_id=page_real_class1671382263884&src_identifier=fc%3DKids%60sc%3D%D8%B7%D9%81%D9%84%D8%A9%20%D8%B5%D8%BA%D9%8A%D8%B1%D8%A9%60tc%3D0%60oc%3D0%60ps%3Dtab03navbar07%60jc%3Dreal_2058&srctype=category&userpath=category-%D8%B7%D9%81%D9%84%D8%A9-%D8%B5%D8%BA%D9%8A%D8%B1%D8%A9")

soup = bs(url.text, "html.parser")
name = soup.find_all("div", {"class": "S-product-item__name"})
price = soup.find_all("span", {"class": "normal-price-ctn__sale-price"})

for i in range(len(name)):
    Name.append(name[i].text)
    Price.append(price[i].text)

file_list = [Name, Price]
Aya = zip_longest(*file_list)

with open("D:/Aya.csv", "w", encoding="utf-8") as d:
    wr = csv.writer(d)
    wr.writerow(["Name", "Price"])
    wr.writerows(Aya)