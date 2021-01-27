# 1.
with open ("test.txt","w") as f:
    f.write("big data")
with open ("test.txt","r") as f:
    text=f.read()
    print(text)

# 2.
info="""
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
import re
p=re.compile("(\d{4})-\d{4}")
print(p.sub("\g<1>-####",info))

# 3.
<meta charset="UTF-8">

# 4.
from selenium import webdriver
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
url="https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=421&aid=0005127566"
driver.get(url)
html=driver.page_source
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,"html.parser")
title=soup.select("#articleTitle")[0].string
body=soup.select("#articleBodyContents")[0].text
print("제목 :",title)
print("내용 :",body)




