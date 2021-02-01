# 1.피타고라스 빗변구하기
# def bitbyeon(x,y):
#     import math
#     z=pow(x,2)+pow(y,2)
#     return math.sqrt(z)
# print(bitbyeon(2,3))


# 2.
def JaccardSim(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    a=[]
    b=[]
    for i in range(len(s1)-1):
        if s1[i:i+2].isalpha()==True:
            a.append(s1[i:i+2])
    for j in range(len(s2)-1):
        if s2[j:j+2].isalpha()==True:
            b.append(s2[j:j+2])
    inter=[i for i in a if i in b]
    union=[x for x in a+b if x not in inter]+inter
    if union == []:
        return 65536
    return int(len(inter)/len(union)*65536)

print(JaccardSim("",""))







