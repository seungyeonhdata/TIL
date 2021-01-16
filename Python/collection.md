# 컬렉션

여러개의 값을 모아서 저장



## 시퀀스 자료형

 : list, tuple, 문자열, range, bytes, bytearray 등 값들이 연속적으로 저장된 형태

* 데이터 존재 유무 확인

  ```python
  찾고자하는 값 in 시퀀스객체
  
  print(30 in a) #True
  print(30 not in a) #False
  ```

* 시퀀스 객체 연결 ('+' 덧셈연산자)

  ```python
  a=[1,2]
  b=[3,4]
  print(a+b)
  #[1,2,3,4]
  
  a=(1,2)
  b=(3,4)
  print(a+b)
  #(1,2,3,4)
  
  #range 객체는 list나 tuple로 변경 후 연결
  print(list(range(0,4))+list(range(4,6)))
  #[0,1,2,3,4,5]
  
  #문자열+숫자> 숫자를 str로
  "hi"+str(100)
  ```

* 시퀀스 객체 반복('*' 곱셈연산자)

  ```python
  print([1,2]*2)
  #[1,2,1,2]
  
  #range는 list나 tuple로 변경 후 반복
  print(list(range(0,4,2))*2)
  #[0,2,0,2]
  ```

* 길이

  ```python
  s="안녕하세요"
  print(len(s))
  #5
  print(len(s.encode('utf-8')))
  #15
  #utf-8에서는 한 글자가 3byte
  ```

* 대괄호로 참조; 참조하여 삭제는 리스트만 가능 `del s[0]`

* slice 객체로 자르기

  ```python
  print(list(range(5,20)[slice(3,9,2)])
  #[8,10,12]
  
  #교체
  a=list(range(8))
  a[1:4]=['a','b','c']
  #[0,'a','b','c',4,5,6,7]
  ```



### 리스트: []

```python
','로 자료 구분하여 순서대로 저장
리스트는 리스트를 포함한 다양한 자료형을 요소값으로 저장 가능

b=[] 
b=list() #빈 리스트 생성

s="hello"
print(list(s))
#['h','e','l','l','o']

a=list(range(1,7))
#[1,2,3,4,5,6]

print(list(range(5))) #[0,1,2,3,4]
print(list(range(3,10))) #[3,4,5,6,7,8,9]
print(list(range(3,10,2))) #[3,5,7,9]
print(list(range(10,0,-1))) #[10,9,8,7,6,5,4,3,2,1]

#'too' 출력
a=[1, 2, ['life', 'is',['too', 'short']]]
print(a[2][2][0])
print(a[-1][-1][-2])
```



* 리스트 컴프리헨션

```python
문법으로 요소의 집합 정의하기
nums=[n*2 for n in range(1,7)]

nums=[]
for n in range(1,7):
    nums.append(n*2) 
#[2,4,6,8,10,12]

#3의 배수만 취하려면 if문으로 조건 작성
nums=[n*2 for n in range(1,7) if n%3==0]
#[6,12]

#1~10까지 짝수 저장
print([i for i in range(1,11) if i%2==0])

#for문 여러개
print([(d,d2) for d in ['쌈밥','치킨','피자'] for d2 in ['사과','아이스크림']])

#0~9까지 수 중 5보다 작으면서 2로 나누어 떨어지는 수
print([for i in range(10) if i<5 and i%2==0])

#음수면 0으로 출력
a=[1,-5,4,2,-2,10]
print([i if i>0 else 0 for i in a])

for i in a:
    if i==1:
        print("pass")
    elif i==2:
        print("fail")
    else:
        print("no")
#한줄로 줄이면
print(["pass" if i==1 else "fail" if i==2 else "no" for i in a])


```



* 리스트 슬라이싱

```python
[begin:end:step]

x=[10,20,30,40,50]
print(x[1:4:-1]) #1부터 3번 요소까지 -1간격으로

a=[1,2,3,['x','y','z'],4,5]
print(a[3][:2])
#['x','y']
```



* 리스트 연산

```python
b=[1,2,3]
print(b[0]+b[2])
#4

a=[1,2]
b=[3,4]
print(a+b)
#[1,2,3,4]
print("ab"+"cd")
#abcd

print(a*3) #[1,2,1,2,1,2] a가 3번 반복
print("ab"*3) #ababab
print(len(a)) #2

print(a[0]+"hi") #에러 발생. 정수와 문자열은 더할 수 없다
print(type(a[0])) #int
print(type("hi")) #str

str(a[0]) # 숫자 1 -> 문자열 "1"
print(str(a[0])+"hi")  => 1hi 출력
#str 함수: 정수나 실수를 문자열로 변환해주는 함수
```



* 리스트 값 변경

