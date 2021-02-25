# R

- 데이터 분석에 적합함. 시각화나 딥러닝에는 무거워서 파이썬을 많이 씀

  

## 환경설정

1. R 설치

www.r-project.org --> cran 에서 최신버전 다운로드

2. R 스튜디오 설치

www.rstudio.com --> open source 에서 r studio 다운

3. Rstudio 기본 폴더 설정

Tools-->global options-->default working directory를 지정

**콘솔창**

```
실행 : enter
지우기 : ctrl+L
결과값에 대한 인덱스번호가 같이 나옴
```

**소스창**

```
실행 : ctrl+enter
블록 잡힌 부분 실행 :블록 잡아서 ctrl+enter
전체 실행 : ctrl+alt+R
직전 명령문 실행 : ctrl+shift+p
도움말 : ?+함수명, 드래그후 f1, help(함수명)
주석 : ctrl+shift+C
대입 <- : alt+-
출력 : 그냥, print(), cat("입력:", x)
```

새 스크립트 : `ctrl+shirt+n`

## 벡터

- c함수 : 벡터들을 모아 하나의 벡터를 만드는 함수

```R
odd<-c(1,3,5) #odd는 길이가 3인 벡터임
even<-c(2,4,6)
c(odd,even)
#[1] 1 3 5 2 4 6
```

- 수열

```R
3:9
5:1
숫자 대소 비교해서 증감을 알아서 처리함

다양한 증감치를 이용한 수열
seq(from=3, to=9, by=0.5)
seq(3,9,2)
#[1] 3 5 7 9

수열의 길이 지정
seq(from=3, to=9, length.out=5)
#[1] 3.0 4.5 6.0 7.5 9.0
```

- 반복 

```R
벡터 전체 반복 : times
rep(1, times=3)
rep(c(1,2), times=2) # 1 2 1 2

벡터 각 원소 반복 : each
rep(c(1,2), each=2) # 1 1 2 2

각 원소 다르게 반복
rep(c(1,2), c(2,5)) #1 1 2 2 2 2 2

rep(1:3, length.out=8) #1부터 3인 수열로 길이 8 만들기
#[1] 1 2 3 1 2 3 1 2
```

- 벡터는 동일한 데이터 유형으로 표현됨

```R
숫자랑 문자 합치면 문자형으로 통일됨
num<-c(1,2,3)
cha<-c("x","y","z")
c(num,cha)
#[1] "1" "2" "3" "x" "y" "z"
```

- str함수: 벡터의 유형 및 구조 확인

```R
n<-c(1,2,3)
str(n)
#num [1:3] 1 2 3
#3개의 원소를 갖는 1차원 벡터
```

- 상수벡터

```
이미 정의된 벡터들
LETTERS
letters
month.abb
month.name
pi
```

- 벡터에서 여러개의 값을 한번에 추출하기

```R
m<-c(12, 9 ,3, 5, 1)
m #5개의 요소로 이루어진 1차원 벡터
month.name
month.name[2]
#벡터의 요소들을 여러개 참조하려면 c함수로 하나의 벡터로 만들어야함 
month.name[m]
# [1] "December"  "September" "March"     "May"       "January" 
```

#### 인덱싱

```R
prime <- c(2,3,5,7,11,13,17)

idx <- c(3,4,5)
prime[idx] #5 7 11
prime[3:5] #5 7 11
prime[seq(3,5)] #5 7 11
prime[-(3:5)] #3~5번 인덱스 제외

> #마지막꺼 빼기
> prime[-length(prime)]
[1]  2  3  5  7 11 13
> #값 변경
> prime[c(3,4)] <- c(30,40)
> prime
[1]  2  3 30 40 11 13 17

#불리언 참조
> p <- c(2,3,5,19,22,14,199)
> p[c(TRUE,TRUE,FALSE)]
[1]   2   3  19  22 199

#자리 참조
which(p%%2==0) #짝수인 원소들의 인덱스
p[which(p%%2==0)] #짝수인 원소들 추출
```

- which()

```R
논리값으로 TRUE 위치 인덱스 추출

> data
 [1] 10 11 12 13 14 15 16 17 18 19 20
> which(data>15) 
[1]  7  8  9 10 11 #인덱스값
> which.min(data)
[1] 1 #1번 인덱스가 제일 작음

#월로 변환
> data <- c(100:111) #길이 12개라서
> month.abb[which(data>105)]
[1] "Jul" "Aug" "Sep" "Oct" "Nov" "Dec"
```

