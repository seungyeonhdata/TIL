**크롤링(crawling)**

크롤링이란 단어는 웹 크롤러(crawler)라는 단어에서 시작한 말이다.

크롤러란 조직적, 자동화된 방법으로 월드와이드 웹을 탐색하는 컴퓨터 프로그램이다.(출처: 위키백과)

크롤링은 크롤러가 하는 작업을 부르는 말로, 여러 인터넷 사이트의 페이지(문서, html 등)를 수집해서 분류하는 것이다.

대체로 찾아낸 데이터를 저장한 후 쉽게 찾을 수 있게 인덱싱한다.



**파싱(parsing)**

파싱이란 어떤 페이지(문서, html 등)에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출하여 정보를 가공하는 것이다.

위 문장만 보면 굉장히 간단해 보이지만 컴퓨터 과학적 정의를 보면 파싱이란 일련의 문자열을 의미있는 토큰(token)으로 분해하고 이들로 이루어진 파스 트리(parse tree)를 만드는 과정을 말한다.(출처: 위키백과)

인터프리터나 컴파일러의 구성 요소 가운데 하나로, 입력 토큰에 내제된 자료 구조를 빌드하고 문법을 검사하는 역할을 한다.



**스크래핑(scraping)**

스크래핑이란 HTTP를 통해 웹 사이트의 내용을 긁어다 원하는 형태로 가공하는 것이다.

쉽게 말해 웹 사이트의 데이터를 수집하는 모든 작업을 뜻한다.

크롤링도 일종의 스크래핑 기술이라고 할 수 있다.



```
<웹페이지 동작 과정>

클라이언트가 페이지를 요청한다(www.naver.com 요청)->웹서버(네이버측 슈퍼컴퓨타)
->메인페이지 제공(index.html)=소스코드를 보낸다->클라이언트는 웹브라우저로 화면 출력

클라이언트(날씨 클릭)->웹서버(날씨페이지(동적,jsp) 생성)-> 생성된 페이지를 html문서로 제공
->웹브라우저 해석->결과를 화면에 출력

jsp,asp,php 등 :동적페이지
hypertext: 서버와 클라이언트 간에 데이터를 동적으로 연결해주는 텍스트
html은 구조가 없다
문서 내용을 컴퓨터가 이해하기가 어렵다
정적페이지

xml은 구조화된 문서
문서 내용이 의미를 이해할 수 있게 작성됨
정적페이지
검색 폭이 넓고 검색 결과에 대한 정확도가 높음
```

## urllib

### 페이지 변경

```python
import urllib.parse as parse
import urllib.request as request
addr="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
values={'stdId':'109'}
print(parse.urlencode(values)) #stdId=109

params=parse.urlencode(values)
url=addr+"?"+params
print(url)
#http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=109

data=request.urlopen(url).read()
data=data.decode('utf-8')
print(data)
```



### 이미지 저장

```python
import urllib
이미지 저장 : urlretrieve로 (주소, "넣을 파일이름")
import urllib.request
url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
urllib.request.urlretrieve(url,"test.png")
print("저장완료")

이미지 저장 2: urlopen으로 접속하고 read로 데이터 읽어옴
이미지는 binary로 읽어와야한다. "wb"
mem=urllib.request.urlopen(url).read()
with open("test2.png","wb") as f:
    f.write(mem)
    print("저장되었습니다.")
```

### 소스코드 뽑아오기

* 패키지 설치

```
패키지 설치하기
1.설정-에디터-파이썬인터프레터-밑에 +로 검색해서 설치
2.터미널에서 pip install 패키지명
```

* html 문서에서 id 참조

```python
import urllib.request as req
url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res=req.urlopen(url) #res안에 페이지 내용이 담겨있음
#print(res) #<http.client.HTTPResponse object at 0x0000022CB4CB13D0>
```



## BeautifulSoup

**데이터를 파싱해주는 파서. 줄여서 bs.**

