# 입출력 종류: 표준, 파일, 네트워크
# 파일 입출력
# -open():파일 열기 -> 파일 입력(read)/출력(write) -> 파일 닫기(close)

#파일로부터 문자열 입력
# f=open("hello.txt","r")
# s=f.read()
# print(s)
# f.close

#with ~as 구문은 파일을 사용한 뒤에 자동으로 파일을 닫아줌
#with open(파일이름,모드) as 파일변수:
#    코드
#

# with open("hello.txt","r") as f:
#     s=f.read()
#     print(s)

#파일에 여러줄 출력
#hello world 1
# ...
#hello world 10

#w모드로 열게되면 기존 작성 내용은 사라짐
# with open("hello.txt","w") as f:
#     for i in range(10):
#         f.write("hello world {0}\n".format(i+1))

# 리스트의 내용을 파일에 출력
# lines=['hi\n','how are you\n']
# with open("hello.txt","w") as f:
#     f.writelines(lines)

#readline함수는 한 줄씩 읽어들임(for 또는 while 문과 함께)
# with open("hello.txt","r") as f:
#     line=None
#     while line !="":
#         line=f.readline()
#         print(line.strip("\n"))
# #속도 빠름 (read는 느림)
#
# #피클(pickle) :파이썬 객체를 파일로 저장하고자 할때 사용하는 모듈
# # 피클링 : 객체 -> 파일
# # 언피클링 : 파일 -> 객체
#
# #객체를 파일로 저장
# import pickle
# 내용물="단팥"
# 색상="파랑"
# 너비="20cm"
# 가족명단={'잉어':30,'게':10,'문어':40}
# #객체 저장할때는 wb 모드로 파일 열기
# with open ("myfish.p","wb") as f:
#     pickle.dump(내용물, f)
#     pickle.dump(색상, f)
#     pickle.dump(너비, f)
#     pickle.dump(가족명단, f)
#
# with open ("myfish.p","rb") as f:
#     내용물=pickle.load(f)
#     색상 = pickle.load(f)
#     너비 = pickle.load(f)
#     가족명단 = pickle.load(f)
# #저장된 순서와 읽어들이는 순서가 일치해야함
#     print(내용물)
#     print(색상)
#     print(너비)
#     print(가족명단)

# f=open("hello.txt","a")
# for i in range(5):
#     f.write("%d번째 줄 추가\n" % (i+1))
# f.close()
#
# res=0
# def add(n):
#     global res
#     res+=n
# add(3)
# print(res)
#
# 사람(클래스):실체가 없음
# 사람홍길동(객체), 사람임꺽정(객체):실체가 있음

# class Calculator: #통상적으로 class는 대문자로 시작
#     def __init__(self):
#         self.res=0
#     def add(self, n):
#         self.res+=n
#         #10%할인 코드를 여기에 작성하면 모든 Calculator에 공통 적용
#         return self.res
# cal1=Calculator() #클래스로부터 객체를 생성(init 함수 자동 호출, res=0으로 초기화).
# # Calculator로부터 cal1생성
# cal2=Calculator()
#
# print(cal1.add(3000))
# print(cal1.add(5000))
# print(cal2.add(1500))
# print(cal2.add(2000))
# import mod1 as m
# print(m.madd(1,2))


# from mod1 import msub
# mod1 모듈에 정의되어 있는 msub 메서드만 가져오기
# print(msub(2,1))

# from mod1 import * #모든 함수 다 가져오기
#
# import mod1 as m
# #이 상태로 실행하면 mod1.py의 실행값 가져옴
#
# print(m.madd(3,5))

# 연습문제

#1.
# def is_odd():
#     num=int(input("input number:"))
#     if num%2==0:
#         print("jjaksu")
#     else:
#         print("holsu")
# is_odd()

#2.
# fhand=open("test.txt","a")
# fhand.write("Life is too short\n")
# text=input("파일에 입력할 내용 : ")
# fhand.write(text)
# fhand.close()

# with open("test.txt","a") as f:
#     f.write("Life is too short\n")
#     text=input("파일에 입력할 내용:")
#     f.write({0}".format("))