- 이름붙이기

```R
벡터에 값에 names() 함수로 이름 붙이기

> absent <- c(8,2,0,4,1)
> names(absent)
NULL
> names(absent) <- c('mon','tue','wed','thu','fri')
> absent
mon tue wed thu fri 
  8   2   0   4   1 
> absent['mon'] #이름으로 값 추출
mon 
  8 

```

- any/all

```R
any(): 논리값이 하나라도 TRUE면 결과가 TRUE
all(): 논리값이 모두 TRUE면 결과가 TRUE

a <- -3:3
any(a>0) #TRUE
all(a>0) #FALSE
```



### 벡터 연산

- 원소끼리 연산 수행

| 연산자 | 기호   |
| ------ | ------ |
| %%     | 나머지 |
| %/%    | 몫     |
| /      | 나눗셈 |

```R
c(1,2,3) + c(4,5,6) 
# [1] 5 7 9

2*c(2,4,5)
# [1] 4 8 10

y<-c(2,4,6)
y/c(2,1,3)
#[1] 1 4 2
 
x<-c(1:3)
y<-c(4:9)
x+y
#[1]  5  7  9  8 10 12
#길이가 짧은쪽의 벡터가 긴쪽에 맞춰서 반복됨
c(1,3,5)+10
#[1] 11 13 15

factorial(1:5)
# 1 2 6 24 120
```

- 논리형

```R
x <- c(1,3,5)
y <- c(2,3,5)
x==y
#[1] FALSE  TRUE  TRUE
#true는 1, false는 0

> as.numeric(TRUE)
[1] 1
> TRUE+TRUE
[1] 2
```

```R
sum(): 벡터의 모든 요소의 합

> sum(1:5)
[1] 15
> sum(1:2, 3:5)
[1] 15
> sum(TRUE, FALSE, TRUE)
[1] 2

#활용 :벡터 x에서 50보다 큰 값의 개수 구하기
> x <- c(0, 25,50,100,200)
> x>50
[1] FALSE FALSE FALSE  TRUE  TRUE
> sum(x>50)
[1] 2

prod(): 벡터의 모든 요소의 곱
prod(1:5)
#120

mean() : 평균
median() : 중앙값
var() : 분산
sd() : 표준편차
range() : 범위
평균0과 표준편차1로 표준화 :  데이터-분산/표준편차
```

- 문자열 합치기

```R
paste()

> fruits <- c("gum","gu","bar")
> food <- c("pie","juice","cake")
> paste(fruits,food)
[1] "gum pie"  "gu juice" "bar cake"
> paste(fruits, "yay")
[1] "gum yay" "gu yay"  "bar yay"
```

- log()

```R
default 밑수는 e(2.718..)

> log(2:5)
[1] 0.6931472 1.0986123 1.3862944 1.6094379
#밑수 2
> log(2:5, base=2) 
> log2(2:5)
[1] 1.000000 1.584963 2.000000 2.321928

> #exp함수: 밑수가 e인 지수값
> y <- exp(1:5)
> log(y)
[1] 1 2 3 4 5
```

```R
factorial(1:5)
choose(5,2) #5개 중 2개를 선택하는 경우의 수 5C2
#nCr = n! / r!(n-r)!
```

- 유효자리수

```R
디폴트는 7
> options("digits")
$digits
[1] 7
> sqrt(1:5)
[1] 1.000000 1.414214 1.732051 2.000000 2.236068

#유효자릿수 지정
> signif(6.434, digits=3)
[1] 6.43
> signif(456.434, digits=2)
[1] 460
> signif(456.439, digits=5)
[1] 456.44
> round(456.434, digits=2)
[1] 456.43
> round(456.434, digits=3)
[1] 456.434

※ 반올림 숫자가 5인 경우 가까운 짝수로 반올림
round(11.5) #12
round(12.5) #12

# floor : 내림
# ceiling : 올림
# trunc : 버림
```

```R
r은 1.8*10의 308승까지 표현 가능

3/0 #Inf
is.infinite(3/0) #TRUE
```

