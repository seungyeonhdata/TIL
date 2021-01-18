# 정규표현식



```python
import re
```

```python
# jumin 데이터의 뒷 부분을 모두 *로 변환하여 출력

jumin="""
park 850201-1264597
kim 95d544-1523654
"""

p=re.compile("(\d{6})[-]\d{7}")
print(p.sub("\g<1>-*******",jumin))

#주민번호 입력 받아서 뒷자리 *처리하기
for line in jumin.split("\n"):
    for word in line.split(" "):
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
            word=word[:6]+"-"+"*******"
            print(word)
```



**메타문자** : 정보의 정보, 데이터(전화번호부)의 데이터(색인) 등

```
종류 : ( ) { } [ ] \ | ? + * $ ^
```

## 규칙

| 명령어    | 설명                                                 |
| --------- | ---------------------------------------------------- |
| `[]`      | 안에는 어떤 문자도 올 수 있음                        |
| `{}`      | 횟수 또는 범위 나타냄                                |
| `()`      | 소괄호 안의 문자를 하나의 문자로 인식                |
| `[abcd]`  | a,b,c,d 중 어떤 한 개의 문자와 매치                  |
| `[0-5]`   | [from-to]로 범위 지정                                |
| `[^3-5]`  | ^뒤에 오는 문자 제외                                 |
| `*`       | * 앞에 있는 대상이 0개 이상이면 매치                 |
| `+`       | + 앞에 있는 대상이 1개 이상이면 매치                 |
| `.`       | 임의의 문자 1개(와일드 카드)                         |
| `?`       | 임의의 문자 0개 또는 1개(탐욕스럽지 않은 방식)       |
| `^첫글자` | ^로 라인의 첫 글자 매치                              |
| `끝글자$` | $로 라인의 끝 글자 매치                              |
| `|`       | 패턴 안에서 or 연산                                  |
| `\d`      | [0-9]                                                |
| `\D`      | [^0-9]                                               |
| `\s`      | [공백, 탭, 엔터]                                     |
| `\S`      | [not 공백, 탭, 엔터]                                 |
| `\w`      | [a-zA-Z0-9_]                                         |
| `\W `     | [^a-zA-Z0-9_]                                        |
| `\`       | 확장 문자로 특수문자 앞에 넣으면 문자 그 자체를 의미 |
| `(?i)`    | 앞부분에 옵션으로 넣으면 대소문자 구분 안함          |

> 명령어 그 자체를 검색하고 싶으면 `\`붙이거나 `[]`안에 넣음

* `compile()` : 패턴 객체



## 컴파일 옵션

정규식을 컴파일할 때 다음 옵션을 사용할 수 있다.

- DOTALL(S) - `.` 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
- IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
- MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (`^`, `$` 메타문자의 사용과 관계가 있는 옵션이다)
- VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)

옵션을 사용할 때는 `re.DOTALL`처럼 전체 옵션 이름을 써도 되고 `re.S`처럼 약어를 써도 된다.

### DOTALL, S

`.` 메타 문자는 줄바꿈 문자(`\n`)를 제외한 모든 문자와 매치되는 규칙이 있다. 만약 `\n` 문자도 포함하여 매치하고 싶다면 `re.DOTALL` 또는 `re.S` 옵션을 사용해 정규식을 컴파일하면 된다.

다음 예를 보자.

```
>>> import re
>>> p = re.compile('a.b')
>>> m = p.match('a\nb')
>>> print(m)
None
```

정규식이 `a.b`인 경우 문자열 `a\nb`는 매치되지 않음을 알 수 있다. 왜냐하면 `\n`은 `.` 메타 문자와 매치되지 않기 때문이다. `\n` 문자와도 매치되게 하려면 다음과 같이 `re.DOTALL` 옵션을 사용해야 한다.

```
>>> p = re.compile('a.b', re.DOTALL)
>>> m = p.match('a\nb')
>>> print(m)
<_sre.SRE_Match object at 0x01FCF3D8>
```

보통 `re.DOTALL` 옵션은 여러 줄로 이루어진 문자열에서 `\n`에 상관없이 검색할 때 많이 사용한다.

### IGNORECASE, I

`re.IGNORECASE` 또는 `re.I` 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션이다. 다음 예제를 보자.

```
>>> p = re.compile('[a-z]', re.I)
>>> p.match('python')
<_sre.SRE_Match object at 0x01FCFA30>
>>> p.match('Python')
<_sre.SRE_Match object at 0x01FCFA68>
>>> p.match('PYTHON')
<_sre.SRE_Match object at 0x01FCF9F8>
```

`[a-z]` 정규식은 소문자만을 의미하지만 re.I 옵션으로 대소문자 구별 없이 매치된다.

### MULTILINE, M

`re.MULTILINE` 또는 `re.M` 옵션은 조금 후에 설명할 메타 문자인 `^`, `$`와 연관된 옵션이다. 이 메타 문자에 대해 간단히 설명하자면 `^`는 문자열의 처음을 의미하고, `$`는 문자열의 마지막을 의미한다. 예를 들어 정규식이 `^python`인 경우 문자열의 처음은 항상 python으로 시작해야 매치되고, 만약 정규식이 `python$`이라면 문자열의 마지막은 항상 python으로 끝나야 매치된다는 의미이다.

다음 예를 보자.

```
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
```

정규식 `^python\s\w+`은 python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미이다. 검색할 문자열 data는 여러 줄로 이루어져 있다.

이 스크립트를 실행하면 다음과 같은 결과를 돌려준다.

```
['python one']
```

`^` 메타 문자에 의해 python이라는 문자열을 사용한 첫 번째 줄만 매치된 것이다.

하지만 `^` 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶은 경우도 있을 것이다. 이럴 때 사용할 수 있는 옵션이 바로 `re.MULTILINE` 또는 `re.M`이다. 위 코드를 다음과 같이 수정해 보자.

```
import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
```

`re.MULTILINE` 옵션으로 인해 `^` 메타 문자가 문자열 전체가 아닌 각 줄의 처음이라는 의미를 갖게 되었다. 이 스크립트를 실행하면 다음과 같은 결과가 출력된다.

```
['python one', 'python two', 'python three']
```

즉 `re.MULTILINE` 옵션은 `^`, `$` 메타 문자를 문자열의 각 줄마다 적용해 주는 것이다.

### VERBOSE, X

지금껏 알아본 정규식은 매우 간단하지만 정규식 전문가들이 만든 정규식을 보면 거의 암호수준이다. 정규식을 이해하려면 하나하나 조심스럽게 뜯어보아야만 한다. 이렇게 이해하기 어려운 정규식을 주석 또는 줄 단위로 구분할 수 있다면 얼마나 보기 좋고 이해하기 쉬울까? 방법이 있다. 바로 `re.VERBOSE` 또는 `re.X` 옵션을 사용하면 된다.

다음 예를 보자.

```
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
```

위 정규식이 쉽게 이해되는가? 이제 다음 예를 보자.

```
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
```

첫 번째와 두 번째 예를 비교해 보면 컴파일된 패턴 객체인 charref는 모두 동일한 역할을 한다. 하지만 정규식이 복잡할 경우 두 번째처럼 주석을 적고 여러 줄로 표현하는 것이 훨씬 가독성이 좋다는 것을 알 수 있다.

`re.VERBOSE` 옵션을 사용하면 문자열에 사용된 whitespace는 컴파일할 때 제거된다(단 [ ] 안에 사용한 whitespace는 제외). 그리고 줄 단위로 #기호를 사용하여 주석문을 작성할 수 있다.



* `match()`

```python
re.match("패턴","문자열") #문자열이 패턴에 부합되나요?
match는 일치하지 않는 부분 나오면 바로 끝남

