#all 함수
# print(all([1,2,3]))

#ord함수

#enumerate : 열거형 데이터를 표현하는 함수, for 문과 함께 사용
#리스트, 튜플, 문자열 데이터(시퀀스 데이터)에 인덱스 부과할때

# for idx,i in enumerate(['aaa','bbb','ccc']):
#     print(idx,i)

#eval():문자열로 구성된 수식을 입력받아서 문자열을 실행한 결과를 리턴
# print(eval("10+20")) #30
#
# for i in range(10,14):
#     print(i+int((str(i))))
#
#
# #filter():월하는 데이터를 걸러내는 함수
# #filter(함수이름, 1번째 인수에 있는 함수에 입력될 반복 가능한 자료형)
# #리턴값이 True/False로 나와야함. True인 값들만 묶어서 돌려준다
# #1.사용안함
# def pos(li):
#     res=[]
#     for i in li:
#         if i>0:
#             res.append(i)
#     return res
# print(pos([1,3,-5,-7,9]))
#
# #2.filter 사용
# def pos2(li):
#     return li>0
# print(filter(pos2,[1,3,-5,-7,9])) #필터 객체 나옴 꺼내려면 리스트로 바꾸기
# print(list(filter(pos2,[1,3,-5,-7,9])))
#
# #3. filter + 람다 함수
# print(list(filter(lambda li:li>0,[1,3,-5,-7,9])))

#hex 함수:16진수로 변환
# print(hex(234))

#경제적인 코딩: comprehension
#리스트
# print([n for n in range(5)])
#1~10까지 짝수 저장
# print([i for i in range(1,11) if i%2==0])
#for문 여러개
# print([(d,d2) for d in ['쌈밥','치킨','피자'] for d2 in ['사과','아이스크림']])
#0~9까지 수 중 5보다 작으면서 2로 나누어 떨어지는 수
# print([for i in range(10) if i<5 and i%2==0])
#셋
# print({x+y for x in range(10) for y in range(10)})
#딕셔너리
# print({x+y:"값" for x in range(5) for y in range(5)})
# scores={'철수':50,'영희':70,'순신':100}
# print({name:score for name, score in scores.items() if name!= '순신'})
#점수 60점 이상이면 pass, 미만이면 fail (else는 for문이 뒤로감)
# print({
#     name:'pass' if score>=60 else 'fail'
#     for name,score in scores.items()
#      })

# words=['Computer','Coke','Bread']
# print([i.lower() for i in words])
#음수면 0으로 출력
# a=[1,-5,4,2,-2,10]
# print([i if i>0 else 0 for i in a])

# for i in a:
#     if i==1:
#         print("pass")
#     elif i==2:
#         print("fail")
#     else:
#         print("no")
#
# print(["pass" if i==1 else "fail" if i==2 else "no" for i in a])

# x={}
# x['a']=10
# x['b']=20
# x.update(c=300,s=50)
# x.update(c=30,d=40)
# x.update(zip(['f','g'],[60,70]))
# x.pop('s',0) #키가 없을때는 0을 리턴
# del x['f']
# x.clear() 딕셔너리 전체 삭제
# print(x)

#리스트(튜플)을 딕셔너리로
# li=['a','b','c']
# d=dict.fromkeys(li,10)
# print(d)
# from collections import defaultdict
#print(d['z']) #키 없어서 에러
# d=defaultdict(int)
# print(d['z']) #0

# d2={'a':10,'b':20}
# for k,v in d2.items():
#     print(k,v)

# keys=['a','b','c']
# d3={key:value for key in dict.fromkeys(keys).items()}
# print(d3) #value는 어떻게 지정하지?
#
# #'b'빼기
# x={'a':10,'b':20,'c':30,'d':40}
# newx={k:v for k,v in x.items() if k!='b'}
# print(newx)

#연습문제 7
# s=[1,3,4,8,13,17,20]
# def shortest(s):
#     diff=[]
#     for i in range(1,len(s)):
#        diff.append(s[i]-s[i-1])
#     locate=diff.index(min(diff))
#     locate_s=tuple(s[locate:locate+2])
#     print(locate_s)
# shortest(s)
# shortest([1,4,5,8,14])
# #
#다른풀이
# def shortest(s):
#    diff=[] #[2,1,4,5,4,3]
#    for i in range(1,len(s)):
#       diff.append(s[i]-s[i-1])
#    for j in range(len(diff)):
#       if diff[j]==min(diff):
#          print(s[j:j+2])
# shortest(s)









#
# def palindrom(str):
#    oneword=str.replace(" ","")
#    if oneword==oneword[::-1]:
#       print("True")
#    else:
#       print("False")
#
# palindrom("tenet")

#다른풀이 1
# text = input("문자입력: ")
# text = text.replace(" ","")
# size=int(len(text)/2)
# length = len(text)
# for i in range(size):
#    if text[i] != text[length-1-i]:
#       res = False
#    else:
#       res = True
# print(res)

# 2
# a = "te   net"
# b = ""
# for i in a:
#     if i != " ":
#         b += i
# if b == b[::-1]:
#     print("True")
# else:
#     print("False")

#3
# def selfpalindrome(string):
#    splitstring = string.split(" ")
#    leng = len(splitstring)
#    nospace = ""
#    for i in range(leng):
#       nospace += splitstring[i]
#    reverse = nospace[-1::-1]
#    if reverse == nospace:
#       return reverse == nospace
#    else:
#       return reverse == nospace
#
# print(selfpalindrome("sos"))
# print(selfpalindrome("nurses run"))
# print(selfpalindrome("hello")