



```
입출력 종류 : 표준, 파일, 네트워크
```



# 파일



## 파일 입출력

`open( )`: 파일 열기

`read()/write()` : 파일 입력/출력

`close()`: 파일 닫기

| 모드 | 설명                                          |
| ---- | --------------------------------------------- |
| r    | 파일을 읽는다. 파일이 없으면 예외가 발생한다. |
| w    | 파일에 기록한다. 파일이 이미 있으면 덮어쓴다. |
| a    | 파일에 데이터를 추가한다.                     |
| x    | 파일에 기록하되 파일이 이미 있으면 실패한다.  |



```python
f=open("hello.txt", "r")
s=f.read()
print(s)
f.close()
#파일을 연속적으로 사용할 때는 꼭 닫아야 한다.

#with 블록으로 자동으로 닫을 수 있다. 파일 입출력시 편함.
with open("hello.txt", "w") as f:
	for i in range(10):
		f.write("hello world {0}\n".format(i+1))
        
#read함수는 1글자씩 읽어들임        
with open("hello.txt", "r") as f:
    s=f.read() 
    print(s)
    
#readline함수는 1줄씩 읽어들임(for 또는 while 문과 함께 사용)   
with open("hello.txt", "r") as f:
    line=None
    while True: #while line !=""
        line=f.readline() 
        print(line) #2줄이 바뀜
        print(line.strip("\n")) 
print(line) #\n을 삭제
#왜 계속 실행됨?

#readlines함수는 전체 한꺼번에 읽음
with open("hello.txt", "r") as f:
    line=f.readlines()
#   for i in range(len(line)):
    for i in line:
        print(i.strip("\n"))
        
#리스트의 내용을 파일에 출력
lines=['hello\n', 'nicetomeetyou\n', 'bye\n']
with open("hello.txt", "w") as f:
    f.writelines(lines)
    
#추가
f=open("hello.txt", "a")
for i in range(3):
    f.write("%d번째 줄 추가\n" % (i+1))
f.close()
```





# 모듈

: 코드를 작성해 놓은 스크립트 파일로 함수, 변수, 클래스 등이 정의되어 있다. 

```python
import #모듈 전체를 불러냄
import as a #모듈 별명 지정
from 모듈 import 함수명 #모듈 함수를 지정해 같은 함수가 다른 모듈에 있어도 충돌x
함수를 직접 임포트 했으므로 모듈명. 안붙여도 됨
```



## 파일 관리 모듈

```python
os 모듈 : 디렉토리, 파일의 경로 등 확인/제어
import os

print(os.environ)

print(os.getcwd()) # 현재 작업 경로
#os.mkdir("sample") #현재 작업 위치에 폴더 생성
#os.rmdir("sample")
#os.rename("sample", "test") #폴더명 변경
#os.renames("hello.txt", "hi.txt")

import shutil
shutil.copy("hi.txt", "hicopy.txt") #hi.txt를 복사하여 hicopy.txt 만든다.

#특정 폴더 내에 있는 폴더 또는 파일 목록 등을 조사
import glob
#모든 파일 목록 출력
#print(glob.glob("C:/Users/i/PycharmProjects/pythonBasic/*"))

#파일 확장자가  py인 파일들을 출력
print(glob.glob("C:/Users/i/PycharmProjects/pythonBasic/*.py"))
```

### 파일 관리 

| 함수                 | 설명                             |
| -------------------- | -------------------------------- |
| shutil.copy(a,b)     | 파일 복사                        |
| shutil.copytree(a,b) | 디렉토리 복사(서브 디렉토리까지) |
| shutil.move(a,b)     | 파일 이동                        |
| shutil.rmtree(path)  | 디렉토리 삭제                    |
| os.rename(a,b)       | 파일 이름 변경                   |
| os.remove(f)         | 파일 삭제                        |
| os.chmod(f,m)        | 파일 퍼미션 변경                 |
| shutil.chown(f,u,g)  | 파일 소유권 변경                 |
| os.link(a,b)         | 하드 링크 생성                   |
| os.symlink(a,b)      | 심볼릭 링크 생성                 |

### 디렉토리 관리 

| 함수          | 설명                             |
| ------------- | -------------------------------- |
| os.chdir(d)   | 현재 디렉토리 변경               |
| os.mkdir(d)   | 디렉토리 생성                    |
| os.rmdir(d)   | 디렉토리 제거                    |
| os.getcwd()   | 현재 디렉터리 조사               |
| os.listdir(d) | 디렉토리의 내용 나열             |
| glob.glob(p)  | 패턴과 일치하는 파일의 목록 나열 |
|               |                                  |

### os.path 모듈

: 디렉토리의 경로를 조사하고 조작

