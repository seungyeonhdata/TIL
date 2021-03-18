# 데이터 전처리



## 모델링

```
모델링과정

1)데이터를 훈련용(70%)/테스트용(30%)으로 분할 
(샘플함수로 무작위 표본추출)
sample(x,size,replace=F) 
x=벡터형식 표본, size=표본의 개수 ,replace=복원추출 여부

2) 훈련용 데이터만으로 모델(예측/분류)을 생성
과적합(오버피팅) : 훈련데이터 평가결과>>테스트 데이터 평가결과
원인 :  데이터부족 ->보충 필요, 변수가 너무 많음 -> 차원 축소

3)테스트
```





## 난수 발생

```R
#seed값을 동일하게 주면 매번 난수가 동일하게 추출
set.seed(20210303)
sample(1:10)
#1~10 데이터로 할때
#전처리 -> 랜덤 : 124579번 추출해서 훈련데이터 ->모델-> 평가(3,8,10)

#정확도를 같은 데이터로 계속 알아봐야함
set.seed(1)
sample(1:10,5,replace=T) #복원추출

#데이터프레임 열로부터 표본 추출
sample(iris,3)

#데이터프레임 행으로부터 표본 추출
set.seed(1)
index <- sample(1:nrow(iris),5) #행 번호 추출
iris[index,]
```

- library(dplyr)

```R
sample_n() : random sample rows for a fixed number
sample_frac() : random sample rows for a fixed fraction
#default는 비복원추출, 복원추출은 replace=T

#Cars93에서 1~5번째 변수만 사용해서 10개의 관측치 무작위 추출
sample_n(Cars93[, 1:5], 10)

#Cars93에서 1~5번째 변수만 사용해서 10%의 관측치 무작위 추출
sample_frac(Cars93[ , 1:5], 0.1)
```



## apply 함수

: 데이터에 함수를 적용하는 함수

- apply()

```R
적용하려는 데이터가 행렬이나 배열일 때 사용가능
#결과값이 벡터, 행렬
x <- 1:24
dim(x) <- c(4,3,2)
x
apply(x,1,max)
apply(x,1,paste,collapse=',') #1:행
apply(x,2,paste,collapse=',') #2:열
apply(x,3,paste,collapse=',') #3:면

apply(x,c(1,2),paste,collapse=',') #행과 열이 교차하는 부분에 함수적용
#결과값 : 행렬

#4차원 데이터 Titanic
str(Titanic)

#등급별 탑승 인원 파악
apply(Titanic,1,sum)

#승객 등급별 생존자 통계
apply(Titanic,c(1,4),sum)
```

- lapply()

```R
#lapply(데이터,함수)
#리스트형식
#데이터프레임에 적용 가능
#함수를 각 열에 모두 적용
exams <- list(s1=c(80,70,60,50,100),
     s2=c(80,40,60,50),
     s3=c(30,70,60,50,100,90),
     s4=c(80,60,60,50,100))
lapply(exams,length)
lapply(exams,mean)
lapply(exams,sd)
lapply(iris,scale)
lapply(iris,class)

lapply(iris,mean)
```

- sapply()

```R
sapply() : 길이가 모두 1이면 벡터, 
길이가 2이상이면서 모두 같은경우 행렬
길이가 2이상이면서 서로 다른경우 리스트로 출력
#데이터프레임에 적용 가능

exams <- list(s1=c(80,70,60,50,100),
     s2=c(80,40,60,50),
     s3=c(30,70,60,50,100,90),
     s4=c(80,60,60,50,100))
     
sapply(exams,length)
sapply(exams,mean)
sapply(exams,sd)

s4=c(80,60,60,50,100)
range(s4)
sapply(exams,range)

sapply(iris,class)

sapply(iris,mean)
sapply(iris,function(x) ifelse(is.numeric(x),mean(x),NA)) #경고안나오게
```

- mapply()

