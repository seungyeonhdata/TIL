def madd(a,b):
    return a+b
def msub(a,b):
    return a-b

if __name__=="__main__": #자기자신에서 실행할때만 출력되도록
    print(madd(1,2))
    print(msub(2,1))
else:
    print(__name__)

#mod1.py를 실행시키면 __name__이라는 특별한 속성의 값으로 __main__이 저장
