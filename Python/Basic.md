# Basic

* 참고 서적 : 파이썬 정복 by 김상형

* Pycharm 설치하기



## 연산자

* `a//b` : 소수 이하 버림
* `a % b` : 나머지
* `a ** b` : 거듭제곱
* `divmod(a,b)` : a(피젯수)를 b(젯수)로 나눈 몫과 나머지
* `==` : 같다
* `!=` : 다르다
* `x+=10` : x=x+10 축약형

```python
x=10
x*=2
#20
x/=5
#4
x%=3
#1

논리연산자
and 모두다
or 하나만
not 반대로
```





## 기본 구조



### 출력

```python
print(출력 내용 [, sep = 구분자] [, end = 끝 문자])
#[]는 생략 가능
```



* print 여러개 이어 쓰려면 `;`로 연결

  ```python
  >>>print('안녕');print('하세요')
  안녕
  하세요
  ```

  

* print 두개 붙여 출력하려면 `end = ''`

  ```python
  >>>print('안녕', end='');print('하세요')
  안녕하세요
  ```



### 입력

```python
변수 = input('질문 내용')
```



### 변수

* 파이썬은 변수 설정이 편리하다.

```python
a,b,c = 1,2,3 #변수와 값의 개수가 같아야 한다
```

* `a=None` : 변수만 만들고 값을 저장하지 않을때

* `a=''` : 변수 값이 공백

- `del a` : 변수 a 삭제
- 변수 교환, 전역변수

```python
x,y=1,2
x,y=y,x   #x,y 값 바꾸기
print(x,y)   
#2 1

res=3
def add(n):
    global res
    #n에 전달된 값을 res에 저장
    res+=n

add(3)
print(res)
#6
```





## 타입

`str()` : 문자열로 변환

`int()` : 문자열을 정수로 변환(두번째 인수로 진법 지정)

`float()` : 실수로 변환



### 진수

| 진법   | 접두 | 사용 가능한 숫자 | 예     | print 명령 |
| ------ | ---- | ---------------- | ------ | ---------- |
| 16진법 | 0x   | 0~9,a~f          | 0x2f   | hex()      |
| 8진법  | 0o   | 0~7              | 0o17   | oct()      |
| 2진법  | 0b   | 0,1              | 0b1101 | bin()      |



### 확장열

* `\n` : 줄 바꾸기
* `\t` : 띄어쓰기(탭)
* `\"` : 큰따옴표 넣기
* `\'` : 작은따옴표 넣기
*  `\\` : \ 넣기
* 확장열 무효는 문자열 앞에 r 넣기  `r''`



#### 긴 문자열

```python
s = """엄청나게 길어서 한 줄에 다 쓸 수 없는 긴 문자열이라서 
중간에 개행되더라도 다음 큰따옴표 3개를 만날 때까지 
하나의 문자열로 정의한다."""
#개행, 띄어쓰기가 문자열의 일부로 포함됨

s = "엄청나게 길어서 한 줄에 다 쓸 수 없는 \
긴 문자열이라서 다음줄로 내려 쓰더라도 \
이후 줄이 하나의 문자열로 정의된다."
#코드의 가독성을 높인다
```



## 문자열 



### 문자열 전처리

* 변경

```python
.upper()
.lower()
.swapcase()
.capitalize()
.title()

.strip()
str=", python,."
print(str.lstrip(",")) 
# python,.
print(str.lstrip(", ")) #큰따옴표 안에 제거대상 문자 나열
#python,.
print(str.lstrip(" ,."))
#python,.
print(str.rstrip(" ,."))
#, python
print(str.strip(" ,."))
#python

import string
print((string.punctuation))
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(str.strip(string.punctuation)) #특수문자 다 걸러냄
print(str.strip(string.punctuation+" ")) #공백포함

```

* 검색

```python
a="hello"
print(a.count("l"))
#2
print(len(a))
#5
print(a.find('l')) 
#2
print(a.find('x')) 
#-1
print(a.rfind('l'))
#3
print(a.index('l'))
#2
print(a.index('x'))
#에러
print(a.rindex('l'))
#3

```

* 조사

```python
print('l' in a)
#True
print(a.startswith("h"))
#True
isalpha
islower
isupper
isspace
isalnum
isdecimal
isdigit
isnumeric
isidentifier
ispritable
```

* 문자열 삽입