```R
#mapply(): 함수가 벡터 연산을 지원하지 않을때 유용
mapply(rep,1:4,4:1)

[[1]]
[1] 1 1 1 1

[[2]]
[1] 2 2 2

[[3]]
[1] 3 3

[[4]]
[1] 4

```

- 그룹 분할 작업 -> 그룹별 연산 작업 동시 진행 가능
  - `tapply()`, `aggregate()`, `by()`
- tapply()

```R

#tapply(x,팩터(리스트도 가능),함수)
tapply(iris$Sepal.Length,iris$Species,mean)

tapply(iris$Sepal.Length,iris$Species,length)
car
with(car,tapply(mpg,list(cyl,am),mean))
#group명 저절로 들어감
```



## 요약

### split()

```R
#-------집단 요약------------------
#벡터를 집단별로 분할(split, unstack)
data(mtcars)
car <- mtcars
car <- within(car,
       am <- factor(am,
              levels=c(0,1),
              labels=c('Auto','Manual'))
      )
car

#split(x,factor,drop=F)
g <- split(car$mpg,car$am) #list
mean(g[['Manual']])
data.frame(split(iris$Sepal.Length,iris$Species))
```

### unstack()

```R
#unstack(x,f,...)
#그룹별로 분할된 데이터의 길이가 동일하면 데이터프레임
#다르면 리스트로 출력
df <- data.frame(car$mpg,car$am)
g1 <- unstack(df) #list
g1
summary(g1) #리스트는 요약 안됨
class(iris$Species)
g2 <- unstack(data.frame(iris$Sepal.Length,iris$Species)) #dataframe
g2
summary(g2) #데이터프레임은 요약됨


```

### table()

```R
#xtabs :table함수와 동일한 기능 
#포물러사용 : 데이터 처리시 어떤 열 사용할 건지 나타낸 수식
xtabs(formula=~., data=parent.frame(), subset)
xtabs(~am+gear,car) #am과 gear 조합한 테이블

#---prop.table--------
#비율. 더해서 1. 행기준 : 1, 열기준 : 2
mydata<-matrix(sample(100,15), ncol=3)
colnames(mydata)<-LETTERS[seq(1,3)]
mydata
#sprintf()
rownames(mydata)<-sprintf("s-%d",seq(5))
mydata

prop.table(mydata)
sum(prop.table(mydata))
library(dplyr)
prop.table(mydata) %>% sum

prop.table(mydata, 1) #행 기준으로 비율
prop.table(mydata, 2) #열 기준으로 비율

rowSums(prop.table(mydata, 1))
prop.table(mydata, 1) %>% rowSums

colSums(prop.table(mydata, 2))
prop.table(mydata, 2) %>% colSums
```



- transform()

```R
데이터 셋 내 형변환/연산 한꺼번에 정의
transform(iris.copy,
          Species=as.character(Species),
          Sepal.Ratio=Sepal.Length/Sepal.Width)
```

**<그룹별 분할 작업>**

### aggregate

```R
#aggregate(벡터,by=집단변수를 리스트형식으로,함수)
with(car,aggregate(mpg,list(Cyl=cyl,Transmission=am),mean))
#group명이 없음

#car[c(1:6)] 변수의 평균, 실린더 개수와 변속기 유형의 조합에 따라
car[c(1:6)]
aggregate(car[c(1:6)],list(car$cyl,car$am),mean)

#꽃 종류별 측정 변수별 요약
aggregate(iris[-5],list(Species=iris$Species),mean)
```

### by()

```
#by(data,팩터나 리스트,함수)
?by
by(iris, iris$Species,summary)
by(iris, iris$Species,function(x) mean(x$Sepal.Length))
```

- rowsum()

```
#rowsum(x,group)
rowsum(iris[-5],iris$Species)
```

- tabulate()

```R
#범주별 관측값 개수
tabulate()
gc <- tabulate(car$gear)
table(car$gear)
names(gc) <- 1:length(tabulate(car$gear))
gc
table(car$am, car$gear)
```

#### formula

