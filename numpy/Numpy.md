# Numpy

> 빠르고 공간 효율적인 ndarray 로 벡터 연산이 가능한 다차원 배열 생성가능. loop 프로그래밍 없이 전체 배열에 대해 표준 수학 함수를 빠른 속도로 수행할 수 있어 선형대수, 무작위 난수 생성 등에 많이 사용.

```python
import numpy as np
```

버전 확인 : `np.__version__`

걸리는 시간 확인(매직 타임) : `%time`

```python
li=list(range(10))
%time for _ in range(10): li2=[x*2 for x in li]

myarr=np.array([1,2,3])
%time for _ in range(10): arr2=myarr*2
```

numpy는 array에 바로 곱하면 요소에 곱해진다



## array



### 생성

```python
직접 넣기
np.array([6,5,4,3])
np.array([[1,2,3],[4,5,6]])

data=[1,2,3]
arr1=np.array(data, dtype=np.float32)
```

```python
np.arange(from,to,step) #to 포함 안함

np.arange(5) #0~4까지 array
np.arange(1,6,2) #array([1, 3, 5])
```

```python
# 행렬구조로 변환하기
np.reshape(행,열)

arr=np.arange(4)
arr.reshape(2,2)
#array([[0, 1],
#       [2, 3]])

np.arange(6).reshape(2,3)
#array([[0, 1, 2],
#       [3, 4, 5]])

#행렬구조 -> 일차원으로 펼치기
arr.flatten()
arr.ravel()

x=np.arange(5)
x[:,np.newaxis] #각 행을 하나의 열로
```

```python
np.asfarray() #float형태로 만들 때
d=[1,2,3]
np.asfarray(d)
array([6.,7.,8.,9.,10.])

np.asarray()로 array로 변환
#단, 이미 있다면 복사 안함
a=np.asarray(arr)
a is arr
#True

np.asarray_chkfinite() #데이터의 결측값이나 무한수 있으면 에러
```



#### 요소 채우기

```python
#0으로 채우기(실수 형태)
np.zeros(10) 
np.zeros((3,6)) 

#1로 채우기
np.ones((2,3))
np.ones(5)*5

#(2,2)행렬을 5로 초기화
np.full((2,2),5) 
#array([[5, 5],
#       [5, 5]])

#단위행렬
np.eye(3)
#array([[1., 0., 0.],
#       [0., 1., 0.],
#       [0., 0., 1.]])
np.eye(3,k=1)
#array([[0., 1., 0.],
#       [0., 0., 1.],
#       [0., 0., 0.]])
np.eye(3,k=-1)
#array([[0., 0., 0.],
#       [1., 0., 0.],
#       [0., 1., 0.]])

#난수(쓰레기값) 채우기
np.empty(3)
np.empty((3,2))
```

- 이미 있는 array와 동일한 모양과 데이터형태를 유지한 상태에서 초기화

```python
a=np.array([[1,2,3],[4,5,6]])

np.zeros_like(a)
array([[0, 0, 0],
       [0, 0, 0]])

np.ones_like(a)
array([[1, 1, 1],
       [1, 1, 1]])

np.empty_like(a)
array([[-1856051296,         340,           0],
       [          0,           1,           0]])
```





#### 난수 발생

```python
np.random.seed(0) #시드 생성

행렬구조로 난수 발생시킬때 함수에 따라 인자를 튜플로 받기도 한다.
-> (()) 와 ()를 다르게 줘야한다.

#[0,1)범위 내 균일 분포
np.random.rand(5)
np.random.rand(2,3)

#평균이 0 표준편차가 1인 표쥰정규분포를 따르는 난수
np.random.randn(5)
np.random.randn(2,3)

np.random.standard_normal(3)
np.random.standard_normal((2,3))

#0에서 1사이의 난수. 
np.random.random(2)
np.random.random((2,3)) 

#정수 난수
np.random.randint(5,size=3) #[0,5)에서 정수 3개
np.random.randint(1,4,2) #[1,4)에서 정수 2개
np.random.randint(1,5,size=(2,3)) #[1,5)에서 (2,3) 행렬구조

#주어진 1차원 어레이에서 샘플 생성
np.random.choice(5,3) #np.arange(5)에서 3개 샘플
np.random.choice(10,(2,3)) #np.arange(10)에서 (2,3) 어레이

#정규 분포로부터 샘플링된 난수
np.random.normal(0,1,2) #정규분포 N(0,1)의 임의의 숫자 2개
np.random.normal(1.5,2.0,(2,3)) #정규분포 N(1.5,2.0^2)의 (2,3)형태의 임의의 숫자 어레이

x=np.arange(10)
np.random.shuffle(x)
x
```





### 속성

numpy 배열은 모든 원소가 같은 자료형이어야 한다.

```python
arr=np.ones((2,3))

len(arr) #행의 개수
len(arr[0]) #열의 개수
np.shape(arr)[1]
arr.shape #(2,3)
arr.ndim #2차원
arr.dtype #dtype('float64')
#type 변환은 arr.astype(np.float64) => 실수로 변환
arr.itemsize #8 (8byte=float, 4byte=int)
arr.size #6 (요소개수)

arr.T  #행,열 바꾸기
```