```python
from bs4 import BeautifulSoup
html="""
<html><body>
<h1>스크래핑</h1>
<p>웹 페이지 분석</p>
<p>원하는 부분 추출</p>
</body></html>
"""
soup=BeautifulSoup(html,'html.parser')
print(soup.html.body.h1)#태그이름 순서대로 적는다
print(soup.html.body.p.string) #태그안의 문자열만 추출
p2=soup.html.body.p
para2=para.next_sibling #줄바꿈 문자
print(para2.next_sibling.string)
# 한줄로 줄이면
print(p2.next_sibling.next_sibling.string)
html2="""
<html><body>
<h1 id='title'>스크래핑</h1>
<p id='body'>웹 페이지 분석</p>
<p>원하는 부분 추출</p>
</body></html>
"""
# soup=BeautifulSoup(html2,'html.parser')
# print(soup.find(id='body').string)

html3="""
<html><body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
</ul>
</body></html>
"""
soup=BeautifulSoup(html3,"html.parser")
print(soup) #html.parser로 분석할 수 있는 객체
print(html3) #raw text
#출력 결과는 같지만 다른 객체
links=soup.find_all('a')
for i in links:
    href=i.attrs['href'] #'href'는 속성임
    print(i.string,"바로가기",href)

html4="""
<p><a href="aaa.html" name="clark">aaa page</a></p>
"""
soup=BeautifulSoup(html4,"html.parser")
print(soup.p.a.string)
print(soup.a.attrs) #딕셔너리 구조로 속성과 값 나옴
mydict=soup.a.attrs
#href 속성 검색하기
# print('href' in mydict)
#값 출력
print(mydict.values())
#값 중 name키의 값 출력
print(list(mydict.values())[1])
print(soup.a.attrs.get('name'))

import urllib.request as req
url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res=req.urlopen(url) #res안에 페이지 내용이 담겨있음
#print(res) #<http.client.HTTPResponse object at 0x0000022CB4CB13D0>
soup=BeautifulSoup(res,"html.parser")
print(soup.find('title').string) #첫번째 제목
print(soup.find_all('title')[1].string)

html5 = """
<html><body>
<div id="lang">
    <h1>programming</h1>
    <ul class="items">
        <li>python</li>
        <li>java</li>
        <li>cpp</li>
    </ul>
</div>
</body></html>
"""

soup=BeautifulSoup(html5,"html.parser")
print(soup.select("div")) #리스트 안에 div 태그 통으로 들어감

여러개 추출
print(soup.select("div#lang > h1")[0].string) #lang 아이디 가진 div 태그 안에 h1을 리스트로 출력

한개 추출
print(soup.select_one("div#lang > h1").string) #첫 번째 요소가 문자열로 출력

print(soup.select('div#lang > ul.items > li')) #클래스 이름은 .으로 지정
print(soup.select_one('div#lang > ul.items > li'))
mylist=soup.select('div#lang > ul.items > li')
for i in mylist:
    print(i.string)
    
from bs4 import BeautifulSoup

fp=open("lang.html",mode="r",encoding='utf-8')
soup=BeautifulSoup(fp,"html.parser")

print(soup.select_one("ul>li")) #첫번째 대상

<li id="py">python</li> 추출하기
print(soup.find_all("li")) #리스트로 출력. 모양은 좀 다름 [<li id="ja">java</li>, <li id="cp">cpp</li>, <li id="py">python</li>, <li id="sp">spark</li>, <li id="js">javascript</li>]
print(soup.select("ul>li")) #리스트로 출력 #[<li id="ja">java</li>, <li id="cp">cpp</li>, <li id="py">python</li>, <li id="sp">spark</li>, <li id="js">javascript</li>]
print(soup.select_one("ul>li#py")) #id가 py인
print(soup.select_one("li#py")) #선택자(selector)
print(soup.select_one("#py"))
print(soup.select_one("ul#language > li#py"))
print(soup.select_one("#language > #py"))
print(soup.select_one("#language #py"))
print(soup.select_one("li[id='py']"))
print(soup.select_one("li:nth-of-type(3)"))

fp=open("fruits-vegetables.html",encoding='utf-8')
soup=BeautifulSoup(fp,"html.parser")
#아보카도 뽑기
print(soup.select("ul#ve-list > li.black")[1].string)
print(soup.select("#ve-list > li:nth-of-type(4)")[0].string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
dic_c={"data-lo":"us","class":"black"}
print(soup.find("li",dic_c).string)
dic={"data-lo":"us"}
print(soup.find(id="ve-list").findAll("li",dic)[1].string)
#find==select_one, findAll==select
print(soup.findAll("li",dic)[2].string)
print(soup.find("li",dic).string)



#네이버 달러 환율 정보 가져오기
import urllib.request as req
url="https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res=req.urlopen(url) #한글깨짐
res=req.urlopen(url).read().decode('euc-kr') #한글 깨질때
soup=BeautifulSoup(res,"html.parser")
print(soup.select("a.head.usd > div > span.value")[0].string)
print(soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string)

#기사 가져오기
import urllib.request as req
url="https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res=req.urlopen(url).read()
soup=BeautifulSoup(res,"html.parser")
print("기사",soup.select_one("#content > div.section_news > div > ul > li:nth-child(1) > p > a"))

#Pop Quiz!-위키피디아->윤동주->'하늘과 바람과 별과 시' 가져오기
from bs4 import BeautifulSoup
import urllib.request as req
url="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res=req.urlopen(url)
soup=BeautifulSoup(res,"html.parser")
#print(soup)
print(soup.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a").string)

#'하늘과 바람과 별과 시'에 수록된 시 목록
mylist=soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li")
for li in mylist:
    print(li.string)




#네이버 이미지 검색
pup="https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B0%95%EC%95%84%EC%A7%80"
kit="https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4"
baseUrl="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
word=input("검색어를 입력하세요 :")
from urllib.request import urlopen
from urllib.parse import quote_plus
num=int(input("개수 입력 :"))
url=baseUrl+quote_plus(word)
html=urlopen(url) #bs로 조작
# print(html) #<http.client.HTTPResponse object at 0x00000282DE58F8E0>
soup=BeautifulSoup(html,"html.parser")
# print(soup)
img=soup.find_all(class_="_img")
print(len(img))

from bs4 import BeautifulSoup
html="""
<html><body>
<h1>스크래핑</h1>
<p>웹 페이지 분석</p>
<p>원하는 부분 추출</p>
</body></html>
"""

# soup=BeautifulSoup(html,'html.parser')
#대문자로 시작하면 클래스
#괄호는 클래스로 객체를 만드는것(괄호안의 내용은 객체의 초기값)
#붕어빵봉투=붕어빵기계(크림, 10센티)
# print(soup.html.body.h1)#태그이름 순서대로 적는다
# print(soup.html.body.p.string) #태그안의 문자열만 추출
#p태그들은 여러개이고 시블링(형제)관계다.
# p2=soup.html.body.p
# para2=para.next_sibling #줄바꿈 문자
# print(para2.next_sibling.string)
# 한줄로 줄이면
# print(p2.next_sibling.next_sibling.string)

html2="""
<html><body>
<h1 id='title'>스크래핑</h1>
<p id='body'>웹 페이지 분석</p>
<p>원하는 부분 추출</p>
</body></html>
"""
# soup=BeautifulSoup(html2,'html.parser')
# print(soup.find(id='body').string)

html3="""
<html><body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
</ul>
</body></html>
"""
soup=BeautifulSoup(html3,"html.parser")
# print(soup) #html.parser로 분석할 수 있는 객체
# print(html3) #raw text
#출력 결과는 같지만 다른 객체
links=soup.find_all('a')
for i in links:
    href=i.attrs['href'] #'href'는 속성임
    print(i.string,"바로가기",href)

html4="""
<p><a href="aaa.html">aaa page</a></p>
"""
soup=BeautifulSoup(html4,"html.parser")
print(soup.p.a.string)
print(soup.a.attrs) #딕셔너리 구조로 속성과 값 나옴
mydict=soup.a.attrs
#href 속성 검색하기
# print('href' in mydict)
#값 출력
print(mydict.values())
#값 중 name키의 값 출력
print(list(mydict.values())[1])
print(soup.a.attrs.get('name'))

```

