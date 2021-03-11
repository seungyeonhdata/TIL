# Kmeans

```R
#kmeans 머신러닝 알고리즘(클러스터링)
#미국 10대 학생 시장 세분화

teens <- read.csv('snsdata.csv')
str(teens)
# 앞의 4변수는 각 학생의 정보(졸업년도, 성별, 나이, 친구 수)
# 나머지는 가장 많이 언급된 36개 단어
# NA값은 성별과 나이에 포함
table(teens$gender)
table(teens$gender, useNA='ifany') #NA를 하나의 변수로
#성별 NA값 2724개
#1은 여성, 0은 남성이거나 NA
teens$female <- ifelse(teens$gender=='F'&!is.na(teens$gender),1,0)
#성별이 없으면 1
teens$nogender <- ifelse(is.na(teens$gender),1,0) 

#나이 NA값 5086개, 이상치 없애기
#13세 이상 20세 미만: 정상, 그 외는 NA
teens$age <- ifelse(teens$age>=13&teens$age<20,teens$age,NA)
summary(teens$age)
#나이 NA값 5523개

#졸업 연도 별 나이의 평균 출력
with(teens,tapply(age,gradyear,mean,na.rm=T)) #결과 array
library(dplyr)
teens %>% group_by(gradyear) %>% 
  summarise(mean(age,na.rm=T)) #결과 tibble
aggregate(data=teens,age~gradyear,mean,na.rm=T) #결과 dataframe
#평균구하는 함수 ave
ave_age <- ave(teens$age,teens$gradyear,FUN=function(x) mean(x,na.rm=T))

#나이 결측값 대체
teens$age <- ifelse(is.na(teens$age),ave_age,teens$age)
summary(teens$age)

#kmeans
#kmeans(x=숫자형 매트릭스,centers=k)
interests <- teens[5:40] #36차원 데이터임
interests_z <- as.data.frame(lapply(interests, scale))

#클러스터 랜덤하게 잡으므로 set.seed로 고정
set.seed(2345)
teen_clusters <- kmeans(interests_z,5) #군집화

teen_clusters

Cluster means:
  각 클러스터의 centeroid의 좌표
  표준화된 데이터라 양수면 평균보다 많이 언급, 
  음수면 평균보다 낮게 언급한 것.
cluster vector:
  각 데이터(행)가 어느 그룹에 속하는지
  
#cluster 정보
teen_clusters$size #k값 : 그룹개수
[1]  1016  5999 21564   553   868
teen_clusters$centers #Cluster means:          
teen_clusters$cluster #cluster vector:
teen_clusters$withinss #클러스터 내 데이터간 거리의 제곱합. 작을수록 동질성 높음
[1] 180641.38 392747.49 253143.30  65818.27  54831.62
teen_clusters$tot.withinss #sum(withinss)
[1] 947182.1
teen_clusters$betweenss #클러스터 간 중심의 거리 제곱합. 클수록 이질성 높음
[1] 132781.9
```

```
[teens_clusters 출력 결과]
K-means clustering with 5 clusters of sizes 1016, 5999, 21564, 553, 868

Cluster means:
  basketball    football      soccer    softball  volleyball
1  0.3564034  0.37070543  0.12090235  0.17593266  0.11316304
2  0.5032205  0.50490026  0.30979413  0.38106159  0.37310168
3 -0.1665316 -0.16801743 -0.09690758 -0.11680224 -0.11743188
4  0.1262118  0.01660786  0.03116961 -0.01746354  0.03065167
5  0.1617135  0.24010406  0.10505348  0.07332336  0.18679719
     swimming cheerleading    baseball      tennis      sports
1  0.27500482   0.19645616  0.27805142  0.11474799  0.81023725
2  0.30042145   0.32873523  0.32733517  0.15415967  0.31540567
3 -0.10864376  -0.11607907 -0.10619816 -0.05465286 -0.13035952
4  0.08981181  -0.01043587  0.03109676  0.03744470  0.01381317
5  0.24365773   0.38850003  0.03073339  0.13414691  0.10151421
         cute           sex        sexy         hot      kissed
1  0.47219033  2.0738429670  0.50970895  0.30889657  3.04770542
2  0.55841493  0.0008619418  0.25939150  0.38704764 -0.03112297
3 -0.19251775 -0.0987938530 -0.09884165 -0.13869170 -0.13651601
4 -0.01024285  0.0035438739 -0.07217944  0.01505922 -0.04640141
5  0.37723557  0.0187046541  0.11219192  0.39940369  0.06881257
```

