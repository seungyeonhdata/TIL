# def investment():
#     invest=int(input("투자액:"))
#     day=int(input("투자 기간:"))
#     a=input("일별 변동폭:").split(',')
#     start=invest
#     for i in range(day):
#         invest*=(1+int(a[i])/100)
#     net=invest-start
#     if net>0:
#         res="good"
#     elif net<0:
#         res="bad"
#     else: res="same"
#     print(round(net),res)
# investment()


def isprime(a): #소수 검증
    if a<2:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                return False
        return True

n=int(input("2보다 큰 짝수: "))
a=[]
for i in range(2,n): #2부터 n-1까지 소수들을 a에 모으기
    if(isprime(i)):
        a.append(i)



pairs=[]
for i in prime:
    if i<=n-i and n-i in prime:
        pairs.append[[i,n-i]]
print(pairs)

# pairs=[[i,j] for i in a for j in a if i+j==n] #a중 더해서 n이 되는 소수 페어 모으기
# import math
# half=math.ceil(len(pairs)/2) #리스트 반만 프린트. 홀수면+1
# print(pairs[:half])






before=['a1','a2','a3','a4','b1','b2','b3','b4']
def arranging(before):
    after=[]
    b=before.index('b1')
    for i in range(len(before)//2):
        after.append(before[i])
        after.append(before[b+i])
    return after
arranging(before)