**find_all** - 해당하는 모든 엘리먼트를 찾는다.

**select** - 해당하는 모든 엘리먼트를 찾는다. css셀렉터 사용가능.

```python
# 정상응답 -> 200:ok
# 문서를 찾지 못한경우 -> 40max()
# 서버 자체 오류 -> 50x
```

## selenium

```python
Selenium : 웹 브라우저를 제어하는 프로그램 pip install selenium
ChromeDriver : 크롬 브라우저를 제어하는 프로그램
크롬드라이버 설치 :크롬 도움말에서 정보 확인 후 버전 맞춰 드라이버 다운로드
https://sites.google.com/a/chromium.org/chromedriver/downloads
#c:/scrap/파일복사


#프로그램으로 크롬 제어하기
from selenium import webdriver
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")

url="https://www.naver.com"
driver.get(url) #url 열기
html=driver.page_source #소스코드 가져오기
print(html)

#멜론 실시간 인기 차트 곡 수집
from bs4 import BeautifulSoup
url="https://www.melon.com/chart/index.htm"
driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html,"html.parser")
# print(soup)
songs=soup.select("tr") #tr은 표의 행으로 구분=노래 목록일 것이다.
print(len(songs)) #101
songs=soup.select("tr")[1:] #top 100

first=songs[0] #첫번째 노래
title=first.select("a")
print(title)
print(first.select("span > a")) #노래 제목이 있는 부분

#3위 BTS-다이너마이트
bts=songs[2]
print(bts.select("span > a"))
print(bts.select("div.ellipsis.rank01>span>a")[0])
print(songs)
for song in songs:
    print("곡 명 :", song.select("div.ellipsis.rank01 > span > a")[0].string)
    print("가수명 : ", song.select("div.ellipsis.rank02 > span > a")[0].string)
    print("=" * 50)

#다나와에서 무선청소기 검색
from selenium import webdriver
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
url="https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81"
driver.get(url) #해당 url을 브라우저에 띄움
#print(driver.current_url)
driver.implicitly_wait(3) #웹페이지의 모든 데이터를 읽을때까지 3초간 대기
res=driver.page_source
#print(res)
soup=BeautifulSoup(res,"html.parser")
prods=soup.search("ul.product_list")
#print(prods)
for item in prods:
    print("모델명 :",item.select("p.prod_name>a")[0].string)
    print("상세정보 :",item.select('div.spec_list')[0].text.strip())
    print("가격 :",item.select('li.rank_one > p.price_sect > a > strong')[0].string)
    print("-"*100)

```



