# 시각화

```R
#graphics패키지 :고수준, 저수준
#고수준 : 완전한 하나의 그래프 생성
#plot(), boxplot(),hist(),crve(),...
#저수준 :  독자적으로 그래프 생성 불가능
#완성된 그래프에 요소를 첨가하는 역할
#points(),lines(),abline(),text(),polygon(),...
```

```
#시계열 분석-> 시간의 흐름에 따라 변하는 데이터 분석
```

```
#산점도 :  각 데이터 점으로 찍음 상관관계 보임.
#분출시간이 길수록 대기시간도 김
plot(faithful)

eruptions.long <- faithful %>% filter(eruptions>3)
eruptions.long
#점 색깔과 모양 바꾸기
points(eruptions.long,col='red',pch=19)#심볼
par(mar=c(5.1,4.1,4.1,2.1))
```

## 선형 회귀 모델

회귀선을 찾는 다양한 방법

### optim()

```R
주어진 y데이터를 x데이터로 예측했을 경우, 예측값과 실제값 사이에서
#차이의 제곱들의 합이 가장 작은 직선

#잔차(residual): 예측값과 실제값 사이의 차이
#잔차제곱의합 : residual sum of square (Rss)

#중간고사(x) ->모델 -> 기말고사 점수 예측 (yhat)
#잔차= y - yhat
#잔차 제곱의 합
#중 최소값인 선 찾기

rss(mydata[,3:4],c(5,1))
#y=x+5를 회귀직선으로, mydata[,3:4]에 대한 rss구하기


#잔차 제곱의 합 구하는 함수
rss <- function(data,lineInfo){
  x <- data[,1] #mid
  y <- data[,2] #final
  intercept <- lineInfo[1] #y절편
  slope <- lineInfo[2] #기울기
  yhat <- intercept+slope*x
  result <- sum((y-yhat)^2)
  result
}

rss(mydata[,3:4],c(-15,1.5))

#회귀모델 만들기 1 : optim()
#optim() : y절편과 기울기를 변경하면서 최적의 값 찾아냄
#par=y절편과 기울기, value=rss
result <- optim(par=c(1,1), fn=rss, data=mydata[,3:4])

#for문 돌듯이 반복해서 돌아서 결과 나옴

# $par
# [1] 13.8833436  0.8967623
# 
# $value
# [1] 5712.789

# 따라서, yhat=13.88x+0.896


plot(mydata$midterm, mydata$final,
     main='시험점수',
     xlab='중간',
     ylab='기말',
     col=color)
abline(result$par[1],result$par[2]) #회귀선
abline(result$par)
```



### 수식

```R
# 기울기 = 상관계수 * 표준편차(y)/표준편차(x)
x <- mydata$midterm
y <- mydata$final
a <- cor(x,y)*sd(y)/sd(x)
#0.896

# 절편 = 평균(y) - 기울기*평균(x)
b <- mean(y)-a*mean(x)
#13.88
```



### lm()

```R
#lm(종속변수~독립변수,데이터)
faith.lm <- lm(waiting~eruptions,data=faithful) #분출시간에 따른 대기시간의 변화

attributes(faith.lm) #속성명들 알려줌

coef(faith.lm)[1] -->b
coef(faith.lm)[2] -->a
#y=ax+b
#a: 기울기(coefficient), b: y절편(intercept)

#fitted : 회귀모델에서 예측값 추출
fitted(faith.lm) #y값
faith.lm$fitted.values #라고 해도 됨
#데이터의 ~뒤 값들을 만들어진 선형회귀 모델에 대입한 것

#회귀선 (rmse값이 최소인 값)
lines(x=faithful$eruptions,y=fitted(faith.lm),col='blue')
```



### 신뢰구간 그리기

```R
#선형회귀 -> 신뢰구간 출력
#속력에 따른 거리의 변화

dev.off()
cars
m <- lm(dist~speed,cars)
p <- predict(m, interval='confidence') #신뢰구간
#fit=직선, lwv=하한구간, upr=상한구간
#fit=회귀모델로 적합된 값
#각 행은 cars 데이터의 각 행에 대한 신뢰구간 표시
#1행은 speed 4에 대한 dist값 예측

plot(cars, cex=0.5)
#자료 내용 출력(문자열)
text(cars$speed,cars$dist,pos=2,cex=0.5) #pos는 위치
identify(cars$speed,cars$dist) #표 우측에 finish 눌러야 나옴
abline(m) #회귀선

head(cars)

#신뢰구간 다각형으로 만들기
#벡터 만들어서 그 안에 넣기
x <- c(cars$speed,tail(cars$speed,1),rev(cars$speed),cars$speed[1]) #rev는 역순
y <- c(p[,'lwr'],tail(p[,'upr'],1),rev(p[,'upr']),p[,'lwr'][1])
#다각형 만들기
polygon(x,y,col=rgb(.7,.7,.7,.5)) #마지막값은 투명도

```