- 특수한 값들

```R
NA : 결측값, 누락된 값
NaN : 정의가 불가능한 값
NULL : 정의되지 않음 (초기값)

> z <- c(1,2,3,4,NA)
> sum(z)
[1] NA
> range(z)
[1] NA NA
> median(z)
[1] NA
#중간에 NA에 있으면 연산 안됨
> sum(z, na.rm=TRUE) #NA 제외
[1] 10
> na.omit(z)
[1] 1 2 3 4
attr(,"na.action")
[1] 5
attr(,"class")
[1] "omit"
> sum(na.omit(z))
[1] 10
```

- 누적합

```R
cumsum():

> traffic.death <- c(10,20,30,20)
> cumsum(traffic.death)
[1] 10 30 60 80

#중간에 NA가 있으면 빼고 누적합 안됨
```

- 요소간의 차

```R
diff(, lag=) #lag=간격

> traffic.death <- c(10,20,30,20)
> diff(traffic.death)
[1]  10  10 -10

> 1:10
 [1]  1  2  3  4  5  6  7  8  9 10
> diff(1:10, lag=3) #7까지만 가능
[1] 3 3 3 3 3 3 3
```

- 집합

```R
> p <- 1:10
> q <- 6:15
> union(p,q) #합집합
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
> intersect(p,q) #교집합
[1]  6  7  8  9 10
> setdiff(p,q) #차집합
[1] 1 2 3 4 5
> setequal(p,q) #두 집합이 동일한지 확인
> is.element(1, p) #p안에 1 있음? ㅇㅇ
```



### 팩터

```
카테고리를 구분하는 범주형 데이터

levels : 팩터에 포함된 범주값
factor() : 문자/숫자 벡터를 범주형 데이터로 변형
```

```R
> review <- c('good','good','bad','ind','bad','good')
> review.factor <- factor(review)
> review.factor
[1] good good bad  ind  bad  good #따옴표 없어짐
Levels: bad good ind #알파벳 순 정렬
> str(review.factor)
 Factor w/ 3 levels "bad","good","ind": 2 2 1 3 1 2
> as.numeric(review.factor) #팩터형을 숫자형으로 전환
[1] 2 2 1 3 1 2

#levels 변경
> levels(review.factor) <- c('B','G','I')
> review.factor
[1] G G B I B G
Levels: B G I

#levels 길이
nlevels(review.factor)

#levels 지정
> everyday <- c('mon','mon','fri','fri','tue')
> everyday.factor <- factor(everyday, levels=c('mon','tue','wed','thu','fri','sat','sun'))
> everyday.factor
[1] mon mon fri fri tue
Levels: mon tue wed thu fri sat sun

#levels 빈도
table(everyday.factor)

#서열팩터 : 순서가 있는 범주형 데이터(부등호로 표시)
> eval <- c('medium','low','high','medium','high')
> eval.ordered <- factor(eval, levels=c('low','medium','high'),ordered=TRUE)
> eval.ordered
[1] medium low    high   medium high  
Levels: low < medium < high

#숫자벡터 -> 팩터로 변환
gender <- c(2,1,2,2,1,0)
> gender.factor <- factor(gender, levels=c(1,2), labels=c('male','female'))
> gender.factor
[1] female male   female female male   <NA>  
Levels: male female
```



## 행렬

```
2차원 벡터로 이루어진 자료구조로 매트릭스라고도 한다.
여러 주제로 데이터 수집이 가능하며 모든 자료의 종류가 동일하다. 
```



```R
> v <- 1:12

#dim()
> dim(v) <- c(3,4) #차원 정의
> v
     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10
[2,]    2    5    8   11
[3,]    3    6    9   12

#matrix()
> matrix(data=v, nrow=3, ncol=4) #열방향(default)
     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10
[2,]    2    5    8   11
[3,]    3    6    9   12

matrix(1:10,,5) #행이나 열 생략하면 자동으로 나머지에 맞춰짐
> matrix(data=v, nrow=3, ncol=4, byrow=TRUE) #행방향
> matrix(v, 3, 4, byrow=TRUE) #생략 가능
     [,1] [,2] [,3] [,4]
[1,]    1    2    3    4
[2,]    5    6    7    8
[3,]    9   10   11   12

#행 개수
new <- matrix(1:10,,5)
new[nrow(new)] #2
#열 개수
new[ncol(new)] #5

#행과 열에 이름 넣기
> rnames <- c('r1','r2','r3')
> cnames <- c('c1','c2','c3','c4')
> matrix(v,3,4,byrow=TRUE,dimnames=list(rnames,cnames))
   c1 c2 c3 c4
r1  1  2  3  4
r2  5  6  7  8
r3  9 10 11 12
```