```python
#3차원 배열
#0~31까지의 array
arr=np.arange(32).reshape(4,2,4) #4행 2열 4채널=깊이=높이

array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]],

       [[16, 17, 18, 19],
        [20, 21, 22, 23]],

       [[24, 25, 26, 27],
        [28, 29, 30, 31]]])

arr.ndim #3차원
arr.sum() #전체합

arr.sum(axis=0) #행 방향으로 요소 모두 더한 값
array([[48, 52, 56, 60],
       [64, 68, 72, 76]])

arr.sum(axis=1) #열 방향으로 요소 모두 더한 값
array([[ 4,  6,  8, 10],
       [20, 22, 24, 26],
       [36, 38, 40, 42],
       [52, 54, 56, 58]])

arr.sum(axis=2) #깊이 방향으로 요소 모두 더한 값
array([[  6,  22],
       [ 38,  54],
       [ 70,  86],
       [102, 118]])
```

<img src="Numpy.assets/shape1.png" alt="실습 데이터 다차원 배열의 shape: (4, 2, 4) " style="zoom:70%;" />

<img src="https://taewanmerepo.github.io/2017/09/numpy_axis/sample.jpg" alt="실습 데이터의 형태" style="zoom:50%;" />

#### 기술통계

```python
#axis 생략하면 None
arr.sum(axis=None) #np.sum(arr)
arr.min() #np.min(arr)
arr.mean() #np.mean(arr)
arr.var() #np.var(arr)
arr.std() #np.std(arr)
arr.median() #np.median(arr)
arr.cumsum() #누적합
arr.cumprod() #누적곱
np.percentile(arr,25) #0=최소, 25=1사분위수...

arr>0.sum() #양수의 개수
arr[arr>0].sum() #양수의 합
```

#### 결합

```python
#열 결합 (행의 개수가 같아야한다)
a=np.ones((2,3))
b=np.zeros((2,2))
np.hstack([a,b])

#행 결합 (열의 개수가 같아야한다)
a=np.ones((2,4))
b=np.zeros((3,4))
np.vstack([a,b])

#배열 반복
np.tile(a,2) #옆으로 2번 
np.tile(a,(3,1)) #아래로 3번
np.tile(a,(3,2)) #아래로 3번, 옆으로 2번
```



### 연산

```python
array 요소별 연산

data=np.arange(6)

data*10
data+data
data*data
data**2 
np.dot(data,data.T) #행렬곱 (2,3)*(3,2)=>(2,2)
np.sqrt(data)
np.exp(data)
np.maximum(x,y) #x,y 배열의 두 요소 중 큰 값 리턴
np.minimum(x,y) #x,y 배열의 두 요소 중 작은 값 리턴
np.modf(arr) #정수, 실수 분리해서 array 두 개인 튜플로 리턴
remainder, whole_part=np.modf(arr) #각 array를 변수에 넣기
np.meshgrid() #두 개의 1차원 배열을 입력받아서 가능한 모든 (x,y) 2차원 배열 2개 리턴
```



### 인덱싱

```python
0번부터 인덱싱

ar2=np.arange(10,16).reshape(2,3)
#array([[10, 11, 12],
#       [13, 14, 15]])

#12 인덱싱
ar2[0][2] 
ar2[0,2]
ar2[0][-1]

#1행 2열 
ar2[1,2] 

#0행과 1행
ar2[[0,1]]

arr=np.arange(10,42).reshape(8,4)
#1,5,7,2 행 추출
arr[[1,5,7,2]] 

#각 행의 추출할 열 값 따로 입력하여 하나의 벡터값으로 추출
arr[[1,5,7,2],[0,3,1,2]] 
#array([14, 33, 39, 20])

#각 행의 추출할 열 순서 정하기
arr[[1,5,7,2]][:,[0,3,1,2]] 
```

#### 인덱스 구하기

```python
#0이 아닌 인덱스
np.nonzero([1,2,0,0,3])
#(array([0, 1, 4], dtype=int64),)

#오름차순으로 인덱스 반환
np.argsort(기준)
#내림차순은 -
np.argsort(-기준)
```

#### 슬라이싱

```python
arr=np.arange(11,20).reshape(3,3)
arr
array([[11, 12, 13],
       [14, 15, 16],
       [17, 18, 19]])

arr[:2,1:]
array([[12, 13],
       [15, 16]])

arr[2] #1차원 (3,)
arr[2,:] #1차원 (3,)
arr[2:,:] #2차원 (1,3)
#다 같은 결과인데 구조가 다름
array([17, 18, 19])
-범위에 따라 구조가 달라진다. 
-[1,]은 1차원, [1:2,]은 2차원

arr[::-1] #역방향
array([[17, 18, 19],
       [14, 15, 16],
       [11, 12, 13]])
```

#### 불리안 참조

```python
names=np.array(['Bob','Mary','Joe','Bob','Will'])

names=='Bob'
#array([ True, False, False,  True, False])

~(names=='Bob')
#array([False,  True,  True, False,  True])

#조건 여러개면 괄호
(names=='Bob')|(names=='Will') 
#array([ True, False, False,  True,  True])

arr=np.array([6,3,2,5,6,4,4])
np.in1d(arr,[2,3,6]) #arr의 요소가 [2,3,6]중에 포함되어 있는지
```

### 정렬

```python
 #열 방향으로 오름차순 정렬
arr.sort()
arr

#행 방향으로 오름차순 정렬
arr.sort(axis=0) 
arr

#내림차순
arr.sort()
arr[::-1] 

#문자형, 범주형 정렬
names=np.array(['Bob','Mary','Joe','Bob','Joe'])
np.unique(names)
sorted(set(names)) #종류별로 정렬
```

```
idx,cnt=np.unique([1,3,5,6,3],return_counts=True) #각 개수도 세줌
#다른 방법 : 주사위를 던져서 나온 수 집합
np.bincount([1,1,3,3,5], minlength=7) #0~6까지 숫자들이 나온 횟수 세준다
```

iris 데이터 가져오기

```python
from sklearn.datasets import load_iris
iris=load_iris()
iris.data[0,:]
```