print(re.match("[abcdef]","a")) #매치됨
print(re.match("[abcdef]","g")) #매치 안됨
print(re.match("[abcdef]","abc")) #매치됨
print(re.match("[abcdef]","c")) #매치됨
#<re.Match object; span=(0, 1), match='a'>
#None
#<re.Match object; span=(0, 1), match='a'>
#<re.Match object; span=(0, 1), match='c'>

print(re.match('[0-9]','1234')) #앞에서부터 하나만 매치
print(re.match('[0-9]*','1234'))#*은 문자(숫자)가 0개 이상 있으면 매치
print(re.match('[0-9]*','a1234')) # *있으면 0개로 판단, 없으면 none
print(re.match('[0-9]+','1234')) #+는 1개 이상 있으면 매치
print(re.match('[0-9]+','a1234')) #None
print(re.match('a*b','b')) #a가 0개 이상 있고 b가 나오면 매치
print(re.match('a+b','b')) #a가 1개 이상 있고 b가 나오면 매치
print(re.match("a+b", "aaaabb")) #aaaab까지만 매치
print(re.match("hello|world", "hello")) #or의 의미
```

* `search()`

```python
search는 문자열 끝까지 조사

print(re.search("^hello", "hello, world"))
print(re.search("world$", "hello, world"))

