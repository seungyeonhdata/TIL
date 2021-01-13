
#정규화표현식으로 4자리까지 매칭하면 다섯자리 숫자도 매칭하고 맞다고 할수있음
#$붙여서 반드시 끝나게 할 수 있음
# import re
# if re.match("\d{4}$","12345"):
#     print("정상 전화번호")
# else:
#     print("비정상 전화번호")

# sub함수
# 대한민국, 한국, 코리아 모두 같은 것을 가리키지만 컴퓨터는 다르게 인식한다.
# re.sub("패턴","바꿀문자열","문자열",바꿀횟수)
# print(re.sub("apple|orange","fruit","apple tree banana orange"))
#두줄로 표현
# pat=re.compile("apple|orange")
# pat.sub("fruit","apple tree banana orange")

# "1 2 apple 3 banana 4 7 9 30 tree"
# print(re.sub("\d+","num","1 2 apple 3 banana 4 7 9 30 tree"))

#이미지 저장 : urlretrieve로 (주소, "넣을 파일이름")
# import urllib.request
# url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# urllib.request.urlretrieve(url,"test.png")
# print("저장완료")

#이미지 저장 2: urlopen으로 접속하고 read로 데이터 읽어옴
#이미지는 binary로 읽어와야한다. "wb"
# mem=urllib.request.urlopen(url).read()
# with open("test2.png","wb") as f:
#     f.write(mem)
#     print("저장되었습니다.")


# 웹페이지 동작 과정
# 클라이언트가 페이지를 요청한다(www.naver.com 요청)->웹서버(네이버측 슈퍼컴퓨타)
# ->메인페이지 제공(index.html)=소스코드를 보낸다->클라이언트는 웹브라우저로 화면 출력

# 다시.
# 클라이언트(날씨 클릭)->웹서버(날씨페이지(동적,jsp) 생성)-> 생성된 페이지를 html문서로 제공
# ->웹브라우저 해석->결과를 화면에 출력
#
# jsp,asp,php 등 :동적페이지
# hypertext: 서버와 클라이언트 간에 데이터를 동적으로 연결해주는 텍스트
# html은 구조가 없다
# 문서 내용을 컴퓨터가 이해하기가 어렵다
# 정적페이지
#
# xml은 구조화된 문서
# 문서 내용이 의미를 이해할 수 있게 작성됨
# 정적페이지
# 검색 폭이 넓고 검색 결과에 대한 정확도가 높음

# import urllib.parse as parse
# import urllib.request as request
# addr="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# values={'stdId':'109'}
# print(parse.urlencode(values)) #stdId=109
#
# params=parse.urlencode(values)
# url=addr+"?"+params
# print(url)
#http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=109

# data=request.urlopen(url).read()
# data=data.decode('utf-8')
# print(data)

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
# soup=BeautifulSoup(html3,"html.parser")
# print(soup) #html.parser로 분석할 수 있는 객체
# print(html3) #raw text
#출력 결과는 같지만 다른 객체
# links=soup.find_all('a')
# for i in links:
#     href=i.attrs['href'] #'href'는 속성임
#     print(i.string,"바로가기",href)

html4="""
<p><a href="aaa.html" name="clark">aaa page</a></p>
"""
# soup=BeautifulSoup(html4,"html.parser")
# print(soup.p.a.string)
# print(soup.a.attrs) #딕셔너리 구조로 속성과 값 나옴
# mydict=soup.a.attrs
# #href 속성 검색하기
# # print('href' in mydict)
# #값 출력
# print(mydict.values())
# #값 중 name키의 값 출력
# print(list(mydict.values())[1])
# print(soup.a.attrs.get('name'))

import urllib.request as req
url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res=req.urlopen(url) #res안에 페이지 내용이 담겨있음
#print(res) #<http.client.HTTPResponse object at 0x0000022CB4CB13D0>
soup=BeautifulSoup(res,"html.parser")
# print(soup.find('title').string) #첫번째 제목
# print(soup.find_all('title')[1].string)

#모든 wf 태그 내용 출력
# print(soup.find('wf').string)
# print(len(soup.find_all('wf'))) #534개

# 정상응답 -> 200:ok
# 문서를 찾지 못한경우 -> 40max()
# 서버 자체 오류 -> 50x

from bs4 import BeautifulSoup

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
# print(soup.select("div")) #리스트 안에 div 태그 통으로 들어감

#여러개 추출
# print(soup.select("div#lang > h1")[0].string) #lang 아이디 가진 div 태그 안에 h1을 리스트로 출력

#한개 추출
# print(soup.select_one("div#lang > h1").string) #첫 번째 요소가 문자열로 출력

# print(soup.select('div#lang > ul.items > li')) #클래스 이름은 .으로 지정
# print(soup.select_one('div#lang > ul.items > li'))
# mylist=soup.select('div#lang > ul.items > li')
# for i in mylist:
#     print(i.string)


