# # 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
# def is_odd (n):
#     if n%2==0:
#         print("짝수")
#     else:
#         print("홀수")
#
# # 2. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# # 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
# with open ('test.txt','a') as f:
#     f.write('Life is too short\n')
#     i = input("파일에 저장할 내용을 입력하세요 : ")
#     f.write("%s \n" % i)
#
# with open ('test.txt','r') as f:
#     r=f.read()
#     print(r)
#
#
# # 3. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# # Life is too short
# # you need java
# with open ('test2.txt','w') as f: #윗문제랑 엉켜서 'test2.txt'로 변경
#     f.write('Life is too short\nyou need java')
#
# with open("test2.txt", "r") as f:
#     s = f.read()
#
# with open("test2.txt","w") as f:
#     s=f.write(s.replace("java","python"))
#
#
# # 4. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
# def print_coin() :
#     print('비트코인')
# # 5. 4에서 정의한 함수를 호출하라.
# print_coin()
# # 6. 4에서 정의한 print_coin 함수를 100번호출하라.
# for x in range (100):
#     print_coin()
# # 7. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# def print_coins():
#     for x in range(100):
#         print('비트코인')
#
# # 8. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# def print_with_smile():
#     c=input("하나의 문자를 입력하세요 : ")
#     print(c+':D')
#
#
# # 9. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# def print_upper_price():
#     l = [x for x in map(int, input("현재 가격을 입력하세요 : ").split(' '))]
#     l.sort()
#     l.reverse()
#     upper=int(0.3*len(l))
#     print(l[:upper])
#
#
# # 10. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# def print_even():
#     l = [x for x in map(int, input("숫자를 입력하세요 : ").split(' '))]
#     for x in l:
#         if x%2==0:
#             print(x)
#
#
# # 11. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# def print_keys():
#     dict = {}
#     key = input('키 입력 : ')
#     val = input('밸류 입력 : ')
#     dict[key] = val
#     print(dict.keys())
#
#
# #12. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# def print_mxn(string):
#     string=string.replace(" ","")
#     print('글자 수 : ',len(string))
#
# s=input('글자를 입력하세요 : ')
# print_mxn(s)
#
#
# # 13. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라.
# # 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# def calc_monthly_salary(annual_salary):
#     print('월급 :',int(annual_salary/12))
#
# a=int(input('연봉을 입력하세요 : '))
# calc_monthly_salary(a)
#
#
# # 14. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# def make_url():
#     i=input('입력 : ')
#     print ('www.%s.com'%i)
#
#
# # 15. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# def make_list():
#     i = input("문자열을 입력하세요 : ")
#     m_list=[]
#     for x in i:
#         m_list.append(x)
#     print(m_list)
#
#
# # 16. 게임 기업 입사문제
# # 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# # 예를 들어 d(91) = 9 + 1 + 91 = 101
# # 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# # 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# # #그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# # 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# # 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
#
# gen=set() #불필요한 중복 제거
# for i in range(1, 5000):
#     d_n = i + i%10 + (i%100)//10 + (i%1000)//100 + i//1000 #자신+1의자리+...+1000의자리
#     gen.add(d_n)
#
# self_num=[]
# self_sum = 0
# for i in range(1, 5001):
#     if i not in gen: #gen에 없는 수는 제네레이터가 없음
#         self_num.append(i)
#         self_sum = self_sum + i
# # print(self_num) #셀프넘버 확인용
# print('모든 셀프 넘버들의 합 : ',self_sum)
#
#
# # 17. 최대낙차
# box=[7,4,2,0,0,6,0,7,0]
# count=0
# max_list=[]
#
# for i in range(len(box)) :
#     right=box[i+1:] #자신보다 오른쪽에 있는 그래프
#     box_list = []
#
#     for j in right:
#         if box[i]<=j:
#             box_list.append(j) #오른쪽에 자신보다 길거나 같은 그래프가 있으면 append
#
#     drop=len(box)-len(box_list)-(i+1) # 낙차 = 입력값 갯수- 길거나 같은 그래프 갯수 - 본인의 위치
#     max_list.append(drop)
#
# m_drop=max(max_list)
# print('최대낙차 : ',m_drop)

































