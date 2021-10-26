from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
b=input()
driver.get(f"https://www.wnacg.org/photos-slide-aid-{b}.html")
a=1
t=0
while 1:
    driver.execute_script(f'document.documentElement.scrollTop={a}')
    a=a+1000
    c=driver.execute_script(f'document.documentElement.scrollTop={a}')
    if t==c:
        break
    else:t=c
soup=BeautifulSoup(driver.page_source,"html.parser")
soup=soup.find_all("div",style="text-align:center;color:#999;padding-bottom:10px;font-size:13px;")
os.mkdir(f"./{b}")
for k in range(len(soup)-1):
    img=soup[k].find("img")
    img=img.get("src")
    r=requests.get(f"https:{img}")
    print(img)
    with open(f"./{b}/{k}.png","wb") as f:
        f.write(r.content)