```R
> matrix(0,3,4)
     [,1] [,2] [,3] [,4]
[1,]    0    0    0    0
[2,]    0    0    0    0
[3,]    0    0    0    0
> matrix(NA,3,4)
     [,1] [,2] [,3] [,4]
[1,]   NA   NA   NA   NA
[2,]   NA   NA   NA   NA
[3,]   NA   NA   NA   NA

> mat <- matrix(v,ncol=4)
> str(mat)
 int [1:3, 1:4] 1 2 3 4 5 6 7 8 9 10 ...
> mat
     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10
[2,]    2    5    8   11
[3,]    3    6    9   12
> dim(mat)
[1] 3 4
> dim(mat)[1]
[1] 3
> nrow(mat)
[1] 3
> ncol(mat)
[1] 4
> length(mat)
[1] 12
```

- 벡터+벡터

```R
> v1 <- 1:5
> v2 <- 6:10
> rbind(v1,v2)
   [,1] [,2] [,3] [,4] [,5]
v1    1    2    3    4    5
v2    6    7    8    9   10
> cbind(v1,v2)
     v1 v2
[1,]  1  6
[2,]  2  7
[3,]  3  8
[4,]  4  9
[5,]  5 10
```

- 벡터+행렬

```R
> cbind(1:3,4:6,matrix(7:12,3,2))
     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10
[2,]    2    5    8   11
[3,]    3    6    9   12

> rbind(matrix(1:6,2,3),matrix(7:12,2,3))
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6
[3,]    7    9   11
[4,]    8   10   12
```

### 호출

```R
> mat <- matrix(v,3,4)
> mat
     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10
[2,]    2    5    8   11
[3,]    3    6    9   12

> mat[1,]
[1]  1  4  7 10 #벡터
> mat[1,,drop=FALSE] #행렬 형태 유지
     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10
> mat[,c(1,4)] #1,4열만 출력
     [,1] [,2]
[1,]    1   10
[2,]    2   11
[3,]    3   12
> mat[,-c(2,3)] #2,3열만 제외
     [,1] [,2]
[1,]    1   10
[2,]    2   11
[3,]    3   12
```

### 연산

```R
> w <- c(1:6)      
> mtx <- matrix(w,2,3)
> mtx
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6

#행렬과 스칼라 (짧은쪽이 긴쪽에 맞춰진다)
> mtx+1
     [,1] [,2] [,3]
[1,]    2    4    6
[2,]    3    5    7

#행렬과 행렬 (반드시 차원이 같아야 한다)
> matrix(1:6,2,3)+matrix(6:1,2,3)
     [,1] [,2] [,3]
[1,]    7    7    7
[2,]    7    7    7
> matrix(1:6,2,3)*matrix(6:1,2,3) 
     [,1] [,2] [,3]
[1,]    6   12   10
[2,]   10   12    6

#행렬의 곱(%*%)은 앞행렬 열과 뒷행렬 행 개수가 일치해야한다
> matrix(1:6,2,3)%*%matrix(6:1,3,2)
     [,1] [,2]
[1,]   41   14
[2,]   56   20
```

### 속성

```R
> mtx
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6

#행열 반전
> t(mtx)
     [,1] [,2]
[1,]    1    2
[2,]    3    4
[3,]    5    6
#행의 합
> rowSums(mtx)
[1]  9 12
#열의 합
> colSums(mtx)
[1]  3  7 11
#행 중간값
> rowMeans(mtx)
[1] 3 4
#열 중간값
> colMeans(mtx)
[1] 1.5 3.5 5.5
```



### 다차원 배열

- dim()

```R
> a <- 1:24
> dim(a) <- c(3,4,2) #3차원, 2개의 면(테이블), 3행 4열
> a
, , 1

     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10
[2,]    2    5    8   11
[3,]    3    6    9   12

, , 2

     [,1] [,2] [,3] [,4]
[1,]   13   16   19   22
[2,]   14   17   20   23
[3,]   15   18   21   24
```