## plot

```
#plot(x) : x 타입에 따라 출력되는 그래프가 달라짐
#벡터, 데이터프레임, 팩터, 시계열, 테이블, 선형회귀 모델...

str(cars)
plot(cars) 
#벡터는 산점도 그래프

str(ToothGrowth)

plot(ToothGrowth$supp,ToothGrowth$len)
#x값이 팩터. 팩터는 박스 그래프

plot(iris[,1:4])
#변수가 2개 넘으면 행렬식 구성

nhtemp
str(nhtemp)
plot(nhtemp)
#시계열은 연결선

UCBAdmissions
str(UCBAdmissions)
plot(UCBAdmissions)
#테이블 데이터는 모자이크 도표로 출력
#모자이크 조각의 크기로 교차표의 상대적 빈도 확인
```

plot 창 닫기 

dev.off() : 초기화

### 스타일

```R
plot(faithful,
     main='main title',
     sub='sub title',
     xlab='eruption time(m)',
     ylab='waiting time till next eruption')
#x,y축 숫자 방향
plot(faithful,
     las=3) #0기본값, 1:y축 숫자 돌아감, 2:x축 숫자 돌아감 3:둘다 돌아감
#박스 모양(그래프 외곽선 모양)
plot(faithful, bty='o')
plot(faithful, bty='n')
plot(faithful, bty='l')
plot(faithful, bty=']')
plot(faithful, pch=24, col='green2',bg='blue')

plot(LakeHuron)
str(LakeHuron)

plot(LakeHuron, lty='solid')
plot(LakeHuron, lty='dashed')
plot(LakeHuron, lty='dotted')
plot(LakeHuron, lty='twodash')

pressure
plot(pressure, type='p') #점으로 표시 (기본값)
plot(pressure, type='l') #선으로
plot(pressure, type='b') #both
plot(pressure, type='o') #겹쳐서
plot(pressure, type='h') #히스토그램
plot(pressure, type='s') #계단식
plot(pressure, type='n') #nothing
#사용자 정의 형식 그래프
x <- 1:10
y1 <- exp(1:10)
y2 <- exp(10:1)
plot(x,y1,type='n',ylab='y')
lines(x,y1,type='o',col='red')
lines(x,y2,type='o',col='blue')

plot(faithful,type='n') #틀 만들고
grid() #격자선 추가
points(faithful, pch=18, col='blue') #포인트찍기
dev.off()
plot(faithful, pch=18, col='blue') #처음부터 찍기

colors() #색 이름들
palette('default') #기본색상 파레트
palette()
pie(rep(1,12), col=1:12) #기본색상 파레트
palette(rainbow(6)) #변경 파레트
palette()
pie(rep(1,12),col=1:12)
pie(rep(1,12),col=gray(level=seq(0,1,length=12))) #그라데이션
pie(rep(1,12),col=rainbow(12,alpha=seq(0,1,length=12))) #그라데이션
#alpha: 투명도
pie(rep(1,12),col=heat.colors(12))
pie(rep(1,12),col=terrain.colors(12))
pie(rep(1,12),col=cm.colors(12))

install.packages('mlbench')
library(mlbench)
data("Ozone")
head(Ozone)
plot(Ozone$V8,Ozone$V9,
     xlab='Sandburg',
     ylab='El Monte', 
     main='Ozone',  #제목
     pch=19,        #점 모양
     cex=0.5,       #점 크기
     col='red',
     xlim=c(0,150), #x축범위
     ylim=c(0,150)) #y축범위
     
#iris 종별 sepal.length평균
with(iris,tapply(Sepal.Length,Species,mean))

#cars 속도별 거리 평균
dist_mean <- with(cars,tapply(dist,speed,mean))
plot(dist_mean, type='o',
     xlab='speed',
     ylab='dist',
     cex=0.7)
    
```

#### legend

```
legend(x, y = NULL, legend, fill = NULL, col = par("col"),
       border = "black", lty, lwd, pch,
       angle = 45, density = NULL, bty = "o", bg = par("bg"),
       box.lwd = par("lwd"), box.lty = par("lty"), box.col = 	        par("fg"),
       pt.bg = NA, cex = 1, pt.cex = cex, pt.lwd = lwd,
       xjust = 0, yjust = 1, x.intersp = 1, y.intersp = 1,
       adj = c(0, 0.5), text.width = NULL, text.col = par("col"),
       text.font = NULL, merge = do.lines && has.pch, trace =            FALSE,
       plot = TRUE, ncol = 1, horiz = FALSE, title = NULL,
       inset = 0, xpd, title.col = text.col, title.adj = 0.5,
       seg.len = 2)
       
x : 범례의 x 위치
y : 범례의 y 위치
fill : 범례기호 채우기 색
col : 범례기호 점,선 색
border : 범례 상자 테두리색
bg : 범례 상자 배경색
pch : 범례 기호 모양, 설정 안할경우 디폴트는 사각형.
cex : 범례 크기
box.lty : 범례 외곽선의 모양(0으로 할 경우 외곽선 없음)

범례위치 x값
top, topleft, topright, bottom, bottomleft, bottomright, center, left, right
```