```python
a=[1,2,3]
a[2]=30 
#a=[1,2,30]

a=[0,1,2,3,4,5,6]
a[1:4]=[10,20,30]
#a=[0,10,20,30,4,5,6]

#소문자로 변경
words=['Computer','Coke','Bread']
print([i.lower() for i in words])
```



* 리스트 추가, 확장, 삽입(append, extend, insert)

```python
a=[1,2,3]
a+=[4]
a.append(4) #리스트 끝에 요소 추가
#둘다 a=[1,2,3,4]

a.append([5,6,7]) #리스트 추가
#a=[1, 2, 3, 4, [5, 6, 7]]

a+=[5,6,7]
a.extend([5,6,7]) 
#[1,2,3,5,6,7]

a.insert(1,4) # 1번 요소에 4 추가
#a=[1,4,2,3]

nums = [1,2,3,4]
nums[2:2] = [90,91,92] #삽입
#[1,2,90,91,92,3,4]
print(num.insert(2,[90,91,92]))

nums = [1,2,3,4]
nums[2] = [90,91,92] #대체
#[1,2,90,91,92,4]
```



* 리스트 값 제거(del, remove, pop)

```python
#del : 위치 삭제. 내장함수
a=[10,20,30]
del a[1]
#a=[10,30]

a=list(range(1,10))
del a[:5] #0~4번 index까지 삭제
#a=[6,7,8,9]

#remove : 값 삭제
a=[10,20,30,10,20,30]
a.remove(30) #첫번째 30만 제거, 없는 요소값을 입력하면 에러 발생
a.remove(30) #두번째 30 제거
#a=[10,20,10,20]

a=[10,20,30,40,50]
a[1:4]=[]
print(a)
#[10,50]

#pop : 가장 마지막 위치의 데이터 제거 후 삭제한 요소를 리턴
a=[10,20,30]
print(a.pop())
#[30] 
a.pop()
#a=[10]
```



* 리스트 정렬

```python
a=[3,5,6,2]
a.sort() #오름차순
a.reverse() #뒤집기
a.sort(reverse=True) #내림차순

단, 이렇게 출력하면 안됨
print(a.sort()) 
#None

#sorted는 정렬된 새로운 리스트를 만들어 리턴하므로 별도의 변수 대입
b=[3,7,8,5]
b2=sorted(b)
print(b2)
#[3,5,7,8]
```



### 튜플: ()

```python
t=()
t=tuple()
tu=2, #요소가 하나면 일반 변수랑 구분안돼서 값 다음에 콤마 찍어 튜플 표시
t0=5,6,7 #만들때 괄호 안써도 됨

tuple(range(5)) #(0,1,2,3,4)
tuple(range(1,9,2)) #(1,3,5,7)

s="hello"
print(tuple(s))
#('h','e','l','l','o')

#unpacking
tu="김","이","강"
kim,lee,kang=tu
print(lee) #이
print(kim) #김
print(kang) #강

#swap
a,b=12,34
a,b=b,a
print(a,b)
#34,12
```

* 튜플은 값을 변경할 수 없다.

```python
t1[1]=20 #불가능
del t1[1] #불가능

#값 변경 (튜플>리스트>요소값 변경)
x=tuple(range(1,5)) #튜플생성
print(list(x)) #리스트로 변경
tempx=list(x) #리스트로 새로 저장
tempx[2]=30 #요소값 변경
print(tempx)

y=[1,2,3]
tempy=tuple(y) #리스트>튜플
```

* 변수를 여러개 쓰면 튜플 내의 값들에 순서대로 저장됨.

```python
ex1, ex2 = divmod(9,4)
#ex1=2, ex2=1 

1,2,3=(a,b,c)
```

* 연산

```python
t1=(1,2,3)
t2=('a',3,4)
t3=5,6 
print(t1[:2]) #(1, 2)
print(t1+t2) #(1, 2, 3, 'a', 3, 4)
print(t3*5) #(5, 6, 5, 6, 5, 6)
print(t1+(7,8)) #(1,2,3,7,8)
```



## 딕셔너리: {}

