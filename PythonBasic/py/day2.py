# print(True and False)

# print("%-10swhat" %"hi")

# num = 3
# s = "two"
# day = "three"
# print("I eat %d apples" % num)
# print("I eat %s apples" % s)
#
# print("I eat {0} apples".format(num)) # num에 있는 숫자를 {}값으로 대체
# print("I eat {0} apples".format(s))
#
# print("I eat {0} apples every {1} days.".format(num, day))
# print("I eat {1} apples every {0} days.".format(num, day))
#
# print("{0:<10}".format("hi")) #10자리 확보 후 왼쪽 정렬
# print("{0:>10}".format("hi")) #10자리 확보 후 오른쪽 정렬
# print("{0:^10}".format("hi")) #10자리 확보 후 가운데 정렬
# print("{0:-<10}".format("hi")) #10자리 확보 후 왼쪽 정렬 빈자리는 -로 채움
#
# print("{0:.4f}".format(3.145154))
# print("{0:10.4f}".format(3.145154)
#
# 문자열 삽입
# print(",".join("abcd"))
# print(",".join(['a','b','c','d']))
# #리스트에 저장되어 있는 각각의 요소들을 컴마와 결합하여 하나의 문자열로 만든다
#
# t=str.maketrans('aeiou','12345')
# print('apple'.translate(t))
# 변환테이블(t)를 참조하여 문자바꾸기

# 정규표현식 : 문자열 전처리
# str=", python,."
# print(str.strip('.,'))
# 제거대상 문자를 나열하면 다 지워짐
#
# import string
# print(str.strip(string.punctuation+" "))

# print('python'.ljust(10)) #10자리 확보 후 좌측 정렬

# 적재해야 하는 함수 import
# chaining
# print('python'.rjust(10).upper())

# padding : 특정 값으로 빈자리를 채우는 것

# list
# x=[10,20,30,['life','is',['too',['short']]]] # x에는 요소가 몇 개? 4개
# print(x[3][2][1][0])
# short

# 리스트 생성
# b=[]
# b=list()
#
# b=[1,2,3]
# print(b[0]+b[2])
# 4

# x=[10,20,30,['life','is',['too',['short']]]]
# print(x[-1][-1][-1][-1])
# short

# 리스트 슬라이싱
# x=[10,20,30,40]
# print(x[1:4])
# print(x[1:-1])
# print(x[::-2])

# a=[1,2,3,['x','y','z'],4,5]
# print(a[3][:2])
# ['x','y']

# print(list(range(2,5)))
# [2,3,4]

# a=[1,2]
# b=[3,4]
# print(a*3)
# print("a"*3)
# print(len(a))
# a에 "hi" 더하기
# print(str(a[0])+"hi")


#리스트 값 변경
# a=[1,2,3]
# a[2]=4 # 변경
# a.append(4) # 추가
# a.extend([5,6,7]) # 확장 a+=[5,6,7]
# a.insert(0,4) # 1 자리에 4 추가
# del a[1] # 위치 삭제
# a.remove(2) # '2' 1개 제거
# a.pop() # 가장 마지막 위치의 데이터 제거

# a=list(range(1,10))
# del a[:5]
# print(a)

# 리스트 정렬
# a=[3,5,6,2]
# a.sort()
# a.reverse()

# 연습 문제
# 1.다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())

# 2.다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
print(ticker.lower())

# 3.다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
a=a.split(" ")
print(a)

# 4.다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
t=ticker.split("_")
print(t)

# 5.다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-12-30"
d=date.split("-")
print(d)

# 6.문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
data=data.rstrip()
print(data)

# 7.
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
print("이름: %s 나이: %d" % (name1,age1))
print("이름: %s 나이: %d" % (name2,age2))

# 8. 문자열의 format( ) 메서드를 사용해서 7번 문제를 다시 풀어보세요.
print("이름: {0} 나이: {1}".format(name1,age1))
print("이름: {0} 나이: {1}".format(name2,age2))

# 9. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
price = "5,969,782,550"
price=int(price.replace(",",''))
print(price)

# 10. 다음과 같은 문자열에서 '2020/12'만 출력하세요.
분기 = "2020/12(E) (IFRS연결)"
extracted=분기[:7]
print(extracted)

# 11. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
str=string.replace('a','A')
print(str)

# 12.
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = "881120-1068234"
print(pin[7])

# 13.다음과 같은 문자열 a:b:c:d가 있다. a#b#c#d로 바꿔서 출력해 보자.
a = "a:b:c:d"
a=a.replace(':','#')
print(a)

# 14. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# (join 활용)
list=['Life', 'is', 'too', 'short']
print(" ".join(list))

# a=[1,2,3]
# a+=[4]
# a.append(4)
# print(a)
# a+=[5,6,7]
# a.extend([5,6,7])
# print(a)

# a.append([5,6,7]) #리스트가 추가
# print(a)
# [1, 2, 3, 4, [5, 6, 7]]

# a.extend([5,6,7]) #확장 a=a+[5,6,7]
# print(a)

# b=[1,2,3]
# b.extend([4,5])
# print(b)
# b=b+[4,5]
# b+=[4,5]
# print(b)
# [1, 2, 3, 4, 5, 4, 5]


print("hello".zfill(10)) #zero fill
print("345".zfill(10)) #zero fill
