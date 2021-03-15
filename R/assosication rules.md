## 연관 분석

: 거래 데이터에서 동시구매와 관련된 규칙

**협업필터링 알고리즘** : 추천대상 고객과 가장 높은 상관계수를 가진 고객(가장 구매 패턴이 비슷한 고객)을 찾아서 상품을 추천----시간분석 제외(어떤 상품을 먼저 넣었는지는 고려하지 않음)



```
-X,Y는 항목집합
-연관규칙: X->Y
-N: 전체 거래 건수 ex) n(X) : X의 거래건수
-동일한 물건 여러건 구매한 것은 고려하지 않는다
```

- 지지도(Support)

```
S(X->Y) : X구매자가 Y도 구매하는 규칙에 대한 지지도
  X와 Y를 모두 포함하는 거래수/전체거래수 : n(X+Y)/N
  
```

- 신뢰도(Confidence)

```
C(X->Y) : X를 포함하는 거래 중, Y도 포함하는 거래 비율
  X와 Y를 모두 포함하는 거래수/X의 거래수 : n(X+Y)/n(X)
```

- 향상도(Lift)

```
Lift(X,Y) : X 구매자가 Y도 구매할 확률(우연인지 아닌지)
 (X->Y)의 신뢰도/Y의 지지도 : c(X->Y)/S(Y)
  - X구매자 중 X와 Y를 모두 구매한 비율/전체에서 Y를 구매한 비율
  
  향상도 = 1, 두 항목이 독립적. 서로 연관이 없음
  향상도 > 1, 필연적, 서로 연관이 큼(클수록)
  향상도 < 1, 필연적, 서로 연관이 적음(작을수록)
```

- IS(Interest Support) 척도

```
sqrt(lift(X,Y)*S(X,Y))
```

- 교차지지도

```
최대 지지도에 대한 최소 지지도의 비율
X={i1,i2,...,im}
min(S(i1,i2,i3...,im))/max(S(i1,i2,...,im))

- 최대 최소 차이가 클수록 교차지지도가 작아진다
- 작을수록 항목집합 X에서 생성되는 연관규칙이 의미가 없다.
```



## apriori

```
거래데이터는 희소행렬(몇개 없는거) sparse matrix(기억장소 낭비임)
물품종류 169개
1번거래아이템: a,b,c
2번: a,b,t
3번: b,c
4번: g
이런 식으로 저장되어있음

df <- read.table('groceries.csv',header=F)
str(df)
head(df)
#이렇게 하면 희소행렬때문에 빈열이 많이 생김 
#arules 패키지로 transactions로 읽어오기
```

```R
install.packages('arules')
library(arules)
groceries <- read.transactions('groceries.csv',sep=',')
summary(groceries)
class(groceries)

#데이터 보는 함수 inspect {}형식
inspect(groceries[1:10]) #트렌잭션 단위로 구매아이템 확인

#알파벳 순서로 각 단어 비율 = 지지도
itemFrequency(groceries[,])

#====시각화====
dev.off()
itemFrequencyPlot(groceries,support=0.1) #최소지지도 0.1
#열명중에 한명은 이 물건들은 산것
#상위 물품 개수 적절하게 적정한 지지도 설정해야함

#지지도 높은 25가지 품목 출력
itemFrequencyPlot(groceries,topN=25)

#데이터 분포확인 #행렬다이어그램
image(groceries[1:10])
#x축 아이템 번호는 알파벳순으로 나열한것

#랜덤하게 100개 상품 추출하여 행렬다이어그램 형식
image(sample(groceries,100))

#apriori 알고리즘으로 규칙지정(빈발 항목집합 추리기)
groceryrules <- apriori(groceries,
                        list(support=0.006, confidence=0.25, minlen=2))

apriori(groceries) #옵션 없이 넣으면 default 옵션으로 들어가서
#맞는 규칙 하나도 없음 (default=support=0.1, confidence=0.8, maxlen=10)

groceryrules #규칙 463개

summary(groceryrules)

inspect(groceryrules[1:3]) #그냥 3개 

#연관 높은 상품들
inspect(sort(groceryrules,by='lift')[1:10]) #향상도 기준으로 정렬해서 상위 10개

#특정 상품과 관련된 규칙들만 추출
#키워드 줘서 추출
#'berries'가 lhs, rhs(items라고 함)에 포함된 경우 추출
berryrules <- subset(groceryrules,items %in% 'berries') #4개
inspect(berryrules)
berryrules <- subset(groceryrules,lhs %in% 'berries') #왼쪽에
berryrules <- subset(groceryrules,rhs %in% 'berries') #오른쪽에 

#'berries'나 'yogurt' 들어간 경우
yogurtoo <- subset(groceryrules,items %in% c('berries','yogurt')) #132개
inspect(yogurtoo)

#부분 매칭 (포함되는 경우도 모두)
fruitrules <- subset(groceryrules, items %pin% 'fruit') #111개
inspect(fruitrules)

#완전매칭 (모두 포함하는 경우만)
allrules <- subset(groceryrules,items %ain% c('berries','yogurt')) #1개
inspect(allrules)

#파일로 만들기(quote=따옴표, row.names=행번호)
write(groceryrules,'groceryrules.csv',sep=',',quote=F,row.names=F)

#데이터프레임으로 바꾸기(분석업무할때)
groceryrulesDf <- as(groceryrules,'data.frame')

#추가조건(지지도나 신뢰도같은거)
fruitrules <- subset(groceryrules, items %pin% 'fruit' & confidence>0.4) #47개
inspect(fruitrules)
```