```
자주 사용할 만한 범례값
data=rbind(A=c(1,2,3),B=c(2,4,5))

mybar=barplot(data,beside=T,ylim=c(0,10),names=c("a","b","c"),col=c("red","blue"),border="white")
text(x=mybar,y=data,labels=data,pos=3,col="black")
grid(nx=NA,ny=NULL)

legend("topright",legend=c("A","B"),fill=c("red","blue"),border="white",box.lty=0,cex=1.5)
```



#### 선그리기

````R
#선 긋기
abline(v=3,col='purple')
abline(h=mean(faithful$waiting),col='green')
abline(a=coef(faith.lm)[1]+10,b=coef(faith.lm)[2],col='green')
abline(faith.lm,col='red')

#평균으로 4분면으로 나누기
mydata <- read.csv('examscore.csv')

plot(mydata$midterm, mydata$final,
     main='시험점수',
     xlab='중간',
     ylab='기말')
title(sub=paste('상관계수 : ',round(mycorr,4)), adj=1, col.sub='red') #adj=위치. 1=오른쪽아래
abline(v=xBar,h=yBar)

````

- par()

```
#plot창 분할(그래프 여러개 넣기)
opar <- par(mfrow=c(1,2)) #2칸으로 나누기
par(mfcol=c(2,1)) #세로방향 두칸으로 나누기
plot(Ozone$V8,Ozone$V9)
plot(Ozone$V8,Ozone$V9)

par(opar) #설정 불러오기
dev.off() #설정 초기화
```

#### 저장

```
png('myplot.png',width=800,height=400)

windows()
savePlot('myplot.pdf',type='pdf')
```

### 그래프

```
#그래프 관련 함수
#curve(함수나 표현식, 시작점, 끝점)
curve(sin,)
curve(sin,0,2*pi)

#iris로 점 찍기
plot(iris$Sepal.Width,iris$Sepal.Length,cex=0.5,pch=20,
     xlab='width',ylab='length')
points(iris$Petal.Width,iris$Petal.Length,cex=0.5,pch='+'
       ,col='#ff0000')
#범례
legend('topright',legend=c('sepal','petal'),pch=c(20,43),
       cex=0.8,col=c('black','red'),bg='grey')

#박스
boxplot(iris$Sepal.Width)
box <- boxplot(iris$Sepal.Width)
#박스의 정보
box #out:극단치
boxplot(iris$Sepal.Width,horizontal=T)
hist(iris$Sepal.Length,breaks='sturges') #히스토그램
#sturges=log2(n)+1
hist(iris$Sepal.Length,breaks=8,freq=F) #default는 개수
#freq=F 확률밀도로 합이 1
h <- hist(iris$Sepal.Length,breaks=8)
h
#밀도 그래프
plot(density(iris$Sepal.Width))

#히스토그램과 비교
hist(iris$Sepal.Width,freq=F)
lines(density(iris$Sepal.Width))

#바 그래프
barplot(tapply(iris$Sepal.Width,iris$Species,mean))

#데이터 비율 :pie그래프 (구간 나눠서)
pie(table(cut(iris$Sepal.Width,breaks=10)))
```

### ggplot2

```R
library(ggplot2)
#3층 레이어로 그래프 그릴 수 있음
#데이터프레임만 가능
#1층: 배경 + 2층: 그래프 + 3층: 범위,설정
#aes:배경(변수설정)
ggplot(data=mtcars, aes(x=wt,y=mpg))+
  geom_point()+
  labs(title='practice',
       x='weight',y='mpg')

mtcars$gear <- factor(mtcars$gear, levels=c(3,4,5),
                      labels=c('3gear','4gear','5gear'))
mtcars$cyl <- factor(mtcars$cyl, levels=c(4,6,8),
                      labels=c('4cyl','6cyl','8cyl'))

ggplot(data=mtcars, aes(x=mpg))+
  geom_histogram()+
  facet_grid(cyl~.)+
  labs(title='cyl vs mpg')

ggplot(data=mtcars, aes(x=cyl,y=mpg))+
  geom_boxplot()+
  labs(title='cyl x mpg')

ggplot(data=mtcars, aes(x=mpg, fill=cyl))+
  geom_density()+
  labs(title='mpg x cyl density')

ggplot(data, aes(x=, y=, fill=색채우기(factor면 각 factor마다 색 다르게)))+geom_col(position='dodge') #옆으로 내려서 따로 표시할때
```



