from bs4 import BeautifulSoup
import requests
import requests as rq
import os
b=input()
respond=requests.get(f"https://web.archive.org/web/20210914150403/https://nhentai.net/g/{b}/")
soup=BeautifulSoup(respond.text,"html.parser")
soup=soup.find_all("span",class_="name")
print(soup)
soup=soup[-1].text
a=soup
os.mkdir(f"./{b}")
for i in range(1,int(a)+2):
    respond=requests.get(f"https://web.archive.org/web/20210824054045/https://nhentai.net/g/{b}/{i}/")
    soup=BeautifulSoup(respond.text,"html.parser")
    soup=soup.find_all("img")
    soup=soup[1].get("src")
    print(soup)
    r=requests.get(soup)
    print(i)
    with open(f"./{b}/{i}.png","wb") as f:
        f.write(r.content)