```R
~..+..

#cyl와 am 열로 mpg열의 평균 구하기
aggregate(mpg~cyl+am, car, mean)
with(car,aggregate(mpg,list(Cyl=cyl,am=am),mean)) #포뮬러 없이
```



## dplyr 패키지

: 데이터프레임의 분할(split)-적용(apply)-결합(combine)  SAC 작업 용이

```
library(dplyr)
```

### %>%

```R
여러 단계의 절차를 필요로 해서 중간 결과를 저정 후 그 객체를 후속 절차에서 받아서 사용해야 하는 경우의 프로그래밍의 경우 chain operation %>%이 유용

예시)
"(a) Cars93 데이터프레임에서  %>%  (b) 제조생산국(Origin), 차종(Type), 실린더개수(Cylinders)별로   %>%   (c) 차 가격(Price)과 고속도로 연비(MPG.highway) 변수에 대해   %>%   (d)  (결측값은 제외하고) 평균을 구하는데,   %>%   (e) 단, 가격 평균은 10을 넘거나 or 고속도로 연비평균은 25를 넘는 것만 알고 싶다"

Cars93 %>%  # dataframe name
  group_by(Origin, Type, Cylinders) %>%  # group_by()
  select(Price, MPG.highway) %>%  # select() columns
  summarise(
    Price_m = mean(Price, na.rm = TRUE),
    MPG.highway_m = mean(MPG.highway, na.rm = TRUE)  # summarise()
  ) %>%
  filter(Price_m > 10 | MPG.highway_m > 25)  # filter() condition

풀어쓰면

library(dplyr)
library(MASS)
select <- dplyr::select
str(Cars93)
a1 <- group_by(Cars93,Origin,Type,Cylinders)
a2 <- select(a1,Price,MPG.highway)
a3 <- summarise(a2,
                Price_m=mean(Price,na.rm=T),
                MPG.highway_m=mean(MPG.highway,na.rm=T))
a4 <- filter(a3, Price_m>10|MPG.highway_m>25)

참고)
Python이나 Scala로 Spark 사용할 때 보면 '.' (dot) 을 이용해서 chain operation 가능, R의 '%>%'과 사용방법이 유사 

 [Spark에서 Python으로 map과 reduceByKey를 chaining 해서 단어 세기] 예시

rdd = sc.textFile("file")
words = rdd.flatMap(lambda x: x.split(" "))
result = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
```

### 추출

:{base}의 subset()과 같은 기능

**열 단위 추출**

- select() :select columns

```R
#필요한 열만 추출

df <- read.csv('train.csv',na.string='')
df <- select(df,Survived,Pclass,Age,Sex,SibSp,Parch)
library(Amelia)
missmap(df,col=c('red','grey'))
```

| verbs                    | description                                          |
| ------------------------ | ---------------------------------------------------- |
| select(df,starts_with()) | select columns that `start` with a prefix            |
| select(df,ends_with())   | select columns that `end` with a prefix              |
| select(df,contains())    | select columns that contain a `char string`          |
| select(df,matches())     | select columns that match a `regular expression`     |
| select(df,one_of())      | select columns that are from `a group of names`      |
| select(df,num_range())   | select columns from `num_range a to n` with a prefix |

```R
'xx_name'은 대소문자 구분 안함
select(df, start_with('s')) #Survived, Sibsp, Sex 열 나옴
select(df, ends_with('s')) #Pclass 열
select(df, contains('s')) #Survived, Sibsp, Sex, Pclass, PassengerId
select(df, matches('.p')) #Sibsp만

vars <- c('Survived','Dead','Sex')
select(df, one_of(vars)) #Survived, Sex 열
Warning message:
In one_of(vars) : Unknown variables: `Dead`

select(df,2:4) #서로 인접해서 줄지어 있는 변수들의 경우
select(df,Survived:Name)
select(df,-(2:4))

#동일한 접두사를 사용하는 변수들인 경우
select(df, num_range("V", 2:3)) #V2,V3열 추출
```

