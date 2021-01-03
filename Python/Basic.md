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
x+=10
#x=20

x*=2
#x=40

x/=5
#x=8

x%=5
#x=3
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

```python
x,y=1,2
x,y=y,x   #x,y 값 바꾸기
print(x,y)   
#2 1
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
print(str.lstrip(","))
print(str.lstrip(", ")) #큰따옴표 안에 제거대상 문자를 나열
print(str.lstrip(" ,."))

print(str.rstrip(" ,."))
#[l|r]strip("삭제대상문자들")
print(str.strip(" ,."))

import string
print((string.punctuation))
#punctuation(구두점) : !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print(str.strip(string.punctuation))
print(str.strip(string.punctuation+" "))

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
```

* 분할

```python
print(s.split()) #공백문자로 분리

print('python'.ljust(10)) #10자리 확보 후 좌측 정렬
print('python'.rjust(10))
print('python'.center(10))


.strip()
print("hi")
print("            hi")
print("hi            ")

print("%10s" % "hi")
print("hello%10s" % "hi")

print("%-10shello" % "hi")

print("%.4f" % 3.141592) #소수 이하 5번째 자리에서 반올림 -> 4번째 자리까지 표현
print("%10.4f" % 3.141592) #10자리를 확보한 다음 출력(우측 맞춤)


South Korea, south korea, SOUTH KOREA,...


#"   대한민국" "대한민국  " "대한민국" ...
n1=" 대한민국"
n2="대한민국  "
n3="  대한민국   "
print(n1.lstrip())
print(n2.rstrip())
print(n3.strip())

chaining 
print('python'.rjust(10))
s='python'.rjust(10)
print(s.upper())

print('python'.rjust(10).upper())

padding:특정값으로 빈자리 채우기
print("hello".zfill(10)) #zero fill
print("345".zfill(10)) #zero fill

s="Life$is$too$short"
print(s.split("$")) #method(=function), class
print('1,2,3'.split(','))

t=str.maketrans('aeiou', '12345')
print('apple'.translate(t)) #apple 문자열을 t변환테이블을 참조하여 변환하세요.
#문자바꾸기
#str.maketrans('바꿀문자', '새문자') 작성하여 변환테이블(t) 생성
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
print("%10s" % "hi") #자리수 지정

%-10s #왼쪽 정렬

%.4f #소수 이하 넷째 자리까지 표현

%10.4f #우측에 10자리 확보 후 소수 이하 넷째 자리까지 표현
```



## 정리해 넣을것



## 함수

* bool() 불리안

```python
print(1==1.0) True #값 비교 
print(1 is 1.0) False #객체 비교
0:False 1:True #그 외 숫자나 텍스트도 참. 빈 문자열은 거짓
```

```python

```



```python

```

```python
map
x1, x2= map(int,  input("숫자 두 개 입력 : ").split())   
#['1', '2']
int함수
[1, 2]
#x1=1, x2=2
print(x1+x2)
#mapping:사상  
x > f > y
입력 : 10 20
30


함수출력=map(함수, 함수입력)
x1,x2=map(int, ['3', '4'])
print(x1+x2)
#7


#입력값을 컴마로 구분
x1, x2= map(int,  input("숫자 두 개 입력 : ").split(","))
#"1,2"-> ['1','2'] -> [1,2] -> x1=1, x2=2
print(x1+x2)

입력 :10,20
#30
```



print(",").join("abcd")



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



## 컬렉션

여러개의 값을 모아서 저장



### 리스트: []

```python
','로 자료 구분하여 순서대로 저장
리스트는 리스트를 포함한 다양한 자료형을 요소값으로 저장 가능

b=[] 
b=list() #빈 리스트 생성

b=[1,2,3]
print(b[0]+b[2])
#4

#'too' 출력
a=[1, 2, ['life', 'is',['too', 'short']]]
print(a[2][2][0])
print(a[-1][-1][-2])
```



#### 리스트 컴프리헨션

