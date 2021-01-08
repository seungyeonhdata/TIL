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

#readline함수는 한 줄씩 읽어드림(for 또는 while 문과 함께)
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

a=3
a.isodd()
# def is_odd():
#     num = int(input("숫자 입력 :")
#     return num.isodd()




































