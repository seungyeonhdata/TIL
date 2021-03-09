# 시각화

#graphics패키지 :고수준, 저수준
#고수준 : 완전한 하나의 그래프 생성
#plot(), boxplot(),hist(),crve(),...
#저수준 :  독자적으로 그래프 생성 불가능
#완성된 그래프에 요소를 첨가하는 역할
#points(),lines(),abline(),text(),polygon(),...


#시계열 분석-> 시간의 흐름에 따라 변하는 데이터 분석


#산점도 :  각 데이터 점으로 찍음 상관관계 보임.
#분출시간이 길수록 대기시간도 김
plot(faithful)

eruptions.long <- faithful %>% filter(eruptions>3)
eruptions.long
#점 색깔과 모양 바꾸기
points(eruptions.long,col='red',pch=19)#심볼
par(mar=c(5.1,4.1,4.1,2.1))

#dev.off() : 그래프 창 닫기
dev.off()

#선형 회귀 모델
#lm(종속변수~독립변수,데이터)
faith.lm <- lm(waiting~eruptions,data=faithful) #분출시간에 따른 대기시간의 변화
coef(faith.lm)[1]
coef(faith.lm)[2]
#y=ax+b
#a: 기울기(coefficient), b: y절편(intercept)

#fitted : 회귀모델에서 예측값 추출
fitted(faith.lm) #y값
#데이터의 ~뒤 값들을 만들어진 선형회귀 모델에 대입한 것

#회귀선 (rmse값이 최소인 값)
lines(x=faithful$eruptions,y=fitted(faith.lm),col='blue')

#선 긋기
abline(v=3,col='purple')
abline(h=mean(faithful$waiting),col='green')
abline(a=coef(faith.lm)[1]+10,b=coef(faith.lm)[2],col='green')
abline(faith.lm,col='red')

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

png('myplot.png',width=800,height=400)

windows()
savePlot('myplot.pdf',type='pdf')