```python
print(",".join("abcd"))
#a,b,c,d
print(",".join(['a','b','c','d']))
#a,b,c,d
#리스트 각각의 문자들이 컴마와 결합하여 하나의 문자열("a,b,c,d")이 됨
print("".join(['a','b','c','d'])) 
#abcd
```

* 치환 

```python
s="Life is too short"
print(s.replace("Life","Your leg")) #대소문자 구분
#Your leg is too short

변환테이블(t) 생성
t=str.maketrans('aeiou', '12345')
print('apple'.translate(t)) 
#1ppl2

문자열 폭 지정 후 글자 배치
print('python'.rjust(10))
#    python
s='python'.rjust(10)
print(s.upper())
#    PYTHON
print('python'.center(10).upper())
#  PYTHON  

padding:특정값으로 빈자리 채우기
print("hello".zfill(10)) 
print("345".zfill(10)) 
#00000hello
#0000000345
```

* 분할

```python
print(s.split()) #공백문자로 분리

s="Life$is$too$short"
print(s.split("$")) 
#['Life', 'is', 'too', 'short']
print('1,2,3'.split(','))
#['1', '2', '3']
```

* 정렬

```python
print('python'.ljust(10)) #10자리 확보 후 좌측 정렬
print('python'.rjust(10))
print('python'.center(10))
```





### 슬라이싱

```python
[begin:end:step] #끝자리는 포함 안함. 음수는 뒤에서부터
```



### 포매팅

문자열 사이사이에 다른 정보를 삽입하여 조립하는 기법

| 표식 | 설명      |
| ---- | --------- |
| %d   | 정수      |
| %s   | 문자      |
| %f   | 실수      |
| %%   | 퍼센트    |
| %c   | 문자 하나 |
| %h   | 16진수    |
| %o   | 8진수     |



```python
#문자열 뒤에 % 연산자와 표식 위치에 들어갈 값을 밝힌다.

x = 5
y = "apples"
print("I eat %d %s" % (x, y))

x="five"
d=2
per=30
print("I eat %s eggs every %d days for %d%% chance" % (x,d,per))
#I eat five eggs every 2 days for 30% chance
```



- format 메서드로도 가능

<img src="Basic.assets/image-20201230105809957.png" alt="image-20201230105809957" style="zoom:80%;" />



```python
#자리수 지정
%[-]폭[.유효자리수]서식

print("%10s" % "hi") 
#        hi
print("hello%10s" % "hi")
#hello        hi
print("%-10shello" % "hi")
#hi        hello      

%-10s #왼쪽 정렬
%.4f #소수 이하 넷째 자리까지 표현
%10.4f #우측에 10자리 확보 후 소수 이하 넷째 자리까지 표현
```



## if 조건문

```python
x=1
if x==1:
    pass #코드를 수행하지 않고 넘어감
print(x)

in : 검사 
print('h' in "hello")
#True

elif : 조건이 여러개일때
money=6500
if money>=20000:
    print("taxi")
elif money>=10000:
    print("bus")
elif money>=5000:
    print("walk")
#walk
```

* 변수의 논리값

  | 타입                   | 참                  | 거짓    |
  | ---------------------- | ------------------- | ------- |
  | 숫자                   | 0이 아닌 숫자       | 0       |
  | 문자열                 | 비어 있지 않은 상태 | ""      |
  | 리스트, 튜플, 딕셔너리 | 비어 있지 않은 상태 | 빈 상태 |

* 논리 연산자

  | 연산자 | 설명                       |
  | ------ | -------------------------- |
  | or     | 두 조건 중 하나라도 참이다 |
  | not    | 조건을 반대로 뒤집는다     |
  | and    | 두 조건이 모두 참이다      |

  


## 함수

```python
※ 내장 함수랑 객체 소속의 메서드는 호출 방식 다름
len(s) #내장 함수
s.find('a') #메서드

외장함수 : 별도로 적재를 해야 하는 함수
import random
print(random.random())  #난수 발생
#모듈명.함수명()
print(random.randint(1,10))
```

* `map()`

```python
함수출력=map(함수, 함수입력)
x1,x2=map(int, ['3', '4'])
print(x1+x2)
#7

x1, x2= map(int,  input("숫자 두 개 입력 : ").split())   
입력 : 1 2
#['1', '2']
#[1,2]
#x1=1, x2=2 #type==int
print(x1+x2)
#3

#컴마로 구분
x1, x2= map(int,  input("숫자 두 개 입력 : ").split(","))
입력 : 1,2
#['1','2']
#[1,2]
#x1=1, x2=2
print(x1+x2)
#3
```



