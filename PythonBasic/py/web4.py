#패키지 설치하기
#1. 설정-에디터-파이썬인터프레터-밑에 +로 검색해서 설치
#2.터미널에서 pip install 패키지명

#html 문서에서 id를 참조하기 위한 다양한 방법

# from bs4 import BeautifulSoup

# fp=open("lang.html",mode="r",encoding='utf-8')
# soup=BeautifulSoup(fp,"html.parser")

# print(soup.select_one("ul>li")) #첫번째 대상

# <li id="py">python</li> 추출하기
# print(soup.find_all("li")) #리스트로 출력. 모양은 좀 다름 [<li id="ja">java</li>, <li id="cp">cpp</li>, <li id="py">python</li>, <li id="sp">spark</li>, <li id="js">javascript</li>]
# print(soup.select("ul>li")) #리스트로 출력 #[<li id="ja">java</li>, <li id="cp">cpp</li>, <li id="py">python</li>, <li id="sp">spark</li>, <li id="js">javascript</li>]
# print(soup.select_one("ul>li#py")) #id가 py인
# print(soup.select_one("li#py")) #선택자(selector)
# print(soup.select_one("#py"))
# print(soup.select_one("ul#language > li#py"))
# print(soup.select_one("#language > #py"))
# print(soup.select_one("#language #py"))
# print(soup.select_one("li[id='py']"))
# print(soup.select_one("li:nth-of-type(3)"))

#네이버 달러 환율 정보 가져오기
import urllib.request as req
# url="https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
# res=req.urlopen(url) #한글깨짐
# res=req.urlopen(url).read().decode('euc-kr') #한글 깨질때
#
# soup=BeautifulSoup(res,"html.parser")
# print(soup.select("a.head.usd > div > span.value")[0].string)
# print(soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string)

# #기사 가져오기
import urllib.request as req
# url="https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
# res=req.urlopen(url).read()
# soup=BeautifulSoup(res,"html.parser")
# print("기사",soup.select_one("#content > div.section_news > div > ul > li:nth-child(1) > p > a"))

#Pop Quiz!-위키피디아->윤동주->'하늘과 바람과 별과 시' 가져오기
# from bs4 import BeautifulSoup
# import urllib.request as req
# url="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
# res=req.urlopen(url)
# soup=BeautifulSoup(res,"html.parser")
# print(soup)
# # print(soup.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a").string)
#
#'하늘과 바람과 별과 시'에 수록된 시 목록
# mylist=soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li")
# for li in mylist:
#     print(li.string)

# fp=open("fruits-vegetables.html",encoding='utf-8')
# soup=BeautifulSoup(fp,"html.parser")
#
# #아보카도 뽑기
# print(soup.select("ul#ve-list > li.black")[1].string)
# print(soup.select("#ve-list > li:nth-of-type(4)")[0].string)
# print(soup.select("#ve-list > li[data-lo='us']")[1].string)
# dic_c={"data-lo":"us","class":"black"}
# print(soup.find("li",dic_c).string)
# dic={"data-lo":"us"}
# print(soup.find(id="ve-list").findAll("li",dic)[1].string)
#
# #find==select_one, findAll==select
# print(soup.findAll("li",dic)[2].string)
# print(soup.find("li",dic).string)

#Selenium : 웹 브라우저를 제어하는 프로그램 pip install selenium
#ChromeDriver : 크롬 브라우저를 제어하는 프로그램
#크롬드라이버 설치 :크롬 도움말에서 정보 확인 후 버전 맞춰 드라이버 다운로드
#https://sites.google.com/a/chromium.org/chromedriver/downloads
# #c:/scrap/파일복사


#프로그램으로 크롬 제어하기
# from selenium import webdriver
# driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
# #
# url="https://www.naver.com"
# driver.get(url) #url 열기
# html=driver.page_source #소스코드 가져오기
# print(html)

#멜론 실시간 인기 차트 곡 수집
from bs4 import BeautifulSoup
# url="https://www.melon.com/chart/index.htm"
# driver.get(url)
# html=driver.page_source
# soup=BeautifulSoup(html,"html.parser")
# # print(soup)
# songs=soup.select("tr") #tr은 표의 행으로 구분=노래 목록일 것이다.
# print(len(songs)) #101
# songs=soup.select("tr")[1:] #top 100

