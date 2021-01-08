
# 함수는 호출해야만 수행
# 1)add(1,2) 호출
# 2)add 함수 수행->sum 리턴
# 3)sum이 res에 저장
#
# 입력값이 없는 함수
# def say():
#     return "안녕"
# s=say()
# print(s)
#
# #출력값이 없는 함수
# def add(a,b):
#     print("두 수의 합 :",a+b)
# res=add(3,4)
#
# #입력값/출력값이 없는 경우
# def say():
#     print("안녕")
#     #return 생략
# say()
#
# #매개변수의 초기값을 설정하여 함수 호출
# def add(a,b):
#     return a+b
# res=add(b=2,a=3)
# print(res)
#
# def add(a,b=3):
#     print(b)
#     print(a)
#     return a+b
# res=add(2) #인수 하나만 넣어도 b가 초기값 정해져있어서 에러안남
# print(res)

# #함수로 전달되는 인수의 개수가 정해져 있지 않은 경우
# def add(*arg): #매개변수명 앞에 * 붙이면 튜플로 인식
#     res=0
#     for i in arg:
#         res+=i
#     return res
# r=add(1,2,3)
# print(r)
#
# def mul(*arg):
#     res=1
#     for i in arg:
#         res*=i
#     return res
# multi=mul(1,2,3,4)
# print(multi)

# #addmul(add/mul 뒤에 가변 인수)
# def addmul(op,*arg):
#     if op=="add":
#         res=0
#         for i in arg:
#             res+=i
#     elif op=="mul":
#         res=1
#         for i in arg:
#             res*=i
#     return res
#
# r=addmul("add",1,2,3,4)
# print(r)
#
# def am(a,b):
#     return a+b, a*b #return문 쓰면 함수 종료 return 하나 더 써도 무시
# r1,r2=am(3,4)
# print(r1)
# res=am(3,4)
# print(res[0])
# print(res)
# #(7,12) #함수의 결과는 항상 1개. 튜플 형식으로 (덧셈, 곱셈) 리턴

# def prn(a):
#     if a=="안녕":
#         return
#     print("반가워")
# prn("잘있었니?")
#
# def say(name,age,male=True):
#     print("내 이름은",name)
#     print("나이는",age)
#     if male:
#         print("성별은 남")
#     else:
#         print("성별은 여")
# say('홍길동',25,False)

# a=1 #함수 밖에 있는 a
# def mytest(a): #함수 안에서만 사용되는 a
#     a+=1
# print(mytest(a)) #None
# print(a)
#1 처음에 정의해준 a값
# #안에서 밖에 있는 변수 증가시키기
# 1. return
# a=1
# def mytest2(a):
#     a+=1
#     return a
# a=mytest2(a)
# print(a)
#
# 2.global
# a=1
# def mytest3():
#     global a
#     a+=1
# mytest3()
# print(a)

# def myadd(a,b):
#     return a+b
#를 람다로 바꾸면
# myadd2=lambda a,b:a+b

# def mymax(*arg):
#     m=0
#     for i in range(len(arg)):
#         if m<arg[i]:
#             m=arg[i]
#     return m
#
# print(mymax(3,5,8,9))

#람다 함수 자체 호출
# print((lambda x:x+10)(1))
# print((lambda x,y:x+y)(1,2))

#람다 함수 내에서는 변수를 생성할 수 없다
# print((lambda x:y=2;x+y)(1)) #에러
# y=2
# print((lambda x:x+y)(1))
# print((lambda x,y=3:x+y)(1))

#map의 인수에 간단한 함수를 적용하고자 하는 경우
# [1,2,3] 에 10을 더해 [11,12,13] 만들기
# def pt(x):
#     return x+10
# print(list(map(pt,[1,2,3])))
#map(함수, 데이터)

#람다표현식
# print(list(map(lambda x:x+10,[1,2,3])))

#매개변수가 없는 함수 표현
# print((lambda : 1)())

fl=['test.c','test2.h','sample.py','sample2.c']
# for i in fl:
#     prg=i.split('.')
#     if prg[1]=='c' or prg[1]=='h':
#         print('.'.join(prg))
#
# def file_a(alist):
#     for i in fl:
#         if alist[-1] =='c' or 'h':
#             print(i)

# file_a(fl)

#연습문제
# 1. 리스트에서 20 보다 작은 3의 배수를 출력하라
#
list = [13, 21, 12, 14, 30, 18]
# 12
# 18
#
for i in list:
    if i<20 and i%3==0:
        print(i)

# 2. 리스트에서 세 글자 이상의 문자를 화면에 출력하라
#
list = ["I", "study", "python", "language", "!"]
# study
# python
# language

for i in list:
    if len(i)>=3:
        print(i)
#
# 3. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라.
list = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
for i in list:
    name=i.split('.')
    print(name[0])

# 4. my_list를 아래와 같이 출력하라.
#
my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라
for i in range(1,len(my_list)):
    print(my_list[i-1],my_list[i])

# 5. 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
#
my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가
for i in range(len(my_list)-1,0,-1):
    print(my_list[i],my_list[i-1])

# 6.리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때,
# low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
#
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility=[]
for i in range(len(high_prices)):
    diff=high_prices[i]-low_prices[i]
    volatility.append(diff)
print(volatility)

# 7.리스트에 저장된 데이터를 아래와 같이 출력하라.
#
apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# -----
# 201 호
# 202 호
# -----
# 301 호
# 302 호
# -----

for i in range(apart):
    for j in range(i):
        print(j,"호")
    print("-"*5)

# 8. 구글 입사 test
# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
#
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)
eight=0
for i in range(1,10001):
    eight+=str(i).count("8")
print(eight)

#range를 list로 만들면 str의 나열이 됨
count_8 = str(list(range(1, 10001))).count('8')
print(count_8)
