# 1.

# def dartScore(dart):
#     score=[]
#     n=0
#     option={'S':1, 'D':2, 'T':3}
#     for i in range(len(dart)):
#         if dart[i].isdigit():
#             n+=int(dart[i])
#             if dart[i+1].isdigit():
#                 n=10
#         elif dart[i] in 'SDT':
#             n**=option[dart[i]]
#             score.append(n)
#             n=0
#         elif dart[i]=='*':
#             if len(score)>1:
#                 score[-2]*=2
#             score[-1]*=2
#         else:
#             score[-1]*=-1
#     return sum(score)
# print(dartScore("1S*2T*3S"))

# 정규식
# def dart_score(dart):
#     import re
#
#     option={'S':1, 'D':2, 'T':3, '*':2,'#':-1,'':1}
#     res=re.findall(r"(\d+)([SDT])([*#]?)",dart)
#     # print(res) [('1', 'S', '*'), ('2', 'T', '*'), ('3', 'S', '')]
#     for i in range(len(res)):
#         if i > 0 and res[i][2] == '*':
#             res[i - 1] *= 2
#         res[i] = int(res[i][0]) ** option[res[i][1]] * option[res[i][2]]
#     return sum(res)
#
# print(dart_score("1S*2T*3S"))

def LRUtime(n,cities):
    time=0
    cache=[]
    cities=[city.lower() for city in cities]
    if n>0:
        for i in cities:
            if i in cache:              #hit이면 값을 pop해서 제일 뒤로 넣어주기
                cache.pop(cache.index(i))
                cache.append(i)
                time+=1
            else:                       #miss일때
                if len(cache)<n:        #캐시 다 안 찼으면 뒤에 더하고
                    cache.append(i)
                else:                   #다 찼으면 제일 앞 빼고 뒤에 더하기
                    cache.pop(0)
                    cache.append(i)
                time+=5
    else:
        time+=len(cities)*5
    return time

n=3
city=["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(LRUtime(n,city))

