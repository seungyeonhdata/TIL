



## HTML

```

```



## XML

```python

```



## BeautifulSoup

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