# first=songs[0] #첫번째 노래
# title=first.select("a")
# print(title)
# print(first.select("span > a")) #노래 제목이 있는 부분

# 3위 BTS-다이너마이트
# bts=songs[2]
# print(bts.select("span > a"))
# print(bts.select("div.ellipsis.rank01>span>a")[0])
# print(songs)
# for song in songs:
#     print("곡 명 :", song.select("div.ellipsis.rank01 > span > a")[0].string)
#     print("가수명 : ", song.select("div.ellipsis.rank02 > span > a")[0].string)
#     print("=" * 50)

#????? 완전 놓침

#네이버 이미지 검색
# pup="https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B0%95%EC%95%84%EC%A7%80"
# kit="https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4"
# baseUrl="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# word=input("검색어를 입력하세요 :")
# from urllib.request import urlopen
# from urllib.parse import quote_plus
# num=int(input("개수 입력 :"))
# url=baseUrl+quote_plus(word)
# html=urlopen(url) #bs로 조작
# # print(html) #<http.client.HTTPResponse object at 0x00000282DE58F8E0>
# soup=BeautifulSoup(html,"html.parser")
# # print(soup)
# img=soup.find_all(class_="_img")
# print(len(img))

from selenium import webdriver
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
url="http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"

driver.get(url) #해당 url을 브라우저에 띄움
#print(driver.current_url)
#driver.implicitly_wait(3) #웹페이지의 모든 데이터를 읽을때까지 3초간 대기
source=driver.page_source
#print(source)
soup=BeautifulSoup(source,"html.parser")
prod_items=soup.select("li.prod_item")
for item in prod_items:
    print("모델명 :",item.select("p.prod_name>a")[0].string)
    print("상세정보 :",item.select('div.spec_list')[0].text.strip())
    print("가격 :",item.select('li.rank_one > p.price_sect > a > strong')[0].string)
    print("-"*100)

#productInfoDetail_12583850 > p.price_sect > a > strong
#연습문제
#다나와에서 노트북 검색 #동적인 페이지를 읽으려면 selenium 써야한다!
# from bs4 import BeautifulSoup
# import urllib.request as req
#
# from selenium import webdriver
# driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
# url="https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81"
# driver.get(url)
# res=driver.page_source
# soup=BeautifulSoup(res,"html.parser")
# prods=soup.search("ul.product_list")
# print(prods)

# names=soup.find_all("div.product_main_info")
# print(names)
# from bs4 import BeautifulSoup
# import urllib.request as req
# url="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
# res=req.urlopen(url)
# print(soup.findall("#adReaderProductItem11077416 > div > div.prod_info > p > a"))
#노트북 모델명
#인치
#등록월
#평점, 평점을 매긴 건수

#1번의 정보들을 10페이지까지 추출
# for i in range(10):
# 1페이지="http://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page=1&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10586%7C0&defaultVmTab=77822&defaultVaTab=9995878&tab=goods"
# 2페이지="http://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page=2&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10586%7C0&defaultVmTab=77822&defaultVaTab=9995878&tab=goods"
# 3페이지="http://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page=3&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10586%7C0&defaultVmTab=77818&defaultVaTab=9995917&tab=goods"
# urlopen(1페이지)













#보배드림-차량정보 추출
# url="https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
# res=req.urlopen(url)
# soup=BeautifulSoup(res,"html.parser")

# cars=soup.select("ul.clearfix>li.product-item")
# for car in cars:
#     print("차종 :",car.select("div.mode-cell.title>p>a")[0].string)
#     print("연식 :",''.join((car.select("div.mode-cell.year>span")[0]).strings))
#     print("연료 :",car.select("div.mode-cell.fuel>span")[0].string)
#     print("가격 :",car.select("div.mode-cell.price>b>em")[0].string,"만원")
#     print("-"*50)

# --------------------------------------------------
# 차종 : 기아 K5 2세대 2.0 가솔린 SX 디럭스
# 연식 : 15/11(16년형)
# 연료 : 가솔린
# 가격 : 1,090 만원
# --------------------------------------------------

#연도를 나열식으로 하나의 문자열로 만들때
# for car in cars:
#     car=str(car)
#     car=re.sub('<.+?>','',car,0).strip()
#     print(car)



