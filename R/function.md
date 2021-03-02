함수

조건문

```
#transLength.R에 저장한 스크립트
#스크립트 : 야드를 미터로 변환하는 명령어의 집합
#x <- c(30,50,90)
#tlength <- round(x*0.9144,1)
#result <- paste(tlength,'m',sep='')

#transLength.R 실행
source('transLength.R')

#transLength 함수 만들기
transLength <- function(x){
  tlength <- round(x*0.9144,1)
  result <- paste(tlength,'m',sep='')
  result
}
transLength(c(30,50,90))
ls()

trans2 <- transLength
trans2(90)
trans2

f1 <- function(x,y){x+y}
#실행문장이 1개면 중괄호 생략가능
f2 <- function(x,y) x+y

#예외처리
f3 <- function(x){
  if(!is.numeric(x)){
    return('not a number')
  }
  tlength <- round(x*0.9144,1)
  result <- paste(tlength,'m',sep='')
}
f3('abc')

y <- c(100,150,200)
transLength <- function(y,m){
  if(m=='ft'){
  tlength <- round(3*y,1)
  result <- paste(tlength,'ft',sep='')
  return(result)
  }
  tlength <- round(36*y,1)
  result <- paste(tlength,'in',sep='')
  result
}
transLength(y,'ft')

transLength <- function(x,mult=0.9144,unit='m',...){ #default값 설정
    tlength <- round(x*mult,...)
    result <- paste(tlength,unit,sep='')
    return(result)
}
transLength(y,mult=3, unit='ft')
transLength(y,36,'in')
transLength(y,digits=2)

transLength <- function(x,mult=0.9144,unit='m',digits=1){
  tlength <- round(x*mult,digits=digits)
  paste(tlength,unit,sep='')
}
transLength(y)

#함수를 인수취급할때는 FUN 사용
transLength <- function(x,mult=0.9144,unit='m',FUN=round,...){ #default값 설정
  tlength <- FUN(x*mult,...)
  paste(tlength,unit,sep='')
}
transLength(y,digits=2)

a <- pi
b <- 3
if(a>b)a else b
#if,else 는 벡터연산안됨
#ifelse는 벡터연산가능
ifelse(x>y,x,y)

#switch함수: 첫번째 인수로 주어진 값에 따라 두번째 이후의 인수에 코드 실행
center <- function(x,type){
  switch(type,
         mean=mean(x),
         median=median(x),
         trimmed=mean(x,trim=0.1)
         )
}
x <- c(2,3,5,7,11,13,17)
center(x,'mean')
center(x,'median')
center(x,'trimmed')
#trimmed: mean이 outlier(이상치)에 민감하게 반응하는것을 보정해 평균낸것

i <- 5
repeat{if(i>25)break
  else{
    print(i)
    i <- i+5
  }
}

for(i in seq(5,25,5)) print(i)
#실행결과는 루프 안에서는 출력되지 않는다.print해야함
#for문이 종료된 이후에도 변수는 사라지지 않는다.
i <- 1
for(i in seq(5,25,5)) i
print(i) #가장 마지막에 할당된 25가 i에 저장

#mode : 데이터유형 파악
mode(c(3.14,1.5))
mode(factor('high','medium','low'))
mode(as.Date('2021-03-02'))
mode(5>2)
mode(list(1.2,'apple',c(3,4)))
mode(mean)

```

