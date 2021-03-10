# KNN



```
----#머신러닝 #KNN--------------
#컴퓨터비전(얼굴 매칭, 물체식별)
#영화, 음악 추천
#질병 분류, 유전자 데이터 패턴 인식
# 장점 :  쉽다, 훈련이 빠르다, 데이터 분포에 대한 가정 안함
# 단점 :  k값 설정 어렵다, 분류 작업이 느리다, 직관적이지 않다

bc <- read.csv('wisc_bc_data.csv')
bc <- bc[-1]
str(bc)
table(bc$diagnosis)
bc$diagnosis <- factor(bc$diagnosis,levels=c('B','M'),
                       labels=c('Benign','Malignant'))
round(prop.table(table(bc$diagnosis))*100,1)

summary(bc[c('radius_mean','area_mean','smoothness_mean')])

#정규화
normalize <- function(x){
  return ((x-min(x))/(max(x)-min(x)))
}
normalize(c(10,20,30,40,50))

lapply(bc[2:31],normalize) #결과가 리스트
sapply(bc[2:31],normalize) #결과가 리스트

bc_n <- as.data.frame(lapply(bc[2:31],normalize))

#연습문제 8:2 비율로 train/test
set.seed(2021)
sample(1:nrow(bc),nrow(bc)*0.8)

wbcd_train <- bc_n[1:469,]
wbcd_test <- bc_n[470:569,]

wbcd_train_labels <- bc[1:469,1]
wbcd_test_labels <- bc[470:569,1]
wbcd_train_labels

#모델 생성
library(class)
wbcd_predict <- knn(train=wbcd_train, test=wbcd_test, 
    cl=wbcd_train_labels,k=21)
wbcd_predict #예측결과
wbcd_test_labels #답
#교차표로 둘 비교
install.packages('gmodels')
library(gmodels)
CrossTable(x=wbcd_test_labels, y=wbcd_predict)

#표준화
wbcd_z <- as.data.frame(scale(bc[-1]))
wbcd_train <- wbcd_z[1:469,]
wbcd_test <- wbcd_z[470:569,]
wbcd_z_pred <- knn(train=wbcd_train, test=wbcd_test,
    cl=wbcd_train_labels,k=21)
CrossTable(x=wbcd_test_labels,y=wbcd_z_pred)$t[1,1]+CrossTable(x=wbcd_test_labels,y=wbcd_z_pred)$t[2,2]

#k값에 변화를 주면서 가장 테스트 정확도 높았을때 k값 (1~25)
#코드와 정확도 함께 카피
acc <- c()
for(i in seq(1,25,2)){
  wbcd_z_pred <- knn(train=wbcd_train, test=wbcd_test,
                     cl=wbcd_train_labels,k=i)
  acc <- c(acc,sum(wbcd_test_labels==wbcd_z_pred)/length(wbcd_test_labels))
}
which(acc==max(acc))


#---연습---
set.seed(1234)
idx <- sample(1:nrow(iris),nrow(iris)*0.7)
iris_train <- iris[idx,]
iris_test <- iris[-idx,]

str(iris_train)
iris_train_n <- as.data.frame(lapply(iris_train[-5],normalize))
iris_test_n <- as.data.frame(lapply(iris_test[-5],normalize))
iris_predict <- knn(train=iris_train_n,test=iris_test_n,cl=iris_train[,5],k=3)
sum(iris_test[,5]==iris_predict)/length(iris_predict)
CrossTable(iris_test[,5],iris_predict)

acc <- c()
for(i in seq(1,25,2)){
  iris_predict <- knn(train=iris_train_n,test=iris_test_n,cl=iris_train[,5],k=i)
  acc <- c(acc,sum(iris_test[,5]==iris_predict)/length(iris_predict))  
}
acc
index <- which(acc==max(acc))
k <- 2*index-1
acc[index]
paste('k=',k,acc[index])
```