- distinct() : {base}의 unique()

```R
중복 제거하여 행 추출
distinct(df, var1) #
dictinct(df, var1, var2)
> # distinct(dataframe, var1, var2) :  find unique values in a table
> 
> distinct(Cars93, Origin)
   Origin
1 non-USA
2     USA
> 
> distinct(Cars93, Type)
     Type
1   Small
2 Midsize
3 Compact
4   Large
5  Sporty
6     Van
> 
> distinct(Cars93, Origin, Type)
    Origin    Type
1  non-USA   Small
2  non-USA Midsize
3  non-USA Compact
4      USA Midsize
5      USA   Large
6      USA Compact
7      USA  Sporty
8      USA     Van
9      USA   Small
10 non-USA  Sporty
11 non-USA     Van
```

**행 단위 추출**

- filter() : filter rows with condition

```R
filter(dataframe, filter condition1, filter condition2,...)
airquality
air <- filter(airquality,Month==6,Temp>90) #,는 and 연산, &도 가능
air <- filter(airquality,Month==6|Temp>90) # or
head(air)
{base} subset(airquality,Month==6)
```

- slice() : filter rows with position

```R
slice(dataframe,from,to)
Cars93_1
slice(Cars93_1,6:10) #6번부터 10번 행
```

### 정렬

- arrange() 

```R
{base}의 order()과 같은 기능
arrange(Cars93_1, desc(MPG.highway), Max.Price)
```

### 수정/추가

- rename()

```R
#열 이름 변경
rename(x,바꾼 후=바꾸기 전)
rename(midwest,total=poptotal,asian=popasian)
```

- mutate() 

```R
mutate(dataframe, 새로운변수 = 기존변수 조합한 수식,...)
#{base}의 transform() 기능
create(add) new columns and refer to columns that you just created
=기존변수 + 신규변수 모두 keep
하나의 함수 명령문 안에서 신규로 생성한 변수를 바로 다른 신규 생성 변수의 input 변수로 사용할 수 있어 편리 (transform()은 안됨)

exam %>% 
  mutate(total=math+english+science,
         test=ifelse(science>=60,'pass','fail')) %>% 
  arrange(total)
```

- transmute()

```
transmute(dataframe, 새로운 변수 = 기존 변수 조합한 수식,...)
create(add) new columns and only keeps the new columns
= 신규 변수만 keep
```

- left_join()

```R
열 합침
# 중간고사 데이터 생성
test1 <- data.frame(id = c(1, 2, 3, 4, 5),
                    midterm = c(60, 80, 70, 90, 85))
# 기말고사 데이터 생성
test2 <- data.frame(id = c(1, 2, 3, 4, 5),
                    final = c(70, 83, 65, 95, 80))

left_join(test1,test2,by='id')

name <- data.frame(class = c(1, 2, 3, 4, 5),
                   teacher = c("kim", "lee", "park", "choi", "jung"))
left_join(name,exam)
```

- bind_rows()

```R
행 합침

# 학생 1~5 번 시험 데이터 생성
group_a <- data.frame(id = c(1, 2, 3, 4, 5),
                      test = c(60, 80, 70, 90, 85))
# 학생 6~10 번 시험 데이터 생성
group_b <- data.frame(id = c(6, 7, 8, 9, 10),
                      test = c(70, 83, 65, 95, 80))
bind_rows(group_a,group_b)
```



### 요약