## 연습

```python
str="이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
names=str.split(',')

# 김씨, 이씨, 이재영 반복횟수
count_kim=0
count_lee=0
count_ljy=0
for i in names:
    if i.startswith("김"):
        count_kim+=1
    if i.startswith("이"):
        count_lee+=1
    if i=='이재영':
        count_ljy += 1
print("김씨는 {}명, 이씨는 {}명, '이재영'은 {}번 나온다".format(count_kim,count_lee,count_ljy))

# 중복 제거한 이름
print(set(names))

# 중복 제거한 이름 오름차순 정렬
asc=list(set(names))
asc.sort()
print(asc)
```

### 토지 텍스트 추출

```python
from bs4 import BeautifulSoup
with open("toji.txt","rt",encoding='utf-16') as f:
    toji=f.read()
soup=BeautifulSoup(toji,"html.parser")

# print(type(toji))
#저자명
print(soup.find('author').string)
#제목
print(soup.select('title')[1].string)
#출판사명
print(soup.find('publisher').string)

#인용 추출하여 리스트에 저장
import re
quotes=re.findall("\"(.+)\"",toji) #'KO" usage="99'
print(quotes)

#한글 추출하여 저장, 최고빈도 단어 100개 출력
kor=re.findall('[가-힣]{2,}',toji)
counts={}
for i in kor:
    counts[i] = counts.get(i, 0) + 1
print([(key,value) for (key,value) in sorted(counts.items(),key=lambda k:k[1],reverse=True)][:101])

#각 장의 제목 저장 및 출력
chapter=soup.select('head')
for i in chapter:
    print(i.string)
    
    
+다른 풀이
from bs4 import BeautifulSoup

with open("toji.txt", "r", encoding='utf-16') as f:
    toji = f.read()
    soup = BeautifulSoup(toji, 'html.parser')

    # 1) 저자명 추출
    print('저자명 :', soup.find('author').string)

    # 2) 제목 추출
    print('제목 :', soup.find('title').string)

    # 3) 출판사명 추출
    print('출판사명 :', soup.find('publisher').string)

    # 4) 인용부호(큰 따옴표)로 묶여있는 내용을 모두 추출하여 리스트에 저장
import re
dialog = []
for x in re.findall('\"(.+)\"', toji):
    dialog.append(x)

    # 5) 토지 원고 전체에서 한글에 해당되는 내용만 추출하여 저장, 가장 많이 사용된 단어 100개 추출
import re
words = re.findall('[ㄱ-힣]{2,}', toji)
# print(words)
words_count = {}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_words[:101])

    # 6) 각 장의 제목 저장 및 출력
    chap = soup.find_all('head')
    for x in chap:
        print(x)
```



### 웹페이지 긁어오기