| 함수                | 설명                    |
| ------------------- | ----------------------- |
| os.path.isabs(f)    | 절대 경로인지 조사      |
| os.path.abspath(f)  | 파일의 절대 경로 구하기 |
| os.path.realpath(f) | 원본 파일의 경로 구함   |
| os.path.exists(f)   | 파일의 존재 여부 조사   |
| os.path.isfile(f)   | 파일인지 조사           |
| os.path.isdir(f)    | 디렉토리인지 조사       |



## 피클(pickle) 

 : 파이썬 객체를 파일로 저장하고자 할때 사용하는 모듈

```python
피클링 : 객체 -> 파일
언피클링 : 파일 -> 객체
    
#객체를 파일로 저장
import pickle
내용물="단팥"
색상="파랑"
너비="20cm"
가족명단={'잉어':30,'게':10,'문어':40}
#객체 저장할때는 wb 모드로 파일 열기
with open ("myfish.p","wb") as f:
    pickle.dump(내용물, f)
    pickle.dump(색상, f)
    pickle.dump(너비, f)
    pickle.dump(가족명단, f)

with open ("myfish.p","rb") as f:
    내용물=pickle.load(f)
    색상 = pickle.load(f)
    너비 = pickle.load(f)
    가족명단 = pickle.load(f)
#저장된 순서와 읽어들이는 순서가 일치해야함
    print(내용물)
    print(색상)
    print(너비)
    print(가족명단)

```



## 표준 모듈

: 표준 모듈은 파이썬의 일부는 아니지만 같이 설치되어 표준 라이브러리에서 자유롭게 사용 가능하다.



### math

: C 표준 라이브러리를 랩핑한 것으로 C만큼 속도 빠름. 대부분 float 리턴

| 상수 | 설명                                           |
| ---- | ---------------------------------------------- |
| pi   | 원주율 상수. 지름과 원둘레의 비율              |
| tau  | 원주율의 2배 되는 상수. 반지름과 원둘레의 비율 |
| e    | 자연 대수 상수                                 |
| inf  | 무한대                                         |
| nan  | 숫자가 아닌 값                                 |



| 함수                                  | 설명                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| sqrt(x)                               | x의 제곱근. 세제곱근은 1/3승                                 |
| pow(x,y)                              | x의 y승. **연산자와 같지만 인수를 모두 실수로 바꾸고 연산함. |
| hypot(x,y)                            | 피타고르사의 정리. x^2+y^2의 제곱근                          |
| factorial(x)                          | x의 계승. 인수 x는 양의 정수만 가능                          |
| sin(x), cos(x), tan(x)                | 삼각함수. x는 라디안 값                                      |
| asin(x), acos(x), atan(x), atan2(y,x) | 역삼각함수                                                   |
| sinh(x), cosh(x), tanh(x)             | 쌍곡선 삼각함수                                              |
| asinh(x), acosh(x), atanh(x)          | 쌍곡선 역삼각함수                                            |
| degrees(x)                            | 라디안 값을 각도로 바꾼다                                    |
| radians(x)                            | 각도를 라디안 값으로 바꾼다.                                 |
| ceil(x)                               | 수직선 오른쪽의 올림값                                       |
| floor(x)                              | 수직선 왼쪽의 내림값                                         |
| fabs(x)                               | x의 절대값                                                   |
| trunc(x)                              | x의 소수점 이하 버리기                                       |
| log(x,base)                           | base에 대한 x의 로그. 생략하면 자연 로그                     |
| log10(x)                              | 10의 로그. log(x,10)과 같음                                  |
| gcd(a,b)                              | a,b의 최대공약수                                             |



### statistics

| 함수           | 설명                           |
| -------------- | ------------------------------ |
| mean           | 평균                           |
| harmonic_mean  | 조화평균                       |
| median         | 중앙값. 짝수면 보간 값         |
| median_low     | 중앙값. 집합 내의 낮은 값 선택 |
| median_high    | 중앙값. 집합 내의 높은 값 선택 |
| median_grouped | 그룹 연속 중앙값               |
| mode           | 최빈값                         |
| pstdev         | 모표준편차                     |
| stdev          | 표준편차                       |
| variance       | 분산                           |



### time

:1970년 1월 1일 자정을 기준으로 경과한 시간(에폭 시간/유닉스 시간)을 초 단위로 표현

```python
import time

t=time.time()
print(t) #1610812581.4471073
print(time.ctime(t)) #Sun Jan 17 00:56:21 2021

print(time.localtime(t)) #세계표준시간인 UTC로 구하려면 gmtime()
#time.struct_time(tm_year=2021, tm_mon=1, tm_mday=17, tm_hour=0, tm_min=57, tm_sec=34, tm_wday=6, tm_yday=17, tm_isdst=0)
#에폭시간을 인수로 주면 시간 요소를 멤버로 가지는 struct_time형의 객체 리턴

우리나라 말로 쓰기
now=time.localtime()
print("%d년 %d월 %d일" % now.tm_year, now.tm_mon, now.tm_mday)
#2021년 1월 17일

#멤버 이름이 더 짧고 직관적인 datetime 모듈
import datetime

now=datetime.datetime.now()
print("%d년 %d월 %d일" % (now.year, now.month, now.day))
```