```R
수치형 데이터에 대한 요약 통계량
 - mean(x, na.rm = TRUE) : 평균
 - median(x, na.rm = TRUE) : 중앙값
 - sd(x, na.rm = TRUE) : 표준편차
 - min(x, na.rm = TRUE) : 최소값
 - max(x, na.rm = TRUE) : 최대값
 - IQR(x, na.rm = TRUE) : 사분위수 (Inter Quartile Range = Q3 - Q1)
 - sum(x, na.rm = TRUE) : 합, 결측값을 제외하고 계산하려면 na.rm = TRUE 추가

[예제] Cars93 데이터 프레임에서 가격(Price)의 (a) 평균, (b) 중앙값, (c) 표준편차, (d) 최소값, (e) 최대값, (f) 사분위수(IQR), (g) 합계를 구하시오. (단, 결측값은 포함하지 않고 계산함)

> summarise(Cars93, 
+           Price_mean = mean(Price, na.rm = TRUE), 
+           Price_median = median(Price, na.rm = TRUE), 
+           Price_sd = sd(Price, na.rm = TRUE), 
+           Price_min = min(Price, na.rm = T), 
+           Price_max = max(Price, na.rm = T), 
+           Price_IQR = IQR(Price, na.rm = T), 
+           Price_sum = sum(Price, na.rm = TRUE)) 

  Price_mean Price_median Price_sd Price_min Price_max Price_IQR na.rm 
1   19.50968         17.7  9.65943       7.4      61.9      11.1  TRUE 
  Price_sum
    1814.4
```

```R
개수 계산, 관측값 indexing
- n() : 관측치 개수 계산, x 변수 입력하지 않음
- n_distinct(x) : 중복없는 유일한 관측치 개수 계산, 기준이 되는 x변수 입력함
- first(x) : 기준이 되는 x변수의 첫번째 관측치
- last(x) : 기준이 되는 x변수의 마지막 관측치
- nth(x, n) : 기준이 되는x변수의 n번째 관측치 

[예제] Cars93_1 데이터 프레임에서 (a) 총 관측치의 개수, (b) 제조사(Manufacturer)의 개수(유일한 값), (c) 첫번째 관측치의 제조사 이름, (d) 마지막 관측치의 제조사 이름, (e) 5번째 관측치의 제조사 이름은?

> # summarise() : n(), n_distinct(), first(), last(), nth()
> Cars93_1 <- Cars93[c(1:10), c("Manufacturer", "Model", "Type")] # subset for better print
> Cars93_1
   Manufacturer      Model    Type
1         Acura    Integra   Small
2         Acura     Legend Midsize
3          Audi         90 Compact
4          Audi        100 Midsize
5           BMW       535i Midsize
6         Buick    Century Midsize
7         Buick    LeSabre   Large
8         Buick Roadmaster   Large
9         Buick    Riviera Midsize
10     Cadillac    DeVille   Large
> 
> summarise(Cars93_1,
+           tot_cnt = n(), # counting the number of all observations
+           Manufacturer_dist_cnt = n_distinct(Manufacturer), # distinct number of var
+           First_obs = first(Manufacturer), # first observation
+           Last_obs = last(Manufacturer), # last observation
+           Nth_5th_obs = nth(Manufacturer, 5)) # n'th observation

  tot_cnt Manufacturer_dist_cnt First_obs Last_obs Nth_5th_obs
1      10                     5     Acura Cadillac         BMW
```

```R
그룹별 요약 통계량
summarise(group_by(dataframe, factor_var), mean, sd, ...)

[예제] Cars93 데이터 프레임에서 '차종(Type)' 별로 구분해서 (a) 전체 관측치 개수, (b) (중복 없이 센) 제조사 개수, (c) 가격(Price)의 평균과 (d) 가격의 표준편차를 구하시오. (단, 결측값은 포함하지 않고 계산함)

> grouped <- group_by(Cars93, Type)
> summarise(grouped,
+           tot_conut = n(), # counting the number of cars
+           Manufacturer_dist_cnt = n_distinct(Manufacturer), # distinct number of var
+           Price_mean = mean(Price, na.rm = TRUE), 
+           Price_sd = sd(Price, na.rm = TRUE))

# A tibble: 6 x 5
     Type tot_conut Manufacturer_dist_cnt Price_mean  Price_sd
   <fctr>     <int>                 <int>      <dbl>     <dbl>
1 Compact        16                    15   18.21250  6.686890
2   Large        11                    10   24.30000  6.337507
3 Midsize        22                    20   27.21818 12.264841
4   Small        21                    16   10.16667  1.953288
5  Sporty        14                    12   19.39286  7.974716
6     Van         9                     8   19.10000  1.878164
```