```

### match 객체의 메서드

자, 이제 match 메서드와 search 메서드를 수행한 결과로 돌려준 match 객체에 대해 알아보자. 앞에서 정규식을 사용한 문자열 검색을 수행하면서 아마도 다음과 같은 궁금증이 생겼을 것이다.

- 어떤 문자열이 매치되었는가?
- 매치된 문자열의 인덱스는 어디서부터 어디까지인가?

match 객체의 메서드를 사용하면 이 같은 궁금증을 해결할 수 있다. 다음 표를 보자.

| method  | 목적                                                   |
| :------ | :----------------------------------------------------- |
| group() | 매치된 문자열을 돌려준다.                              |
| start() | 매치된 문자열의 시작 위치를 돌려준다.                  |
| end()   | 매치된 문자열의 끝 위치를 돌려준다.                    |
| span()  | 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다. |

다음 예로 확인해 보자.

```
>>> m = p.match("python")
>>> m.group()
'python'
>>> m.start()
0
>>> m.end()
6
>>> m.span()
(0, 6)
```

예상한 대로 결괏값이 출력되는 것을 확인할 수 있다. match 메서드를 수행한 결과로 돌려준 match 객체의 start()의 결괏값은 항상 0일 수밖에 없다. 왜냐하면 match 메서드는 항상 문자열의 시작부터 조사하기 때문이다.

만약 search 메서드를 사용했다면 start() 값은 다음과 같이 다르게 나올 것이다.

```
>>> m = p.search("3 python")
>>> m.group()
'python'
>>> m.start()
2
>>> m.end()
8
>>> m.span()
(2, 8)
```

* grouping

```python

```

### findall

findall 메서드를 수행

```
>>> result = p.findall("life is too short")
>>> print(result)
['life', 'is', 'too', 'short']
```

"life is too short" 문자열의 'life', 'is', 'too', 'short' 단어를 각각 `[a-z]+` 정규식과 매치해서 리스트로 돌려준다.

### finditer

finditer 메서드를 수행

```
>>> result = p.finditer("life is too short")
>>> print(result)
<callable_iterator object at 0x01F5E390>
>>> for r in result: print(r)
...
<_sre.SRE_Match object at 0x01F3F9F8>
<_sre.SRE_Match object at 0x01F3FAD8>
<_sre.SRE_Match object at 0x01F3FAA0>
<_sre.SRE_Match object at 0x01F3F9F8>
```

finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다. 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.

### sub

```python

대한민국, 한국, 코리아 모두 같은 것을 가리키지만 컴퓨터는 다르게 인식한다.
re.sub("패턴","바꿀문자열","문자열",바꿀횟수)
print(re.sub("apple|orange","fruit","apple tree banana orange"))
두줄로 표현
pat=re.compile("apple|orange")
pat.sub("fruit","apple tree banana orange")

