

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



## HTML

```

```



## XML

```python

```



## BeautifulSoup

**데이터를 파싱해주는 파서가 필요하고 그 중하나가 가장 유명한 BeautifulSoup이고 줄여서 bs라 부른다.**

**find_all** - 해당하는 모든 엘리먼트를 찾는다.

**select** - 해당하는 모든 엘리먼트를 찾는다. css셀렉터 사용가능.

```python

```

```python

```

```python
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