* 실행시간 측정

  ```python
  import time
  
  start=time.time()
  for a in range(1000):
      print(a)
  end=time.time()
  print(end-start)
  ```

* sleep :실행속도 늦춤

  ```python
  import time
  
  print("안녕")
  time.sleep(1)
  print("좀 기다려")
  time.sleep(5)
  print("잘했어")
  ```

* calendar

  ```python
  import calendar
  
  calendar.prcal(2021) #무조건 출력해야하므로 pr이 아예 합쳐져있음
  calendar.prmonth(2021,2)
  
  #default는 월요일이 첫번째
  calendar.setfirstweekday(6) #일요일이 첫번째
  
  #2021년 광복절 요일 알아내기
  import calendar
  
  yoil=['월','화','수','목','금','토','일']
  day=calendar.weekday(2021,8,15)
  print("2021년 광복절은",yoil[day]+"요일이다.")
  ```



### random

: 0-1 미만의 실수 무작위로 생성

```python
import random

정수 난수
randint(begin,end) #end도 범위에 포함
randrange(begin,end) #end-1까지

실수 난수
random.uniform(begin,end)

리스트에서 랜덤으로 뽑기
food=['아이스크림','초코','식빵','바나나']
print(random.choice(food))
> choice함수 구현
> i=random.randrange(len(food))
> return food[i]

리스트 요소 섞기
print(random.shuffle(food))

리스트 항목 n개 무작위로 뽑아 새로운 리스트 만들기
print(random.sample(food,n))

로또 번호 생성기. (중복 없이 골라주기)
nums=random.sample(range(46),6)
nums.sort()
print(nums)
```



### sys

:파이썬 해석기가 실행되는 환경과 기능을 조회하고 관리

```python
import sys

sys.version #파이썬 버전
sys.platform #win32
sys.getwindeowsversion() #sys.getwindowsversion(major=10, minor=0, build=18363, platform=2, service_pack='')
sys.byteorder
sys.path
sys.exit(0) #프로그램 종료

```









# 클래스



```python
클래스==붕어빵기계
객체==붕어빵
메서드(동작)==굽는다,...뒤집는다, ...
attribute(속성)==내용물, 크기, 모양,...너비, 높이

res=0
def add(n):
    global res
    #n에 전달된 값을 res에 저장
    res+=n

add(3)
print(res)
add(4)
print(res)


res1=0 #전역변수
res2=0
#편의점->계산대->계산기 2대->

#1번째 계산대
def add1(n): #지역변수
    global res1
    #n에 전달된 값을 res에 저장
    res1+=n
    #res=res*0.9
    return res1
print(add1(3000))
print(add1(5000))

#2번째 계산대
def add2(n): #지역변수
    global res2
    #n에 전달된 값을 res에 저장
    res2+=n
    return res2
print(add2(1500)) #막걸리
print(add2(2000)) #두부

클래스 : 각각의 계산대를 객체로 간주하고, 계산대의 특성 또는 동작등을 일반화시켜 놓은 틀
정/부정관사
the car(객체)
a car(클래스)

사람(클래스): 실체가 없음
사람홍길동(객체), 사람임꺽정(객체) : 실체가 있음

자동차(클래스) : 실체가 없음
내자동차(객체), 네자동차(객체)

class Calculator: #클래스명은 대문자로 시작, 붕어빵기계
    def __init__(self): #현재 객체를 self라고 함
        self.res=0
        print("init함수가 호출됐네?")
    def add(self, n):
        self.res+=n
        #10%할인 코드를 여기에 작성-> 모든 계산대에 공통적으로 적용
        return self.res

Calculator():붕어빵기계에서 붕어빵을 제작 -> __init__자동호출 ->res(내용물)=msg
cal1=Calculator() #클래스로부터 객체를 생성(init 함수 자동 호출, res=0으로 초기화). 계산대(클래스)로부터 계산대1(객체==cal1)을 생성
#Calculator():붕어빵기계에서 붕어빵을 제작 -> __init__자동호출 ->res(내용물)=msg
cal2=Calculator()#클래스로부터 객체를 생성(init 함수 자동 호출). 계산대(클래스)로부터 계산대2(객체==cal2)을 생성

print(cal1.add(3000)) #붕어빵.크기(20)    크기를 20으로...
print(cal1.add(5000)) #붕어빵.너비(10)   너비를 10으로

print(cal2.add(1500))
print(cal2.add(2000))

객체지향프로그래밍





모듈==변수, 함수, 클래스 등을 모아 놓은 파이썬 파일. 다른 프로그램에서 모듈을 불러올 수 있음
```