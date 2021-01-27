# 이진수
# v=10
# b=format(v,'b')
# print(b)




#1.숫자를 입력받으면 그에해당하는 자릿수를 출력하는 코드를 작성하라.
# 입력 : 156 출력 : 100의자리수
# 입력 : 18961 출력 : 10000의자릿수

# num=input("입력:")
# out=str(10**(len(num)-1))
# print("출력:"+out+"의 자리수")



# 2.
# 리스트에 있는 숫자들의 중앙값을 구하는 프로그램을 만들어라.
#
# [7, 9, 14] = 9
# [24, 31, 35, 49] = 33
# [17, 37, 37, 47, 57] = 37
#
# 중앙값 : 자료를 작은 값에서부터 크기순으로 나열할 때 중앙에 위치한 값
# ① 자료의 개수가 홀수이면 가운데 위치한 값이 중앙값이다.
# ② 자료의 개수가 짝수이면 가운데 위치한 두 값의 평균이 중앙값이다.

# import statistics
# a=[24,31,35,49]
# print(statistics.median(a))


# def get_median(a):
#     n=len(a)
#     index=n//2
#     if n%2:
#         return sorted(a)[index]
#     else:
#         return sum(sorted(a)[index-1:index+1])/2
# a=[24,49,31,35]
# print(get_median(a))

# 3.
# 아래와 같은 결과를 출력하는 function을 구현하라
#
# bool OneEditApart(string s1, string s2)
#
# OneEditApart("cat", "dog") = false
# OneEditApart("cat", "cats") = true
# OneEditApart("cat", "cut") = true
# OneEditApart("cat", "cast") = true
# OneEditApart("cat", "at") = true
# OneEditApart("cat", "acts") = false
# 한개의 문자를 삽입, 제거, 변환을 했을때 s1, s2가 동일한지를 판별하는 OneEditApart 함수를 작성하시오.
#
# def oneEditApart(s1,s2):
#     if len(s1)==len(s2):
#         for i in range(len(s1)):
#             a=s1[:i]+s1[i+1:]
#             b=s2[:i]+s2[i+1:]
#             if a==b:
#                 return True
#         return False
#     elif len(s1)>len(s2):
#         for i in range(len(s1)):
#             a=s1[:i]+s1[i+1:]
#             if s2==a:
#                 return True
#         return False
#     elif len(s1)<len(s2):
#         for i in range(len(s2)):
#             b=s2[:i]+s2[i+1:]
#             if s1==b:
#                 return True
#         return False



n=5
arr1=[9,20,28,18,11]
arr2=[30,1,21,17,28]

or 연산자: 둘 중 하나 이상이 1이면 1이되는 연산
and 연산자: 둘 다 1일때만 1, 아니면 0
print(bin(2|1)[2:].zfill(5))

# def secret_map(n,arr1,arr2):
#     ans=[]
#     for i,j in zip(arr1,arr2):
#         bn1=int(format(i,'b'))
#         bn2=int(format(j,'b'))
#         ans.append(str(bn1+bn2))
#     for i in range(n):
#         ans[i] = ans[i].replace("0", " ").replace("1", "#").replace("2", "#")
#     print(ans)


# secret=[str(int(format(i,'b'))+int(format(j,'b'))) for i,j in zip(arr1,arr2)]
# for i in range(n):
#     secret[i]=secret[i].replace("0"," ").replace("1","#").replace("2","#")





#다른사람 풀이
    # def decoding(n, arr1, arr2):
    #     map1 = []
    #     map2 = []
    #     for i in arr1:
    #         map1.append(int(str(bin(i))[2:]))
    #     for i in arr2:
    #         map2.append(int(str(bin(i))[2:]))
    #     com = []
    #     for i in range(n):
    #         com.append(str(map1[i] + map2[i]))
    #     for i in range(n):
    #         com[i] = com[i].replace("0", " ").replace("1", "#").replace("2", "#")
    #     return com