```python
문법으로 요소의 집합 정의하기

nums=[n*2 for n in range(1,7)]

nums=[]
for n in range(1,7):
    nums.append(n*2) 
#[2,4,6,8,10,12]

#3의 배수만 취하려면 if문으로 조건 작성
nums=[n*2 for n in range(1,7) if n%3==0]
#[6,12]
```



#### 리스트 슬라이싱

```python
x=[10,20,30,40,50]
print(x[1:4:-1]) #1부터 3번 요소까지 -1간격으로

a=[1,2,3,['x','y','z'],4,5]
print(a[3][:2])
#['x','y']

range(5) #0~5-1까지 숫자를 생성
print(list(range(5)))
print(list(range(3,10))) #3~9까지
print(list(range(3,10,2))) #3~9까지 2간격으로 추출
print(list(range(10,0,-1))) #10에서 1까지 -1간격으로 
```



#### 리스트 연산

```python
a=[1,2]
b=[3,4]
print(a+b)
#[1,2,3,4]
print("ab"+"cd")
#abcd

print(a*3) #[1,2,1,2,1,2] a가 3번 반복
print("ab"*3) #ababab
print(len(a)) #2

print(a[0]+"hi") #에러 발생. 정수와 문자열은 더할 수 없다
print(type(a[0])) #int
print(type("hi")) #str

str(a[0]) # 숫자 1 -> 문자열 "1"
print(str(a[0])+"hi")  => 1hi 출력
#str 함수: 정수나 실수를 문자열로 변환해주는 함수
```



#### 리스트 값 변경

```python
a=[1,2,3]
a[2]=30 
#a=[1,2,30]

a=[0,1,2,3,4,5,6]
a[1:4]=[10,20,30]
#a=[0,10,20,30,4,5,6]
```



#### 리스트 추가, 확장, 삽입(append, extend, insert)

```python
a=[1,2,3]
a+=[4]
a.append(4) #리스트 끝에 요소 추가
#둘다 a=[1,2,3,4]

a.append([5,6,7]) #리스트 추가
#a=[1, 2, 3, 4, [5, 6, 7]]

a+=[5,6,7]
a.extend([5,6,7]) 
#[1,2,3,5,6,7]

a.insert(1,4) # 1번 요소에 4 추가
#a=[1,4,2,3]

nums = [1,2,3,4]
nums[2:2] = [90,91,92] #삽입
#[1,2,90,91,92,3,4]

nums = [1,2,3,4]
nums[2] = [90,91,92] #대체
#[1,2,90,91,92,4]
```



#### 리스트 값 제거(del, remove, pop)

```python
#del : 위치 삭제. 내장함수
a=[10,20,30]
del a[1]
#a=[10,30]

a=list(range(1,10))
del a[:5] #0~4번 index까지 삭제
#a=[6,7,8,9]

#remove : 값 삭제
a=[10,20,30,10,20,30]
a.remove(30) #첫번째 30만 제거, 없는 요소값을 입력하면 에러 발생
a.remove(30) #두번째 30 제거
#a=[10,20,10,20]

a=[10,20,30,40,50]
a[1:4]=[]
print(a)
#[10,50]

#pop : 가장 마지막 위치의 데이터 제거 후 삭제한 요소를 리턴
a=[10,20,30]
print(a.pop())
#[30] 
a.pop()
#a=[10]
```



#### 리스트 정렬

```python
a=[3,5,6,2]
a.sort() #오름차순
a.reverse() #뒤집기
a.sort(reverse=True) #내림차순

단, 이렇게 출력하면 안됨
print(a.sort()) 
#None

#sorted는 정렬된 새로운 리스트를 만들어 리턴하므로 별도의 변수 대입
b=[3,7,8,5]
b2=sorted(b)
print(b2)
#[3,5,7,8]
```



### 튜플: ()

튜플에 저장된 각각의 인수들을 요소라고 한다.

변수를 여러개 쓰면 튜플 내의 값들에 순서대로 저장됨.

```python
ex1, ex2 = divmod(9,4)
#ex1은 2, ex2는 1이 저장됨
```



### 딕셔너리,셋: {}