



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

모듈은 코드를 작성해 놓은 스크립트 파일로 함수, 변수, 클래스 등이 정의되어 있다. 

```python
import #모듈 전체를 불러냄
import as a #모듈 별명 지정
from 모듈 import 함수명 #모듈 함수를 지정해 같은 함수가 다른 모듈에 있어도 충돌x
함수를 직접 임포트 했으므로 모듈명. 안붙여도 됨
```



## 표준 모듈

표준 모듈은 파이썬의 일부는 아니지만 같이 설치되어 표준 라이브러리에서 자유롭게 사용 가능하다.

```python

#os 모듈:디렉토리, 파일의 경로 등 확인/제어
import os
print(os.environ)

print(os.getcwd()) # 현재 작업 경로
#os.mkdir("sample") #현재 작업 위치에 폴더 생성
#os.rmdir("sample")
#os.rename("sample", "test") #폴더명 변경
#os.renames("hello.txt", "hi.txt")

import shutil
shutil.copy("hi.txt", "hicopy.txt") #파일 복사

#특정 폴더 내에 있는 폴더 또는 파일 목록 등을 조사
import glob
#모든 파일 목록 출력
#print(glob.glob("C:/Users/i/PycharmProjects/pythonBasic/*"))

#파일 확장자가  py인 파일들을 출력
print(glob.glob("C:/Users/i/PycharmProjects/pythonBasic/*.py"))

```



### 피클(pickle) 

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