- array()

```R
> ary -> array(1:24, c(3,4,2))
> ary

, , 1
     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10
[2,]    2    5    8   11
[3,]    3    6    9   12

, , 2
     [,1] [,2] [,3] [,4]
[1,]   13   16   19   22
[2,]   14   17   20   23
[3,]   15   18   21   24

> ary[1,,] #모든 면의 1행들이 출력됨
     [,1] [,2]
[1,]    1   13
[2,]    4   16
[3,]    7   19
[4,]   10   22

#테이블 유지하려면 drop=FALSE
> ary[1,,,drop=FALSE]
, , 1
     [,1] [,2] [,3] [,4]
[1,]    1    4    7   10

, , 2
     [,1] [,2] [,3] [,4]
[1,]   13   16   19   22
```



## 리스트

```
벡터와 행렬은 원소의 데이터 타입이 모두 같아야 하지만
리스트는 다양한 데이터 타입을 저장할 수 있다.
```

### 생성

```R
> lst <- list(0.6,0.9,'fruits')
> lst
[[1]]
[1] 0.6

[[2]]
[1] 0.9

[[3]]
[1] "fruits"

n <- c('n1','n2','n3')
v <- c(100,200,300)
mylist <- list()
mylist[n] <- v
> mylist
$n1
[1] 100
$n2
[1] 200
$n3
[1] 300
```

### 추가/수정

```R
> lst[[3]] <- 'apple'
> lst[[4]] <- matrix(1:6,2,3)
> lst
[[1]]
[1] 0.6

[[2]]
[1] 0.9

[[3]]
[1] "apple"

[[4]]
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6

#하나의 원소에 값을 추가/수정할때는 [[]],[] 둘다 가능

#하나의 원소에 여러개의 값을 할당할때 [[]],[]는 다름
#[[]]는 벡터 형식으로 줘야하고
#[]는 리스트 형식으로 변환해야함
> prod[[3]] <- c(40000,50000)
> prod[3] <- list(c(20000,30000))

#두 개 이상의 원소 값 동시 변경할때는 [] 사용
> prod[1:3] <- list('a02','monitor',10000) #리스트를 넣으면 형식 유지
[[6]]
[1] 0.1
[[7]]
[1] 0.2
[[8]]
[1] "0.3"

> prod[6:8] <- c(0.1,0.2,'0.3') #벡터로 넣으면 데이터 형식 자동 통일됨
[[6]]
[1] "0.1"
[[7]]
[1] "0.2"
[[8]]
[1] "0.3"

#제거 : NULL 할당
prod[4] <- NULL
mylist[mylist<200] <- NULL #조건에 따른 원소제거 #근데 원소내 원소개수가 하나여야가능
```

### 이름붙이기

```R
> names(lst) <- c('n1','n2','n3')
> lst
$n1
[1] 0.6

$n2
[1] 0.9

$n3
[1] "apple"

# $로 요소 참조 가능
> lst$n1
[1] 0.6

#이름 확인
> names(lst)
[1] "n1" "n2" "n3" "n4"

#길이 확인
> length(lst)
[1] 4

#만들면서 이름 붙이기
> prod <- list(id='a001',name='mouse',price=3000)
> prod
$id
[1] "a001"

$name
[1] "mouse"

$price
[1] 3000
```

### 참조

```R
lst[[n]] : n번째 원소가 원소 저장형식 그대로 가짐
lst[n] : n번째 원소가 리스트 형식으로 출력
※자료구조가 다름

prod <- list('a1','mouse',3000)
> prod[[3]]
[1] 3000
> prod[2]
[[1]]
[1] 3000

> class(prod[[3]]) #연산가능
[1] "numeric"
> class(prod[3]) #리스트임
[1] "list"
```