```python
키와 값의 쌍을 저장하는 대용량 자료구조
해시 알고리즘을 사용하여 일대일로 대응되는 특성이 있어 맵이라고도 부름.
연관배열이라고도 함.

dic={'name':'kim','add':'seoul','nn':['사과','바나나']}
#키가 중복되면 마지막에 저장한 값이 남는다.
#키는 고유값, 값은 중복가능
#키에 딕셔너리, 리스트 등 자료구조 안됨. 튜플은 가능
#순서 없음

dict(name='kim',add='seoul',nn=['사과','바나나'])

#zip 객체를 dict로 변환
#dict(zip([키 리스트],[값 리스트]))) 
print(dict(zip(['a','b'],[1,2]))) 
#{'a': 1, 'b': 2}

#키로 검색한다. 수 만개 있어도 빠름
print(dic['name'])
#kim

#키가 있는지 확인
dic={'boy':'소년','id':'홍길동','school':'학교'}
print('age' in dic)
#False

#요소 개수
print(len(dic))

#키가 없는 경우 
#.get으로 None리턴
dic={'name':'kim','add':'seoul','nn':['사과','바나나']}
print(dic.get('age'))
#None
print(dic.get('age','사전에 없는 단어'))
#두 번째 인수로 대신 돌려줄 디폴트값 지정

li=[('nn','bear'),('add','seoul'),('age','10')]
dic=dict(li) 
#리스트나 튜플로 딕셔너리 생성 가능
li=['a','b','c']
d=dict.fromkeys(li,10) #키는 li, 값은 10으로 통일
print(d)

#요소 추출
d2={'a':10,'b':20}
for k,v in d2.items():
    print(k,v)
#a 10
#b 20

from collections import defaultdict
print(d['z']) #키 없어서 에러
d=defaultdict(int)
print(d['z']) #0

```

* comprehension

```python
print({x+y:"값" for x in range(5) for y in range(5)})

scores={'철수':50,'영희':70,'순신':100}
#순신 빼기
print({
    name:score for name, score in scores.items() if name!= '순신'
	})

#점수 60점 이상이면 pass, 미만이면 fail (else는 for문이 뒤로감)
print({
    name:'pass' if score>=60 else 'fail'
    for name,score in scores.items()
     })

keys=['a','b','c']
d3={key:value for key in dict.fromkeys(keys).items()}
print(d3) #value는 어떻게 지정하지?

#'b'빼기
x={'a':10,'b':20,'c':30,'d':40}
newx={k:v for k,v in x.items() if k!='b'}
print(newx)

```

* 삽입, 삭제, 수정

```python
dic={'nn':'bear','add':'seoul','age:10'}
dic['nn']='pup' #수정
dic['height']='170' #삽입
del dic['age'] #삭제
#dic.clear() #모든 요소 제거
print(dic)
#{'nn':'pup','add':'seoul','height':'170'}

word={'boy':'소년','school':'학교'}
word2={'student':'학생'}
word.update(word2)
print(word)
#{'boy':'소년','school':'학교','student':'학생'}

dic={'nn':'bear','add':'seoul','age:10'}
print(dic.keys()) #키만 추출
print(dic.values()) #값만 추출
print(dic.items()) #키와 값 쌍으로 추출

#요소 추출하려면 리스트로 만들기
mykey=dic.keys()
listmykey=list(mykey)

x={}
x['a']=10
x['b']=20
x.update(c=300,s=50)
x.update({'a':10, 'd':30})
x.update(zip(['f','g'],[60,70]))
x.pop('s',0) #키가 없을때는 0을 리턴
x.setdefault('e') #키 e가 추가, 값이 None저장
print(x)

```



## 집합: Set{}

```python
순서 없음
키 중복 안됨
값을 포함하고 있느냐 아니냐만 중요하다.

s1=set([1,2,3,4,2]) #리스트 자료를 기초로 집합(중복 제외) 생성
#{2,4,3,1}
s2=set("hihello")
#{'h', 'o', 'l', 'i', 'e'}
s3={'blue':'sky','pink':'blush','red':'blank'}
#{'blue','pink','red'}

#교집합
s1&s2
s1.intersection(s2)

#합집합
s1|s2
s1.union(s2)

#차집합
s1-s2
s1.difference(s2)
```

* 편집

```python
add함수 : 하나만 추가
s3=set()
s3.add(3)
#{3}
s3.add([3,4]) #리스트 안됨

update함수 : 여러 개 추가
s3.update([1,2,3,4])
#{1,2,3,4}
s3.update([1,5,7])
#{1,2,3,4,5,7}

remove : 하나만 제거
s3.remove(2)
#{1,3,4,5,7}
```



# 컬렉션 관리 함수



## enumerate

```python
enumerate : 열거형 데이터를 표현하는 함수, for 문과 함께 사용
리스트, 튜플, 문자열 데이터(시퀀스 데이터)에 인덱스 부과할때

for idx,i in enumerate(['aaa','bbb','ccc']):
    print(idx,i)
#0 aaa
#1 bbb
#2 ccc

color=['red','blue','green']
list(enumerate(color))
#[(0,'red'),(1,'blue'),(2,'green')]
```



## eval

```python
eval():문자열로 구성된 수식을 입력받아서 문자열을 실행한 결과를 리턴
print(eval("10+20")) #30

for i in range(10,14):
    print(i+int((str(i))))

print(eval("divmod(5,3)"))
#(1,2)
```



## zip