```python
보배드림-차량정보 추출
url="https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
res=req.urlopen(url)
soup=BeautifulSoup(res,"html.parser")

cars=soup.select("ul.clearfix>li.product-item")
for car in cars:
    print("차종 :",car.select("div.mode-cell.title>p>a")[0].string)
    print("연식 :",''.join((car.select("div.mode-cell.year>span")[0]).strings))
    print("연료 :",car.select("div.mode-cell.fuel>span")[0].string)
    print("가격 :",car.select("div.mode-cell.price>b>em")[0].string,"만원")
    print("-"*50)

--------------------------------------------------
차종 : 기아 K5 2세대 2.0 가솔린 SX 디럭스
연식 : 15/11(16년형)
연료 : 가솔린
가격 : 1,090 만원
--------------------------------------------------

연도를 나열식으로 하나의 문자열로 만들때
for car in cars:
    car=str(car)
    car=re.sub('<.+?>','',car,0).strip()
    print(car)



로튼토마토 popular streaming movies
순위와 함께 영화 제목 추출

url="https://www.rottentomatoes.com/"
res=req.urlopen(url)
soup=BeautifulSoup(res,"html.parser")
titles=soup.select("div.js-scores-lists-wrapper>div:nth-child(1)>section>text-list > ul>li")
index=1
for title in titles:
    print("%d위 :"%index,title.select("a:nth-child(1) > span")[0].string)
    index+=1

```

### 스타벅스 매장 정보

```python
from selenium import webdriver
browser=webdriver.Chrome("c:/scrap/chromedriver.exe")
url="https://www.istarbucks.co.kr/store/store_map.do?disp=locale"
browser.get(url)
seoulBtn="#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a"
browser.find_element_by_css_selector(seoulBtn).click()
allBtn="#mCSB_2_container > ul > li:nth-child(1) > a"
browser.find_element_by_css_selector(allBtn).click()
source=browser.page_source
soup=BeautifulSoup(source,"html.parser")
sb_list=soup.select("li.quickResultLstCon")
sb_store=sb_list[0]
name=sb_list[0].select("strong")[0].text #string은 안되네
name
lat=sb_store['data-lat']
lng=sb_store['data-long']
sb_type=sb_store.select("i")[0]['class']
addr=str(sb_store.select("p")[0]).split("<br/>")[0].split(">")[1]
# addr=''.join((sb_store.select("p")[0]).strings)
tel=str(sb_store.select("p")[0]).split("<br/>")[1].split("<")[0]
seoul_sb_list=[]
for item in sb_list:
    name=item.select("strong")[0].text
    lat=item['data-lat']
    lng=item['data-long']
    sb_type=item.select("i")[0]['class']
    addr=str(item.select("p")[0]).split("<br/>")[0].split(">")[1]
    tel=str(item.select("p")[0]).split("<br/>")[1].split("<")[0]
    seoul_sb_list.append([name,lat,lng,sb_type,addr,tel])
import pandas as pd
col=['매장명','위도','경도','매장타입','주소','전화번호']
sb_df=pd.DataFrame(seoul_sb_list, columns=col)
sb_df.to_excel("스타벅스정보.xlsx", index=False)
```

### 인스타그램 로그인&검색

```python
from selenium import webdriver
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")import time
driver.get("https://www.instagram.com")
time.sleep(2)
#로그인하기
email="01028849804"
password=""
input_id=driver.find_elements_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")[0]
input_id.clear()
input_id.send_keys(email)
input_pw=driver.find_elements_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")[0]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit() #엔터 누르는거

def insta_searching(word):
    url="https://www.instagram.com/explore/tags/"+word
    return url
word="조던1하이"
url=insta_searching(word)
driver.get(url)
def select_first(driver):
    first=driver.find_element_by_css_selector("div._9AhH0")
    first.click()
    time.sleep(2)
select_first(driver)
import re
def getContent(driver):
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    content=soup.select("div.C4VMK>span")[0].text
    tags=re.findall("#[\S,]+",content)
    date=soup.select("time.FH9sR.Nzb55")[0]['datetime'][:10]
    data=[content, date, tags]
    return data
getContent(driver)
#다음페이지 이동
def next_page(driver):
    n_page=driver.find_element_by_css_selector("div.EfHg9 > div > div > a")
    n_page.click()
next_page(driver)

```

### 스택오버플로우 제목 추출

```python
from selenium import webdriver
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
url="https://stackoverflow.com/questions/tagged/python"
driver.get(url)
def title(driver):
    source=driver.page_source
    soup=BeautifulSoup(source,"html.parser")
    titles=soup.select("div.question-summary")
    index=1
    for title in titles:
        print(index,title.select("div.summary>h3>a")[0].string)
        index+=1
title(driver)
```