```R
> prod[c(1,2)]
[[1]]
[1] "a1"
[[2]]
[1] "mouse"

> prod[c(TRUE,FALSE,TRUE)]
[[1]]
[1] "a1"
[[2]]
[1] 3000

> prod[-1]
[[1]]
[1] "mouse"
[[2]]
[1] 3000

#이름으로 참조
> prod$name
[1] "mouse"

> prod[['name']]
[1] "mouse"

> prod['name'] #리스트형식
$name
[1] "mouse"

#2개 이상의 원소 참조
> prod[c('name','price')]
$name
[1] "mouse"
$price
[1] 3000

#없는 이름은 NULL
#첨자 허용 넘어가면 에러
> prod[5]
$<NA>
NULL

> prod[[5]]
Error in prod[[5]] : 첨자의 허용 범위를 벗어났습니다
```

### 연산

```R
R의 수치연산 함수들은 대부분 벡터 자료구조에 적용 가능하다.
따라서 리스트로 저장된 데이터를 연산하려면, 벡터로 변한해야한다.
unlist() : 리스트 -> 벡터

mydata <- list(1.5,2.0,3.5,4.5)
mean(unlist(mydata))
max(unlist(mydata))
```



## 데이터프레임

```
행과 열로 구성된 2차원 구조.
행렬은 모든 데이터 타입이 일치하는데 반해, 데이터 프레임은 서로 다른 데이터 타입이 입력 가능하다.
동일한 길이의 벡터로 이루어진 2차원 리스트와 같은 것. 
```

```R
이미지 데이터라면? 100*100이라면

  x1 x2 ... x10000
0  0 20 ... 255
1  0 20 ... 255
...
99 0 20 ... 255

- variable(feature)는 10000
- obs(instance,object)는 관측치 (몇장인지)
- 각 이미지의 차원은 10000차원
- 각각의 이미지가 10000차원 공간의 (0,2.,...,255) 위치에 점으로 표시됨
- 점 사이의 거리를 구할 수 있다. 가까운 점이 유사한 이미지
- 두 점 사이의 거리는 피타고라스의 정리로 구하듯
- 만 차원이니까 유클리디안 거리 또는 코사인 유사도 등의 알고리즘 기반 거리 계산으로 이미지 유사도 분석 가능
```

### 속성

```R
v1 <- c('a1','a2','a3')
v2 <- c(10,20,30)
v3 <- c('x','y','z')

1. 벡터들 연결해서 데이터프레임 만들기
data.frame(id=v1, name=v2, price=v3) #열이름 지정
  id name price
1 a1   10     x
2 a2   20     y
3 a3   30     z

data.frame(row.names=v1,v2,v3) #행이름 지정
   v2 v3
a1 10  x
a2 20  y
a3 30  z

2. as.data.frame() : 행렬, 리스트로 데이터프레임 만들기
lst <- list(v1,v2,v3)
p <- as.data.frame(lst)
  c..a1....a2....a3.. c.10..20..30. c..x....y....z..
1                  a1            10                x
2                  a2            20                y
3                  a3            30                z
#열이름 만들기
colnames(p) <- c('id','name','price')
  id name price
1 a1   10     x
2 a2   20     y
3 a3   30     z

#열 개수
length(p) #3 (행렬은 전체 원소 수)

stringAsFactors=TRUE #문자열을 팩터로 읽는다.
> p <- data.frame(id=v1, price=v2, name=v3, stringsAsFactors = TRUE)
> str(p)
'data.frame':	3 obs. of  3 variables: #3행 3열
 $ id   : Factor w/ 3 levels "a1","a2","a3": 1 2 3
 $ price: num  10 20 30
 $ name : Factor w/ 3 levels "x","y","z": 1 2 3
```

### 추가/수정