```python
여러개의 컬렉션을 합쳐 하나로 만든다. 
두 리스트의 대응되는 요소끼리 짝을 지어 튜플의 리스트 생성.
두 개의 리스트를 병렬로 순회할 때 편리하다.
두 리스트 길이 달라도 짧은 쪽에 맞춰진다.

days=['월','화','수','목','금','토','일']
food=['banana','apple','orange','tomato']
menu=zip(days,food) #프린트하면 zip object
for d,f in menu:
    print("%s요일 메뉴: %s" % (d,f))
#menu 출력하고 싶으면 list나 dict으로 출력

print(list(zip([1,2],['one','two'])))
#[(1, 'one'), (2, 'two')]
```



## filter

```python
filter(함수, 자료):원하는 데이터를 걸러내는 함수
#리턴값이 True/False로 나와야함. True인 값들만 묶어서 돌려준다


ex1) 음수 걸러내기
#1.사용 안함
def pos(li):
    res=[]
    for i in li:
        if i>0:
            res.append(i)
    return res
print(pos([1,3,-5,-7,9]))

#2.filter
def pos2(li):
    return li>0
print(filter(pos2,[1,3,-5,-7,9])) #필터 객체 나옴. 꺼내려면 리스트로 바꾸기
list=[1,3,-5,-7,9]
for li in filter(pos2,list):
    print(li)

#3. filter + lambda
print(list(filter(lambda li:li>0,[1,3,-5,-7,9])))

map과의 차이점이라면, 함수의 결과가 참/거짓인지에따라 요소를 포함할지를 결정
ex2) 짝수 리스트 출력
t=list(range(1,11))

#1. 사용 안함
def isEven(n):
    return True if n % 2==0 else False   #return True or False
res=[]
for v in t:
    if isEven(v):
        res.append(v)
print(res)

#2. filter 
print(list(filter(isEven, t)))

#3. filter + lambda
print(list(filter(lambda x: x%2==0, t)))

```



## map

```python
map(함수, 자료): 모든 요소에 대해 변환 함수를 호출하여 새 요소값으로 구성된 리스트 생성

def half(s):
    return s/2

list=[24,35,46,22]
for li in map(half,list):
    print(li,end=' ')
#12.0 17.5 23.0 11.0 #float으로 출력
```



## is 연산자

```python
두 변수가 같은 객체를 가리키고 있는지 조사
list1=[1,2,3]
list2=list1
list3=list1.copy()

print(list1 is list2)
print(list1 is list3)
print(list2 is list3)
#True
#False
#False

x={'a':0,'b':1}
y=x #실제로는 딕셔너리가 1개 만들어짐
print(x is y)
#True
```



## copy

```python
a=3
b=a
a=5
#기본형 변수는 서로 독립적. 대입해도 일시적으로 값이 같아질 뿐 a값이 바뀌어도 b는 영향을 받지 않는다.

하지만 컬렉션의 경우,
list1=[1,2,3]
list2=list1
#list2의 요소를 변경하면 list1의 요소도 같이 변경된다.
#두 리스트를 독립적인 사본으로 만들기 위해 copy메서드 사용
list3=list1.copy()
list4=list1[:] #copy메서드 대신 [:]도 독립적인 사본 만듦
list3[2]=300
print(list1)
#[1,2,3]
print(list3)
#[1,2,300]

#딕셔너리로 복습
x={'a':0,'b':1}
y=x
x['a']=100
print(y)
#{'a': 100, 'b': 1}

y=x.copy() #완전히 다른 2개의 딕셔너리가 만들어짐
print(x is y) #False
print(x==y) #True
x['a']=111
print(x)
print(y)
#{'a': 111, 'b': 1}
#{'a': 100, 'b': 1}

중첩컬렉션은 copy로는 독립안됨. deepcopy해야 독립
list0=['a','b']
list1=[list0,1,2]
list2=list1.copy()

list2[0][1]='c'
print(list1)
#[['a','c'],1,2]
#list0은 여전히 공유

x={'a':{'python':'3.8'}, 'b':{'python':'2.7'}}
import copy
y=copy.deepcopy(x) #깊은 복사
y['a']['python']="2.7777"
print(x)
print(y)
#{'a':{'python':'3.8'}, 'b':{'python':'2.7'}}
#{'a':{'python':'2.7777'}, 'b':{'python':'2.7'}}
```



## any/all

```python
any:하나라도 참이면 참
all:모두 참이어야 참

adult=[True,False,True,True]
print(any(adult))
print(all(adult))
#True
#False

adult=[]
print(any(adult)) #참이 하나도 없다고 판단
print(all(adult)) #거짓이 하나도 없다고 판단
#False
#True
```



## ord/chr

```python
문자 -> 아스키코드 : chr()
아스키코드 -> 문자 : ord()
print ord('A')
#65
print chr(65)
#'A'
```

<img src="collection.assets/화면 캡처 2021-01-16 235350.png" alt="화면 캡처 2021-01-16 235350" style="zoom:60%;" />