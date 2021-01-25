# 1.
# a=[-1,1,3,-2,2]
# neg=[i for i in a if i<0]
# pos=[i for i in a if i>0]
# print(neg+pos)

# m=int(input("총건수:"))
# n=int(input("페이지 당 게시물 수:"))
# x, y = divmod(m, n)
# if y != 0:
#     x += 1
# print("출력", x)



a="10 fail means first attempt in learning"
a=a.split()
li=a[1:]
res=list(range(len(li)))
num=int(a[0])
for i in range(len(li)):
    res[(num+i)%len(li)]=li[i]
print(res)