#로튼토마토 popular streaming movies
#순위와 함께 영화 제목 추출

# url="https://www.rottentomatoes.com/"
# res=req.urlopen(url)
# soup=BeautifulSoup(res,"html.parser")
# titles=soup.select("div.js-scores-lists-wrapper>div:nth-child(1)>section>text-list > ul>li")
# index=1
# for title in titles:
#     print("%d위 :"%index,title.select("a:nth-child(1) > span")[0].string)
#     index+=1




# 류경희님 풀이
# 1. 다나와 -> 무선청소기 검색 결과

from urllib.request import urlopen
import re

# from selenium import webdriver
# driver = webdriver.Chrome('c:/scrap/chromedriver.exe')
# url = "http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
# driver.get(url)
# from bs4 import BeautifulSoup
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

 # 1) 무선청소기 모델명(굵은 글씨)
#
# name = soup.select('p.prod_name > a')
#
# for i in name:
#     print(i.string)

# 2) 세부사항
#
# spec_list = soup.select('div.spec_list')
#
# for i in spec_list:
#     print(i.text.strip())

# 이름 + 세부사항

# for i, j in zip(name, spec_list):
#     print(i.text.strip(), j.text.strip())

# 3) 등록월
#
# date = soup.select('dl.meta_item.mt_date > dd')[:42]
#
# for i in date:
#     print(i.string)

#모델명+등록월

# for i,j in zip(name, date):
#     print(i.text.strip(),j.text.strip())


# 4) 평점, 평점을 매긴 건수

# score = soup.select('div.cnt_star > div.point_num')
# num = soup.select(' div.cnt_opinion')
#
# for i,j in zip(score, num):
#     print(i.text.strip(), j.text.strip())

# 2. 1번 문제를 다 해결했다면,

# 1~10페이지까지 노트북에 대한 정보를 추출
#
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# for i in range(1,100):
#     print('<{}page 검색 결과>'.format(i))
#
# url ='http://search.danawa.com/dsearch.php?query=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&originalQuery=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page={0}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=103740&defaultPhysicsCategoryCode=72%7C80%7C81%7C0&defaultVmTab=2389&defaultVaTab=120926&tab=goods'.format(i)
# driver = webdriver.Chrome ( 'c:/scrap/chromedriver.exe' )
# driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup ( html, 'html.parser' )
# spec = soup.select('div.spec_list')
# name = soup.select('p.prod_name > a')
#
# for j,k in zip(name,spec):
#     print(j.text.strip(),k.text.strip())
#
#
# # # 3. 보배드림 -> 차량정보추출
#
# url ='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
# driver.get(url)
# html = driver.page_source
# # print(html)
# soup = BeautifulSoup(html,'html.parser')
#
# #차 이름
#
# name = soup.select('div.mode-cell.title > p.tit > a')
#
# ## 1)연식
#
# year = soup.select('div.mode-cell.year > span')
#
# for i in year:
#     print(i.text.strip())
#
# # #차 이름 + 연식
# for i,j in zip(name,year):
#     print(i.text.strip(),'|',j.text.strip())
#
# # # 2)연료
#
# fuel = soup.select('div.mode-cell.fuel > span')
#
# for i in fuel:
#     print(i.string)
# for i,j in zip(name,fuel):
#     print(i.text.strip(),'|',j.text.strip())
#
# # # 3)가격
#
# price = soup.select('div.mode-cell.price > b')
#
# for i in price:
#     print(i.text.strip(),'만원')
#
# #이름+가격
# for i,j in zip(name,price):
#     print(i.text.strip(),'|',j.text.strip())
#
#
# # 4. https://www.rottentomatoes.com/ => popular streaming movies
#
# # 순위와 함께 영화 제목 추출
#
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# url='https://www.rottentomatoes.com/'
# driver=webdriver.Chrome('c:/scrap/chromedriver.exe')
# driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html,'html.parser')
# # print(soup.select('#media-lists > div.layout.media-lists > div > div.js-scores-lists-wrapper.ordered-layout__scores-wrap > div > section > text-list > ul > li'))
# title = (soup.select('text-list > ul > li > a:nth-child(1) > span'))
#
# for i, v in enumerate(title):
#     print("순위 : {}, 제목: {}".format(i+1,v.text.strip()))