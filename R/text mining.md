# 텍스트 마이닝

## 텍스트

```R
#text mining
#베이즈 이메일 분류기 (Bayesian filter) 이진 추론. 성능 좋지 않음
#인공지능 언어모델 bert가 나오면서 다 사라짐

x <- 'we have a dream'
x
nchar(x) #공백문자 포함
length(x) #문자 벡터의 벡터 길이(원소 개수가 1개)

y <- c('we','have','a','dream')
length(y)
nchar(y)
nchar(y[4])

#대소문자 변환
tolower(x)
toupper(x)

자연어 <- sql
#회사에서 직급이 대리인 사람의 이름 모두 출력
#SELECT name FROM company WHERE 직급='대리'
```

- 유일한 단어 추출

```
#유일한 단어 추출
unique(said.word[[1]]) #벡터만 가능
unique(tolower(said.word[[1]]))
unique(c('go','fetch','go','now'))
```



### 분리

```R
strsplit(x,split=' ')
class(strsplit(x,split=' ')) #리스트임

unlist(strsplit(x,split=' ')) #벡터로 만들기
res <- strsplit(x,split=' ')[[1]] #벡터로 만들기
res[4]

x1 <- 'We have a dream'
x2 <- 'how are you'
x3 <- c('i am fine','do you wanna build a snowman. it doesnt have to be a snowman. okay bye')
myword <- c(x1,x2,x3)
myword
strsplit(myword," ")

#대소문자 구분됨
said <- 'WHAT IS ESSENTIAL is invisible to the Eye'
said.word <- strsplit(said,' ')
```

### 결합

```R
#paste() : 분리된 벡터 결합. 벡터의 원소들을 분리한 다음 결합하는게 아님

#기본값으로 공백문자 들어감
> paste('everybody','wants','to','fly')
[1] "everybody wants to fly"
> paste('everybody','wants','to','fly',sep='-')
[1] "everybody-wants-to-fly"

#chr가 아니면 문자열로 변환 후 결합
> paste(pi, sqrt(pi))
[1] "3.14159265358979 1.77245385090552"
> paste('aaa',1+2,'b')
[1] "aaa 3 b"

#벡터는 그대로 나옴
> paste(c('everybody','wants','to','fly'))
[1] "everybody" "wants"     "to"        "fly"   
#paste의 collapse 옵션 : 텍스트 결합으로 생성된 텍스트들 연결하는 구분자 정의
> paste(c('Everybody','wants','to','fly'),collapse=' ')
[1] "Everybody wants to fly"

#"batman wants to fly, and captain america wants to fly, and hulk wants to fly"
heroes <- c('batman','captain america','hulk')
paste(heroes,'wants','to','fly',collapse=', and ')

#벡터끼리 연결하면 각 위치의 원소 하나씩 결합됨
heroes <- c('batman','captain america','hulk')
colors <- c('black','blue','green')
paste(colors,heroes)
[1] "black batman" "blue captain america" "green hulk"  
#길이 다르면 짧은쪽이 반복
> paste('type',1:5)
[1] "type 1" "type 2" "type 3" "type 4" "type 5"
```

- outer() : 두 집합에 대해 가능한 모든 순서쌍의 곱 수행 (카티전곱)

```R
#outer 함수 3번째 자리에 함수를 작성하여 모든 순서쌍에 대해 카티전 곱이 아닌 다른 작업 수행
#outer(문자열,문자열,paste)
asia.countries <- c('korea','china','japan')
info <- c('gdp','pop','area')
out <- outer(asia.countries, info, FUN=paste,sep='-')
out
as.vector(out)
res <- outer(asia.countries, asia.countries, FUN=paste, sep="-")

lower.tri(res) #하삼각행렬
res[lower.tri(res)]
!lower.tri(res)
res[!lower.tri(res)]
```

### 추출

- substr() : 텍스트의 특정 부분 추출

```R

```

