# R

- 데이터 분석에 적합함. 시각화나 딥러닝에는 무거워서 파이썬을 많이 씀
- 

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

## 벡터 속성

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

- 인덱싱

```R
prime <- c(2,3,5,7,11,13,17)

idx <- c(3,4,5)
prime[idx] #5 7 11
prime[3:5] #5 7 11
prime[-(3:5)] #3~5번 인덱스 제외

> #마지막꺼 빼기
> prime[-length(prime)]
[1]  2  3  5  7 11 13
> #값 변경
> prime[c(3,4)] <- c(30,40)
> prime
[1]  2  3 30 40 11 13 17
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
median() : 중간값
var() : 상관계수?
sd() : 표준편차
range() : 범위
```

- any/all 함수

```R
any(): 논리값이 하나라도 TRUE면 결과가 TRUE
all(): 논리값이 모두 TRUE면 결과가 TRUE

a <- -3:3
any(a>0) #TRUE
all(a>0) #FALSE
```

- 문자열 합치기 paste()

```R
zip 같은??

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
#NA 제외하고 더하기
> sum(z, na.rm=TRUE)
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