```R
id<-c('a1','a2','a3')
price<-c(10,20,30)
name<-c('x','y','z')
product <- data.frame(id,price,name)
#요소 하나 추가
#데이터프레임명 <- rbind(데이터프레임명, 넣을 요소)
product <- rbind(product, c('a4',40,'k'))

#여러 줄 추가
#데이터프레임명 <- rbind(데이터프레임명, 넣을 데이터프레임)
add <- data.frame(id=c('a4','a5','a6'),price=c(40,50,60),name=c('k','l','m'))
product <- rbind(product, add)

#요소 제거
product <- product[-4,] #4행 제거

#문자형 -> 숫자형 변환
product$price <- as.numeric(product$price)

#여러 데이터프레임들 합쳐서 데이터프레임 만들기 #리스트 내용물을 합치는것
do.call(함수, 인수)
df1 <- data.frame(gender='f',months=1,weight=55)
df2 <- data.frame(gender='f',months=3,weight=58)
df3 <- data.frame(gender='m',months=4,weight=105)
df4 <- data.frame(gender='m',months=10,weight=75)
df5 <- data.frame(gender='f',months=12,weight=85)
lst <- list(df1,df2,df3,df4,df5)
do.call(rbind,lst)

#여러 리스트 합쳐서 데이터프레임 만들기
lst1 <- list(gender='f',months=1,weight=55)
lst2 <- list(gender='f',months=3,weight=58)
lst3 <- list(gender='m',months=4,weight=105)
lst4 <- list(gender='m',months=10,weight=75)
lst5 <- list(gender='f',months=12,weight=85)
lstt <- list(lst1,lst2,lst3,lst4,lst5)

#lstt 안의 모든 list를 dataframe으로 변환해줘야함
lapply(리스트, 적용함수) : 리스트에 함수 적용
lapply(lstt,as.data.frame) #위의 lst와 같이 변환된 상태임
do.call(rbind, lapply(lstt,as.data.frame))

#행을 열로 바꿔 추가하기(행도 데이터로 쓰기)
state.x77 
class(state.x77) #matrix임
states <- data.frame(state.x77) #데이터프레임으로 변환
str(states)
row.names(states) #행 이름 벡터로 출력
states$name <- row.names(states) #행 이름 열에 추가
row.names(states) <- NULL #행 지우기
states
```

### 인덱싱

```R
리스트 인덱싱, 행렬 인덱싱 다 적용 가능

#패키지에 데이터셋 들어있음
state.abb #미국 주 약자
state.name
state.region
str(state.region) #팩터임

us.state <- data.frame(state.abb,state.name,state.region,state.area)

#열 추출
us.state[['state.name']] #벡터 형식
us.state['state.name'] #데이터프레임 형식
us.state[c(2,3)] #여러 열 추출

#행렬 인덱싱 사용 가능
us.state[,2,drop=FALSE]
us.state[,2]
us.state[c('state.name','state.abb')] #리스트 인덱싱
us.state[,c('state.name','state.abb')] #행렬 인덱싱
```

### 추출

```R
#열평균 추출
cats
colMeans(cats[2:3], na.rm=T)

#자료 부분 추출
states <- data.frame(state.x77)
head(states) #상위 6개 자료
tail(states,10) #하위 10개 자료

#states에서 income이 5000달러 이상인 자료 전체 출력
states[states$Income>=5000,]

#states에서 income이 5000달러 이상인 자료의 name과 income 출력
rich <- states[states$Income>=5000,c('name','Income')]

#states에서 area가 100000 이상인 자료의 name과 area 출력
large <- states[states$Area>=100000,c('name','Area')]

#merge로 합쳐서 추출 (기본값 : 공통으로 열(name)이 일치하는 자료)
merge(rich,large) #교집합
merge(rich,large,all=TRUE) #합집합

부분집합 subset
#subset은 다양한 조건 붙일 수 있음
subset(데이터셋,조건,출력할 열이름)으로 출력 #default는 all 

#income이 5000넘고 Area가 50000 넘는 자료의 모든 정보 추출
subset(states, Income>5000 & Area>50000)

#name이 Alaska인 자료의 모든 정보 추출
subset(states, name=='Alaska')

#income이 5000넘는 주의 murder와 문명률 추출
subset(states, subset=(Income>5000), select=c(Murder,Illiteracy))
subset(states, select=c(Murder,Illiteracy), subset=(Income>5000))
#순서바꿔도 괜찮음. 생략할때는 순서지켜야함

#연습
#cyl가 4이고 am이 0인 mtcars자료의 mpg,hp,wt 출력
mtcars[mtcars$cyl==4&mtcars$am==0,c('mpg','hp','wt')] #열이름에 ''
subset(mtcars,cyl==4&am==0,c(mpg,hp,wt)) #그냥씀

```

