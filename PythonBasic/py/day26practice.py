def euclid_minus(x,y):
    while (y):
        if x>y:
            x,y=y,x-y
        else: x,y=y-x,x
    return x

def euclid_div(x,y):
    while(y):
        x,y=y,x%y
    return x

def chance(a,b):
    from fractions import Fraction
    cnt=0
    for i in range(a+1,b+1):
        res=[]
        for j in range(1,i+1):
            if i%j==0:
                res.append(j)
        if len(res)%2==1:
            cnt+=1
    f=Fraction(cnt,b-a)
    print("%d/%d"%(f.numerator,f.denominator))


def print_time(x,y,n):
    t=1
    while t//x+t//y<n:
        t+=1
    return t

def printTime(x,y,n):
    timeX=[x*i for i in range(1,n+1)]
    timeY=[y*i for i in range(1,n+1)]
    time=sorted(timeX+timeY)
    print(time[n-1])