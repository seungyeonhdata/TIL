
# def gcd(x,y):
#     if x<y:
#         min=x
#     else: min=y
#     for i in range(min+1,1,-1):
#         if x%i==0 and y%i==0:
#             res=i
#             break
#     return res
# # print(gcd(12,24))
# def euclid(x,y):
#     while(y):
#         x,y=y,x%y
#     return x
# print(euclid(30,24))
#
#
# def lcm(x,y):
#     return x*y//gcd(x,y)
# print(lcm(6,8))


# 1~1000까지 숫자 개수 세기
# res={x:0 for x in range(10)}
# for i in range(1,1001):
#     for j in str(i):
#         res[int(j)]+=1
# print(res)
#
# from collections import defaultdict
# res=defaultdict(int)
# for i in range(1,1001):
#     for j in str(i):
#         res[j]+=1
# print(res)

#시저 암호

#ord('A')=65
# def caesar_code(word,n):
#     c=''
#     w = word.upper()
#     for i in range(len(word)):
#         c+=chr((ord(w[i])-65+n)%26+65)
#     return c
# print(caesar_code('caesar',8))
# #KIMAIZ



arr=[[5,2,3,4,32],[4,4,5,8,5],[3,45,6,6,7],[4,4,5,8,5],[3,45,6,6,7]]

def sum_array(arr):
    res=0
    arr_x=len(arr[0])
    for y in range(len(arr)):
        for x in range(arr_x):
            if x>0:
                res+=abs(arr[x][y]-arr[x-1][y])
            if x<arr_x-1:
                res+=abs(arr[x][y]-arr[x+1][y])
            if y>0:
                res+=abs(arr[x][y]-arr[x][y-1])
            if y<len(arr)-1:
                res+=abs(arr[x][y]-arr[x][y+1])
    return res
print(sum_array(arr))