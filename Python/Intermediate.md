# Intermediate



## 반복문

### for

```python
for 변수 in 컬렉션(리스트, 튜플, 문자열):
    명령
```

* 연습

```python
for i in [(1,2),(3,4),(5,6)]:
    print(i)
#각 튜플이 i가 됨
for i,j in [(1,2),(3,4),(5,6)]:
    print(i)
    print(j)
#튜플의 요소가 i,j가 됨

for i in range(3,10,2):
    print(i)
#3 5 7 9

#구구단 2~9단 표현
for dan in range(2,10):
    for i in range(1,10):
        print(dan*i, end=" ")
    print("") #줄바꿈
   
#중복 숫자를 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a2=[]
for i in a:
    if i not in a2:
        a2.append(i)
print(a2)
#혹은 set(a)

#1부터 100까지 출력
for a in range(1,101):
   print(a)

#소수 출력
for i in range(2,101):
    boolean=True
    for j in range(2,i+1):
        if i%j==0:
            boolean=False
            break
    if boolean:
        print(i, end=' ')
#_간략히
for i in range(2,101):
    for j in range(2,i+1):
        if i%j==0:
            break
    if i==j:
        print(i, end=' ')
#_제곱근으로 최적화


     
#평균 구하기
score=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
for s in score:
    sum+=s
print(sum/len(score))


#로또 당첨 번호 제작
import random

for i in range(1,7):
    num=random.randint(1,45)
    print(num,end=" ")
#중복된 수가 나오면 수가 5개만 나올 수도 있음
#while로 무한루프 돌려서 길이가 6이 되는순간 빠져나가도록
num=set()
while len(num) <6:
    nums=random.randint(1,45)
    num.add(nums)
print(num,end=" ")
#중복 안되게   
print('당첨 번호 : ',random.sample(range(1,45),6))

```



### while

```python
while 조건:
    명령
```

* 연습

```python
i=0
while i<10:
    i=i+1
    print(i,"번째 반복 수행")
    if i>10:
        break #반복문 빠져나가기
        
prompt="""
1.취소
2.입력
3.종료
입력 :
"""

a=0
while a<10:
    a=a+1
    if a%2==0:continue #while의 시작위치로 이동
    print(a)
#1
#3
#5
#7
#9

#1~100사이의 자연수 중 4의 배수의 합 출력
num=1
sum=0
while num<=100:
    if num % 4 == 0:
        sum=sum+num
    num += 1
print(sum)
------------------or-------------------
num=0
sum=0
while num<100:
    num += 1
    if num % 4 == 0:
        sum=sum+num
print(sum)

#1부터 1000까지의 자연수 중 3의 배수이면서 7의 배수의 합
num=0
sum=0
while num<1000:
    num+=1
    if num%3==0 and num%7==0:
        sum+=num
print(sum)


자판기(pro, 커피 한 잔에 300원이라 가정, 초기 커피는 10개)
돈을 넣어 주세요: 500
거스름돈 200를 주고 커피를 줍니다.
돈을 넣어 주세요: 300
커피를 줍니다.
돈을 넣어 주세요: 100
돈을 다시 돌려주고 커피를 주지 않습니다.
남은 커피의 양은 8개입니다.
돈을 넣어 주세요: 0
종료합니다

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money-300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("종료합니다")
        break

```

#### 삼각형 그리기

```python
#삼각형 그리기

*
**
***
****
*****

1) while 루프
x=0
while x<5:
    x+=1
    print('*'*x)

2) while 루프
x=0
y=0
while x<5:
    x+=1
    y=0
    while y<x:
        y+=1
        print("*",end='')
    print()

3) for 루프
for i in range(5):
    for j in range(i+1):
        print('*', end = '')
    print() #한 줄이 끝나면 새 줄로 바꿈


     *
    **
   ***
  ****
 *****

1) while 루프
y=5
while y>0:
    y-=1
    print(" "*y+"*"*(5-y))

2) for 루프
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()


     *
    ***
   *****
  *******
 *********

1) while 루프
z=0
while z<10:
    z+=1
    if z%2==0:continue
    print(' '*((9-z)//2)+'*'*(z))

2) for 루프
for i in range(1,6):
    for j in range(6-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
```





## 함수

* bool() 불리안

```python
print(1==1.0) True #값 비교 
print(1 is 1.0) False #객체 비교
0:False 1:True #그 외 숫자나 텍스트도 참. 빈 문자열은 거짓

a=[4,5]
a=b
print(a is b) #a와 b가 가리키는 메모리상의 대상이 동일한가
#True

a=[1,2]
b=[1,2] 
print(a is b) #False
print(a==b) #True

#a 변수 값을 가진 다른 주소(c) 만들기
a=[2,4,6]
c=a[:]
print(a is c) #False
print(a==c) #True

from copy import copy #모듈에서 함수 가져오기
c=copy(a)
print(a is c) #False
print(a==c) #True
```

* `input()`

```python
a,b = input("두 수 입력 :").split()
#split앞에 있는 문자열을 공백으로 분리

a,b=(input("숫자 두 개 입력 : ").split())
print(int(a)+int(b))

a,b=map(int,input("숫자 두 개 입력 : ").split())
print(a+b)
```



### 사용자 함수 `def` 

```python
def 매개변수(인수목록):
	함수 정의 구문
함수 호출 구문
 
#입력값이 없는 함수
def say():
    return "안녕"
s=say()
print(s)

#출력값이 없는 함수
def add(a,b):
    print("두 수의 합 :",a+b)
res=add(3,4)

#입력값/출력값이 없는 경우
def say():
    print("안녕")
    #return 생략
say()

#매개변수의 초기값을 설정하여 함수 호출
def add(a,b):
    return a+b
res=add(b=2,a=3)
print(res)

def add(a,b=3):
    print(b)
    print(a)
    return a+b
res=add(2) #인수 하나만 넣어도 b가 초기값 정해져있어서 에러안남
print(res)

#함수로 전달되는 인수의 개수가 정해져 있지 않은 경우
def add(*arg): #매개변수명 앞에 * 붙이면 튜플로 인식
    res=0
    for i in arg:
        res+=i
    return res
r=add(1,2,3)
print(r)

def am(a,b):
    return a+b, a*b #return문 쓰면 함수 종료 return 하나 더 써도 무시
r1,r2=am(3,4)
print(r1)
res=am(3,4)
print(res[0])
print(res)
#(7,12) #함수의 결과는 항상 1개. 튜플 형식으로 (덧셈, 곱셈) 리턴

#addmul(add/mul 뒤에 가변 인수)
def addmul(op,*arg):
    if op=="add":
        res=0
        for i in arg:
            res+=i
    elif op=="mul":
        res=1
        for i in arg:
            res*=i
    return res
r=addmul("add",1,2,3,4)
print(r)
#10

#기본값 매개변수(non-default parameter)는 제일 뒤에 두기(True/False)
def say(name,age,male=True): 
    print("내 이름은",name)
    print("나이는",age)
    if male:
        print("성별은 남")
    else:
        print("성별은 여")
say('홍길동',25,False)

a=1 #함수 밖에 있는 a
def mytest(a): #함수 안에서만 사용되는 a
    a+=1
mytest(a)
print(a)
#1 처음에 정의해준 a값
```

* 