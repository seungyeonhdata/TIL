# def numonly(a):
#     import re
#     res=re.findall("[\d]+",a)
#     print(''.join(res))
# numonly("1wf3r627r00o!00p00")

# 2.

# def shortestExt(s):
#     lengths=[]
#     res=''
#     if len(s)==1:
#         return 1
#     for i in range(1,len(s)//2+1):
#         cnt=1
#         temp=s[:i]
#         for j in range(i,len(s),i):
#             if s[j:j+i]==temp:
#                 cnt+=1
#             else:
#                 if cnt==1:
#                     cnt=""
#                 res+=str(cnt)+temp
#                 temp=s[j:j+i]
#                 cnt=1
#         if cnt==1:
#             cnt=''
#         res+=str(cnt)+temp
#         lengths.append(len(res))
#         res=''
#     return min(lengths)
# print(shortestExt("a"))

# 함수안에 for문 안에 함수호출을 하면 과부하돼서 메모리 문제 가능

#
# 프로도의 가사찾기
# 다만 for문으로는 효율성 검사 통과 못함
words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]

# import re
# res=[]
# for i in queries:
#     p=i.replace("?",".")+"$"
#     cnt=0
#     for j in words:
#         if re.match(p,j):
#             cnt+=1
#     res.append(cnt)
#
# print(res)


#효율적인 풀이
from collections import defaultdict

class Node:
    def __init__(self,data):
        self.data=data #현재 노드를 상징하는 값
        self.count=0 #현재 노드가 소유한 모든 자식 노드의 숫자
        self.child={} #현재 노드의 자식 노드

class Trie:
    def __init__(self):
        self.head=Node(None) #최상위 노드 생성

    def insert(self,string):
        cur=self.head #최상위 노드 불러오기
        cur.count+=1

        for c in string:
            if c not in cur.child: #c가 cur.child에 없으면
                cur.child[c]=Node(c) #child[c]에 자식노드(c) 생성
            cur=cur.child[c]
            cur.count+=1 #cur을 대체하게 된 cur.child[c]의 count를 +1

    def count(self,prefix):
        cur=self.head #최상위 노드 불러오기
        for c in prefix:
            if c not in cur.child:
                return 0
            cur=cur.child[c] #있으면 자식노드로 이동
        return cur.count

def solution(words,queries):
    ans=[]
    tries=create_trie(words) #Trie 생성
    reversed_tries=create_trie(words,True)
    for query in queries:
        ans.append(count_matched_word(tries, reversed_tries, query))
    return ans

def create_trie(words,is_reversed=False):
    trie_dic=defaultdict(Trie) #dict를 생성할 시 기본적으로 Trie로 생성
    for word in words:
        if is_reversed:
            word=word[::-1]
        trie_dic[len(word)].insert(word) #trie_dict[word의 길이]에 word를 insert한다
    return trie_dic

def count_matched_word(tries, reversed_tries, query):
    no_mark_query=query.replace('?','')
    if query[0]=='?':
        return reversed_tries[len(query)].count(no_mark_query[::-1])
    else:
        return tries[len(query)].count(no_mark_query)











