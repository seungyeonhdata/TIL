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
# print(len(a))
# a에 "hi" 더하기
# print(str(a[0])+"hi")


#리스트 값 변경
# a=[1,2,3]
# a[2]=4 # 변경
# a.append(4) # 추가
# a.extend([5,6,7]) # 확장 a+=[5,6,7]
# a.insert(1,4) # 1 다음에 4 추가
# del a[1] # 위치 삭제
# a.remove(2) # '2' 1개 제거
# a.pop() # 가장 마지막 위치의 데이터 제거


# 리스트 정렬
a=[3,5,6,2]
a.sort()
a.reverse()
print(a)