"1 2 apple 3 banana 4 7 9 30 tree"
print(re.sub("\d+","num","1 2 apple 3 banana 4 7 9 30 tree"))

```



즉 위 정규식에서 사용한 `\` 문자가 문자열 자체임을 알려 주기 위해 백슬래시 2개를 사용하여 이스케이프 처리를 해야 한다.

따라서 위 정규식을 컴파일하려면 다음과 같이 작성해야 한다.

```
>>> p = re.compile('\\section')
```

그런데 여기에서 또 하나의 문제가 발견된다. 위처럼 정규식을 만들어서 컴파일하면 실제 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 따라 `\\`이 `\`로 변경되어 `\section`이 전달된다.

만약 위와 같이 `\`를 사용한 표현이 계속 반복되는 정규식이라면 너무 복잡해서 이해하기 쉽지않을 것이다. 이러한 문제로 인해 파이썬 정규식에는 Raw String 규칙이 생겨나게 되었다. 즉 컴파일해야 하는 정규식이 Raw String임을 알려 줄 수 있도록 파이썬 문법을 만든 것이다. 그 방법은 다음과 같다.

```
>>> p = re.compile(r'\\section')
```

위와 같이 정규식 문자열 앞에 r 문자를 삽입하면 이 정규식은 Raw String 규칙에 의하여 백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 동일한 의미를 갖게 된다.







## 연습

1.

0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: True False False True False

```python
nums=list(input("번호 10개 입력 : "))
print(len(nums)==10 and len(nums)==len(set(nums)))

+다른 풀이
stnum=list(range(10))
def oncenum(num):
    num=str(num)
    for i in num:
        if int(i) in stnum:
            stnum.remove(int(i))
        else: break
    if len(stnum) == 0:
        return True
    else:return False
print(oncenum(6789012345))

```

2.

emails = [

'python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
    'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
    'python.dojang@e-xample.com',                                    # 올바른 형식
    '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식

```python
import re

right=re.compile('\S+@\S+[.]\w+')#대상이 리스트일때는 compile하고 요소 조사
for i in emails:
    if right.findall(i):
        print(right.findall(i))
    else: print("잘못된 형식")
        
+다른 풀이        
p=re.compile('(.+)[@](\w.+[.]\w+)')
#print(p.match("python@example-com"))
for i in emails:
    if p.match(i):
        print("올바른 형식",p.findall(i))
    else:
        print("잘못된 형식")
```

3.

news="""

연합뉴스TV
[날씨] 추위 대신 미세먼지 말썽…밤까지 중부 중심 눈
기사입력 2021.01.12. 오후 1:40 기사원문 스크랩 본문듣기  설정
화나요 후속기사원해요 좋아요 평가하기9 댓글9
글자 크기 변경하기
 인쇄하기 
보내기
동영상 뉴스
[앵커]

오늘은 추위가 풀리는 대신 서쪽 지역의 공기 질이 나쁘겠습니다.

중부지방을 중심으로 눈도 내리겠습니다.

기상캐스터 연결해서 날씨 정보 더 자세히 알아보겠습니다.

김민지 캐스터.

[캐스터]

네, 추위가 한층 풀렸습니다.

어제보다 옷차림을 조금 더 가볍게 하고 나왔는데도 크게 춥지 않습니다.

내륙에 내려졌던 한파특보는 모두 해제가 됐고요.

오늘 한낮에 전국에 영상권으로 올라서겠습니다.

한낮에 서울은 1도, 대전 3도, 대구 5도 등 어제보다 5도 정도 기온이 높겠습니다.

따뜻한 서풍이 불어오면서 추위의 힘이 약해지는 건데요.

이 서풍을 타고 또 미세먼지가 들어오겠습니다.

대기 정체로 먼지가 쌓이면서 오늘은 서쪽 지역을 중심으로 미세먼지 농도 나쁨 수준 보이겠고요.

밤에 중국발 오염물질까지 들어와서 내일은 전국적으로 공기 질 상황이 나쁘겠습니다.

오늘 전국에 구름이 많습니다.

차츰 중부를 중심으로 눈이 내리겠습니다.

수도권과 충남, 전북에 1~3cm, 강원 영서와 충북, 경북과 제주 산지에 최고 5cm의 눈이 내려 쌓이겠습니다.

대부분 오늘 밤이면 그칠 텐데요.

강원 영서 지역은 내일 새벽까지 눈이 이어지겠습니다.

지금은 눈발 정도만 날리고 있습니다.

눈이 쌓이면서 퇴근길 무렵에는 길이 많이 미끄럽겠습니다.

조심히 이동하시기 바랍니다.

날씨 전해 드렸습니다.
"""

1)[캐스터]가 캐스팅한 내용만 추출하시오
2)달린 댓글의 개수를 출력하시오
3)대전의 온도를 출력하시오
4)가장 많이 등장한 단어가 무엇인가요?
5)가장 많이 등장한 글자는 무엇이며, 총 몇 번 등장했나요? (형태소분석기)

```python
import re

