# s2=set("hihello")
# s2.remove('h')
# print(s2)

#불 자료형
#거짓: "", None, 0, [], (), {}
#참: 그 외

# a=[1,2,3]
# while a: #a가 참인 동안에=a에 삭제할 데이터가 존재하는 동안에
#     a.pop()
# print('제거 완료')
#변수=리스트 일 때, 리스트(객체)는 메모리에 생성되고, 변수 a는 리스트가 저장된 메모리상의 주소를 가진다.

#a 변수가 가리키는 메모리 주소 확인
# print(id(a)) #1465889717248

# a=[4,5]
# b=[]
# a=b
# print(a is b) #a와 b가 가리키는 메모리상의 대상이 동일한가
#True

# a=[1,2]
# b=[1,2]
# print(a is b) #False
# print(a==b) #True

#a 변수 값을 가진 다른 주소(c) 만들기
# a=[2,4,6]
# c=a[:]
# print(a is c) #False
# print(a==c)
#
# 패키지(폴더):모듈(파일) 또는 패키지의 묶음
# 모듈:관련 함수들의 묶음

# from copy import copy
#from 모듈명 import 함수명 = 모듈로부터 함수를 가져와라
# a=[1,2]
# b=copy(a)

# money=6500
# if money>=20000:
#     print("taxi")
# elif money>=10000:
#     print("bus")
# elif money>=5000:
#     print("walk")

# s=60
# if s>=60:
#     msg="pass"
# else:
#     msg="fail"
# print(msg)
#
# #for short
# s=60
# msg="pass" if s>=60 else "fail"
# print(msg)

# prompt="""
# 1.취소
# 2.입력
# 3.종료
# 입력 :
# """
# num=0
# while num!=3:
#     num=int(input('번호입력:'))
#     print(prompt)

#1~100사이의 자연수 중 4의 배수의 합 출력
# num=1
# sum=0
# while num<=100:
#     if num % 4 == 0:
#         sum=sum+num
#     num += 1
# print(sum)
#
# num=0
# sum=0
# while num<100:
#     num += 1
#     if num % 4 == 0:
#         sum=sum+num
# print(sum)

# mylist=["하나","둘","셋"]
# for i in mylist:
#     print(i)
#
# for i in [(1,2),(3,4),(5,6)]:
#     print(i)
#
# for i,j in [(1,2),(3,4),(5,6)]:
#     print(i)
#
# for i in range(3,10,2):
#     print(i)
#
# a=[5,6,7,8]
# for i in range(len(a)):
#     print(i)
#0 1 2 3
#
# for dan in range(2,10):
#     for i in range(1,10):
#         print(dan*i, end=" ")
#     print("") #줄바꿈

# import random
# print(random.random()) #0~1
# print(random.randrange(1,7)) #1~6사이 랜덤하게 나옴. 간격 줄 수 있음.
# print(random.randint(1,46)) #1~45사이

#연습문제
# 1. a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a2=[]
for i in a:
    if i not in a2:
        a2.append(i)
print(a2)

# 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수이면서 7의 배수인
# 수의 합을 구해 보자.
num=0
sum=0
while num<1000:
    num+=1
    if num%3==0 and num%7==0:
        sum+=num
print(sum)


# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# 1)
# *
# **
# ***
# ****
# *****

1번
x=0
while x<5:
    x+=1
    print('*'*x)

2번
x=0
y=0
while x<5:
    x+=1
    y=0
    while y<x:
        y+=1
        print("*",end='')
    print()

3번
for i in range(5):
    for j in range(i+1):
        print('*', end = '')
    print() #한 줄이 끝나면 새 줄로 바꿈

# 2)
#      *
#     **
#    ***
#   ****
#  *****
1번
y=5
while y>0:
    y-=1
    print(" "*y+"*"*(5-y))

for 루프
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

# 3)adv
#      *
#     ***
#    *****
#   *******
#  *********

#
z=0
while z<10:
    z+=1
    if z%2==0:continue
    print(' '*((9-z)//2)+'*'*(z))

for 루프
for i in range(1,6):
    for j in range(6-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
# 4.
# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for a in range(1,101):
   print(a)

# 4-1.(adv)
# for문을 사용해 2부터 100까지의 숫자 중에서 소수를(prime number) 출력해 보자.
# *소수란? 1과 자기 자신으로만 나누어 떨어지는 수(ex. 2, 3, 5, 7, 11, 13,...)

for i in range(2,101):
    boolean=True
    for j in range(2,i):
        if i%j==0:
            boolean=False
            break
    if boolean:
        print(i, end=' ')


# 5.
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
score=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.
sum=0
for s in score:
    sum+=s
print(sum/len(score))


# 6. 로또 당첨 번호 제작(adv)
# *주의:중복된 수 나오면 안됨
# 이번 주 로또 당첨 번호 :  3 7 13 22 25 29

import random

for i in range(1,7):
    num=random.randint(1,46)
    print(num,end=" ")

7. 자판기(pro, 커피 한 잔에 300원이라 가정, 초기 커피는 10개)
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