```R
class(iris)
subset(iris,select=-c(Sepal.Width,Petal.Length))
iris$Sepal.Length/iris$Sepal.Width #비율
#특성공학: 주어진 데이터 칼럼으로부터 연산을 수행하여 새로운 칼럼만듦

#with(): 여러개의 명령 한번에 실행, iris$생략
with(iris,Sepal.Length/Sepal.Width)
with(iris, {
  print(summary(Sepal.Length))
  plot(Sepal.Length, Sepal.Width)  
})

#기술통계
summary(iris$Sepal.Length)

with(iris,{
  stats <<-summary(Sepal.Length)
  stats
})
#<<- : 현재 속해있는 변수환경 하나 위에 있는 환경에 있는 변수에 값을 부여할 때
stats

iris$Sepal.Ratio <- iris$Sepal.Length/iris$Sepal.Width
iris <- within(iris, Sepal.Ratio <- Sepal.Length/Sepal.width)
iris
#with, within은 거의 동일(코드의 양 줄여줌)
#within은 데이터 수정 가능

#Sepal.Ratio가 na이면 중앙값으로 대체
within(iris,{     
    Sepal.Ratio=ifelse(is.na(Sepal.Ratio),#조건
                median(Sepal.Ration,na.rm=T), #참
                Sepal.Ratio) #거짓
})
```

- SQL 패키지

```R
#sqldf패키지 : SQL 명령문 사용 가능
install.packages('sqldf') #패키지 설치
library(sqldf)
#Structured Query Language : 데이터베이스에 데이터를 검색/수정/삭제/추가 작업
#수행하는 질의어

sqldf('select * from mtcars', row.names=T)
sqldf('select cyl from mtcars', row.names=T)
sqldf('select * from mtcars where mpg>30 order by hp', row.names=T)
sqldf('select avg(mpg) as avg_mpg from mtcars where mpg>30 group by cyl', row.name=T)
```

### 정렬

```R
sort() #정렬. 데이터프레임 사용 x
order() #정렬 색인 값 추출. 데이터프레임 정렬에서 사용
arrange() #plyr 패키지에 있는 정렬 함수

v1 <- c(20,60,45,10,15)
v2 <- c(300,200,100,700,600)
v3 <- c('a','b','c','d','f')
df <- data.frame(v1,v2,v3)

sort(v1) #벡터 정렬
sort(v1,decreasing=T)

order(v1) #벡터 정렬
order(-v1) #내림차순
df[order(v1),] #데이터프레임 정렬
df[order(v1,-v2,v3),] #우선순위

install.packages('plyr') #설치
library(plyr) #호출
arrange(df,v1,desc(v2),v3) #우선순위

```

### 표준화/정규화

```R
표준화(평균:0, 표준편차:1) = (각 열 data - 각 열 평균) / 각 열 표준편차

#iris 표준화
iris.mean <- c(mean(iris$Sepal.Length),mean(iris$Sepal.Width),mean(iris$Petal.Length),mean(iris$Petal.Width))
iris.sd <- c(sd(iris$Sepal.Length),sd(iris$Sepal.Width),sd(iris$Petal.Length),sd(iris$Petal.Width))
iris.temp <- t(iris[1:4])
iris.std <- (iris.temp-iris.mean)/iris.sd #표준화된 iris[1:4]. vector

#비교하려는 벡터 ex도 iris로 표준화
ex <- c(4.0, 3.0, 1.5, 0.15)
ex.std <- (ex-iris.mean)/iris.sd

#표준화 함수 scale()
scale(iris[1:4]) #matrix
cbind(iris, scale=scale(iris[,-5])) #5열만 제외한건 cbind로 연결

```

- apply()

```R
mean(iris[,-5])
경고메시지(들): 
In mean.default(iris[, -5]) :
  인자가 수치형 또는 논리형이 아니므로 NA를 반환합니다
데이터프레임에 mean 안됨. 열단위로 함수 적용할 때는 apply 함수

#apply(데이터, 행(1)/열(2), 함수)
apply(iris[,-5],2,scale) #데이터프레임에 열 단위로 scale함수 적용
apply(iris[,-5],2,function(x){x-mean(x,na.rm=T))/sd(x)})

#유클리디언 거리
iris$distance <- sqrt(colSums(iris.std-ex.std)^2)
head(iris[order(iris$distance),],9)
--------------------------------------------------------------------
정규화 = (각 열 data - 각 열 최소값) / (각 열 최대값 - 각 열 최소값)

#apply에 함수 넣어서 한방에 해결
apply(iris[,-5],2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})
```