```R
summarise_each() : 다수의 변수에 동일한 summarise 함수 적용

[문제] Cars93 데이터 프레임의 (i) 가격(Price) 변수와 (ii) 고속도로연비(MPG.highway) 의 두개의 변수에 대해 (a) 평균(mean), (b) 중앙값(median), (c) 표준편차(standard deviation) 의 3개의 함수를 동시에 적용하여 계산하시오.

> # summarize_each() : applies the same summary function(s) to multiple variables
> summarise_each(Cars93, funs(mean, median, sd), Price, MPG.highway)
  Price_mean MPG.highway_mean Price_median MPG.highway_median Price_sd 
1   19.50968         29.08602         17.7                 28  9.65943 
  MPG.highway_sd
    5.3
```



## Reshape2 패키지

```
install.packages('reshape2')
library(reshape2)

pivoting
#와이드형, 롱형 변환
```

- melt()

```R
와이드형 -> 롱형
#melt(data,id.vars='subject') factor형 이어야함
smiths.long <- melt(smiths)
> smiths.long
     subject variable value
1 John Smith     time  1.00
2 Mary Smith     time  1.00
3 John Smith      age 33.00
4 Mary Smith      age    NA
5 John Smith   weight 90.00
6 Mary Smith   weight    NA
7 John Smith   height  1.87
8 Mary Smith   height  1.54
```

- dcast()

```R
#포물러x~y : x는 식별자 변수, y는 측정 변수, 변수가 여러개면 +로 연결
dcast(smiths.long,subject~variable)
#month 와 day 묶어서 식별자로 사용
aq.long <- melt(airquality,id.vars=c('Month','Day'))
aq.wide <- dcast(aq.long,Month+Day~variable)
```



- acast()

```

```









# 타이타닉

```R
df <- read.csv('train.csv',na.string='')
View(df)

#기술 통계량 함수
install.packages('psych')
library(psych)

#결측맵 함수가 포함된 패키지
install.packages('Amelia')
library(Amelia)
missmap(df,col=c('red','grey'))
#na가 너무 많으면 자료를 삭제하기보다 대체하거나 열을 제거하는 방향 고려

#필요한 열만 추출
library(dplyr)
df <- select(df,Survived,Pclass,Age,Sex,SibSp,Parch)
missmap(df,col=c('red','grey'))

#na제거(포함된 행 전체 삭제)
na.omit(df)

#범주지정
df$Survived <- factor(df$Survived)
df$Survived
#순서형 범주 지정
df$Pclass <- factor(df$Pclass,levels=c(3,2,1),ordered=T)
df$Pclass

str(df)

#시각화
install.packages('ggplot2')
library(ggplot2)

#ggplot2 확장
install.packages('GGally')
library(GGally)

#상관계수 확인 #숫자형 데이터만 적용가능(범주형도 제외)
ggcorr(df, nbreaks=6,        #수치 구간을 6개로 나눔
       label=T, 
       label_size=3, color='grey50') 
#운임이 높을수록 생존율 높음, Pclass가 작을수록(높은등급) 생존율 높음
```

## 결측값

```
개수 확인

연속성 변수면
summary()
```



```R
is.na()
x <- c(1, 2, 3, 4, NA, 6, 7, 8, 9, NA)
> is.na(x)
 [1] FALSE FALSE FALSE FALSE  TRUE FALSE FALSE FALSE FALSE  TRUE

갯수가 너무 많으면 어렵다.
#개수만 확인
sum(is.na(df)) #df전체
sum(is.na(df$Luggage.room)) #특정 열
[1] 11

#각 열
colSums(is.na(df))

데이터가 연속성 숫자면
summary()

비연속성 변수면
table()
```