3-1)
cast=re.compile('\[캐스터.*',re.DOTALL)
print(cast.findall(news)[0][len("[캐스터]"):])

3-2)
comment=re.findall('댓글\d+',news)
print("댓글 수 :",comment[0][2:])

3-3)
print("대전 기온 :",re.findall('대전\s\d+',news)[0][2:],"도")

3-4)
words=news.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
counts_max=max(counts.keys(),key=lambda k:counts[k])
print(counts_max,"(이)라는 단어가",counts[counts_max],"번으로 가장 많이 나왔습니다.")



+다른 풀이
3-1)
splits=news.replace('\n',' ').replace('-',' ').split(' ')
lst = [word for word in splits if word!= '']

words_count={}
for word in lst:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
sorted_words=sorted(words_count.items(), key=lambda x: x[1], reverse=True)
print('가장 많이 등장한 단어는 "{0}" 입니다. {1}회 등장했습니다.'.format(sorted_words[0][0],sorted_words[0][1]))


import re
3-2), 3-3)
p=re.compile('\\[캐스터.+',re.DOTALL)
#print(p.findall(news))
print("댓글수:",re.findall("댓글\d",new)[0][2])
print("대전의 온도:",re.findall("대전.{,10}",new)[0][3])

3-4)
p=re.compile('\w+')
res=p.findall(new)
#print(p.findall(new))
#print(type(res))
#print(res[0])
l = []
excount = 0
for i in res:
	newcount = 0
	for j in res:
		if i==j:
			newcount+=1
			l.append((newcount,i))
max1=max(l)[0]
print(l)
print(set([l[i][1] for i in range(len(l)) if l[i][0] >= max1]),":",max1)

3-5)
p=re.compile("[가-힣]+")
print(p.findall(new))
l=p.findall(new)
word=dict()
for j in l:
	for i in j:
		if i in word.keys():
			word[i]+=1
		else:word[i]=0
print(word)
maxnum=max(word.values())
for i in range(len(word.keys())):
	if list(word.values())[i]==maxnum:
		print(list(word.keys())[i],":",maxnum)
        

++다른 풀이
import re
sliced=news.split()
sliced_s=set(sliced)
word_cnt={}
for i in sliced_s:
    word_cnt[i]=sliced.count(i)
    cnt_m=max(word_cnt.values())
for key, value in word_cnt.items():
    if value == cnt_m:
        print("가장 많이 등장한 단어는?", key)


res=re.findall("[ㄱ-ㅎ가-힣a-zA-Z]", news)
from collections import Counter
letters=Counter(res)
max_let=max(letters.values())
for key, value in letters.items():
    if value == max_let:
        print("가장 많이 등장한 글자는?", key)
```





