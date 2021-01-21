

# a='1.0.4'
# b='1.0'
#
# def compare_result(ver1, ver2):
#     v1 = list(map(int, ver1.split('.')))
#     v2 = list(map(int, ver2.split('.')))
#     result = "="
#     for i in range(max(len(v1), len(v2))):
#         if len(v1) == i:
#             v1.append(0)
#         if len(v2) == i:
#             v2.append(0)
#
#         if v1[i] > v2[i]:
#             result = ">"
#             break
#         elif v1[i] < v2[i]:
#             result = "<"
#             break
#     print(ver1, result, ver2)



# n=10
# k=3
# sol=list(range(n))
# del sol[2::3] 7
# del sol[1::3] 5
# del sol[0::3] 3
# del sol[1::3] 1
# del sol[0::3]
# # print(sol)
# def jose(n,k):
#     sol=list(range(1,n+1))
#     # print(sol)
#     ind=0
#     i=k-1
#     while len(sol)>1:
#         ind=(len(sol)+ind)%k
#         del sol[i::k]
#         i=k-ind-1
#     return sol
# print(jose(50,2))



# def count_words():
#     text=input("글을 입력하세요: ")
#     txt=text.split()
#     dic={}
#     for i in txt:
#         i.strip(',.')
#         dic[i]=dic.get(i,0)+1
#     lst=[]
#     for k,v in dic.items():
#         new=(v,k)
#         lst.append(new)
#     lst=sorted(lst,reverse=True)
#     for v,k in lst[:10]:
#         print(k,v)

단어 세주는 함수 있음
from collections import Counter
with open("input.txt","r") as f:
    words=[w.strip('.,') for w in f.read().split()]
for w,c in Counter(words).most_common(10)
    print(w,c)








