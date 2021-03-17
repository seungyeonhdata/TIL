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
> outer(c(1,2,3),c(3,2,1))
     [,1] [,2] [,3]
[1,]    3    2    1
[2,]    6    4    2
[3,]    9    6    3

#outer 함수 3번째 자리에 함수를 작성하여 모든 순서쌍에 대해 카티전 곱이 아닌 다른 작업 수행
#outer(문자열,문자열,paste)
asia.countries <- c('korea','china','japan')
info <- c('gdp','pop','area')
out <- outer(asia.countries, info, FUN=paste,sep='-')
out
     [,1]        [,2]        [,3]        
[1,] "korea-gdp" "korea-pop" "korea-area"
[2,] "china-gdp" "china-pop" "china-area"
[3,] "japan-gdp" "japan-pop" "japan-area"

as.vector(out) #벡터로 변환
[1] "korea-gdp"  "china-gdp"  "japan-gdp"  "korea-pop"  "china-pop"  [6] "japan-pop"  "korea-area" "china-area" "japan-area"

#자기자신끼리도 엮기 가능
res <- outer(asia.countries, asia.countries, FUN=paste, sep="-")
     [,1]          [,2]          [,3]         
[1,] "korea-korea" "korea-china" "korea-japan"
[2,] "china-korea" "china-china" "china-japan"
[3,] "japan-korea" "japan-china" "japan-japan"

# 하삼각행렬
lower.tri(res)
      [,1]  [,2]  [,3]
[1,] FALSE FALSE FALSE
[2,]  TRUE FALSE FALSE
[3,]  TRUE  TRUE FALSE

res[lower.tri(res)] #T만 출력
[1] "china-korea" "japan-korea" "japan-china"

!lower.tri(res) #T/F 바꾸기
      [,1]  [,2] [,3]
[1,]  TRUE  TRUE TRUE
[2,] FALSE  TRUE TRUE
[3,] FALSE FALSE TRUE

res[!lower.tri(res)] #T만 출력
[1] "korea-korea" "korea-china" "china-china" "korea-japan" 
[5] "china-japan" "japan-japan"
```

### 추출

- substr() : 텍스트의 특정 부분 추출

```R
substr(x,시작,끝)
substr('data analytics',1,4) #data

substring() #끝위치 생략
substring('data analytics',6) #analytics

#텍스트 벡터가 인수인 경우 각 벡터의 원소별로 각각 추출
myclass <- c('data analytics','data mining','data visualization')
substr(myclass, 1,4)
[1] "data" "data" "data"

substring(myclass, 6)
[1] "analytics" "mining" "visualization"

#뒤의 다섯글자(length가 아니라 nchar)
substr(myclass, nchar(myclass)-5,nchar(myclass)) 
[1] "lytics" "mining" "zation"
```

- grep() : 패턴으로 특정 부분 추출

```R
grep(패턴, 문자데이터, value=F, fixed=F) 

islands
class(islands) #numerical
landmass <- names(islands) #이름만 따로 저장
grep(pattern='New',x=landmass) #'New'가 들어간 인덱스 출력
[1] 30 31 32 33 34

#'New' 들어간 이름 출력
1) landmass[grep(pattern='New',x=landmass)]
2) grep(pattern='New',x=landmass,value=T) #'New'가 들어간 자료값 출력
[1] "New Britain" "New Guinea" "New Zealand (N)" "New Zealand (S)"
[5] "Newfoundland"

#두 개 이상의 단어로 이루어진 대륙 또는 섬을 출력
1) grep(' ', landmass,value=T)
2) landmass[grep(' ', landmass)]

#fixed = F -> pattern이 정규표현식
```

#### 정규표현식

| 기호               | 의미               |
| ------------------ | ------------------ |
| ?                  | 0개나 1개          |
| *                  | 0개 이상           |
| +                  | 1개 이상           |
| ^ , $              | 시작, 끝           |
| [[:alnum:]] , \\\w | 알파벳 + 숫자      |
| [[:digit:]] , \\\d | 숫자               |
| [[:space:]] , \\\s | 빈칸, 탭, \n       |
| [[:punct:]]        | 문장부호, 특수문자 |
| [[:alpha:]]        | 알파벳             |

```R
grep('chas?e',words,value=T)
grep('chas*e',words,value=T)
grep('ch(a?e*)se$',words,value=T)
grep('^a',words,value=T)
grep('t$',words,value=T)
#.* : 모든 문자가 0개 이상
grep('^c.*t$',words,value=T)
grep('^[ch]?at',words,value=T)

words2 <- c("12 Dec", "OK", "http://", "<TITLE>Time?</TITLE>","12345", "Hi there")
grep('[[:alnum:]]',words2,value=T)
grep('\\w',words2,value=T)
grep('[[:alpha:]]',words2,value=T)
grep('[[:digit:]]',words2,value=T)
grep('\\d',words2,value=T)
grep('[[:punct:]]',words2,value=T)

```

#### 변경

- gsub()

```R
sub(pattern,replacement,x),gsub('') : 문자열 검색해서 다른 문자열로 변경
sub() : 처음 1개만
gsub() : 모든 문자열

#문자열 변경
txt <- 'Data Anal is useful. Data Anal is interesting.'

sub(pattern='Data',replacement = 'Business', txt)
[1] "Business Anal is useful. Data Anal is interesting."

gsub(pattern='Data',replacement = 'Business', txt)
[1] "Business Anal is useful. Business Anal is interesting."

#파일명만 추출
x <- c('input.csv','data.csv','big.csv')
gsub('.csv','',x)
```



## 날짜 데이터

```R
class(Sys.Date()) #Date타입(문자열 아님)

Sys.Date() #시스템 현재날짜
[1] "2021-02-26"

date() #현재 날짜 및 시간
[1] "Fri Feb 26 11:09:13 2021"

Sys.time() #시스템 날짜 및 시간
[1] "2021-02-26 11:09:27 KST"

#문자열->date
as.Date('2021-02-26') #기본 형식
as.Date('02/26/21', format='%m/%d/%y') #기본 형식 아닌 경우 format 지정

#Date형식에 format() 적용
d <- as.Date('2021-02-26')
format(d,format='%m/%d/%Y')
[1] "02/26/2021"

today <- Sys.Date()
format(today, '%Y/%m/%d %A')
[1] "2021/02/26 금요일"

#날짜의 요일 알아내기
weekdays(as.Date('2021-02-27'))
[1] "토요일"
```

- seq() : 연속된 날짜 생성

```R
s <- as.Date('2021-02-26')
e <- as.Date('2021-04-01')
seq(from=s,to=e,by=5) #5일단위로
seq(s,e,5)
[1] "2021-02-26" "2021-03-03" "2021-03-08" "2021-03-13" 
[5] "2021-03-18" "2021-03-23" "2021-03-28"
seq(s,by=2,length.out=5) #5개까지
[1] "2021-02-26" "2021-02-28" "2021-03-02" "2021-03-04" "2021-03-06"
seq(s,by='2 weeks',length.out=5) #단위 조정 가능
seq(s,by='2 months',length.out=5)
seq(s,by='5 years',length.out=5)

※윤달인 2월은 별도처리 필요
> seq(as.Date('2021-01-30'),by='month',length.out=3)
[1] "2021-01-30" "2021-03-02" "2021-03-30" #2월 안나옴
```

```R
qrt <- seq(s,by='3 months',length.out=4)

> months(qrt) #월 정보
[1] "2월"  "5월"  "8월"  "11월"
> quarters(qrt) #분기 정보
[1] "Q1" "Q2" "Q3" "Q4"
```

## stringr 패키지

```R
library(stringr)
mytext <- c('software environment','software  environment','software\tenvironment')
str_split(mytext, ' ') #띄어쓰기로 나누기
sapply(str_split(mytext, ' '),length) #단어 수
sapply(str_split(mytext, ' '),str_length) #각 단어의 글자수

#전체 문자열 다른 문자로 바꾸기 (gsub)
mytext.nowhitespace <- str_replace_all(mytext,'[[:space:]]{1,}',' ')
mytext.nowhitespace
sapply(str_split(mytext.nowhitespace, ' '),length) #단어 수
sapply(str_split(mytext.nowhitespace, ' '),str_length) #각 단어의 글자수

mytext <- "The 45th President of the United States, Donald Trump, 
states that he knows how to play trump with the former president"
#단어단위로 분리
myword <- unlist(str_extract_all(mytext, boundary('word'))) #리스트로 출력
myword
table(tolower(myword))
myword<-str_replace(myword, "Trump", "Trump_unique_")
myword<-str_replace(myword, "States", "States_unique_")
myword

mytext <- c("He is one of statisticians agreeing that R is the No. 1 statistical software.","He is one of statisticians agreeing that R is the No. one statistical software.")
#숫자 제거
mytext2 <- str_replace_all(mytext, '[[:digit:]]{1,}[[:space:]]{1,}','')
#자르고 연결하기
mytext2 <- str_split(mytext2,' ')
str_c(mytext2[[1]],collapse=' ') 
mytext3 <- str_replace_all(mytext, '[[:digit:]]{1,}[[:space:]]{1,}','_number_')
mytext3 <- str_split(mytext3,' ')
str_c(mytext3[[1]],collapse=' ') 

#'. '기준으로 분리
mytext <- "Kim et al. (2014) argued that the state of default-setting is critical for people to protect their own personal privacy on the Internet."
str_split(mytext,' ')
str_split(mytext,'\\. ')

mytext2 <- str_replace_all(mytext,'-',' ') #정규표현식도 가능
mytext2

#불용어(stopwords): , a, an, the 빈번하게 사용되나 의미 없는 단어들
#불용어 사진 설정 및 제거
mytext <- c('She is an actor','She is the actor')
mystopwords <- '(\\ba )|(\\ban )|(\\bthe )'
str_remove_all(mytext,mystopwords)
#기본 stopwords 이미 있음
stopwords('en') #영어 stopwords 모음
stopwords('SMART')
#stopwords에서 뽑아서 사용

#어근 동일화 작업
various_be <- '(\\b(a|A)m)|(\\b(a|A)re)|(\\b(i|I)s)|(\\b(w|W)as)|(\\b(w|W)ere)'
mystemmer.func <- function(myt){
  mytext <- str_replace_all(myt,various_be,'be')
  print(mytext)
}
mytext <- c('I am a boy. You are a boy. The person might be a boy. Is Jane a boy?')
mystemmer.func(mytext)

mytext <- "The United States comprises fifty states. In the United States, each state has its own laws. However, federal law overrides state law in the United States."
myword <- unlist(str_extract_all(mytext,boundary('word')))
table(myword) #각 단어 개수
length(table(myword)) #종류개수
sum(table(myword)) #전체 단어수
mytext.2gram <- str_replace_all(mytext,'\\bUnited States','United_States')
#     the 관사까지 포함하려면 '\\b(t|T)he United States','The_United_States'
mytext.2gram
mytext2 <- unlist(str_extract_all(mytext.2gram,boundary('word')))
table(mytext2)
```



## tm 패키지

```
#말뭉치 : VCorpus함수로
my.text.location <- 'ymbaek_papers'
mypaper <- VCorpus(DirSource(my.text.location)) #폴더 통으로 줄때
mypaper
summary(mypaper)

mypaper[[2]]
mypaper[[2]]$content #내용 확인
mypaper[[2]]$meta #메타정보?
#meta 정보 수정
meta(mypaper[[2]], tag='author') <- 'Y. M. Baek'
meta(mypaper[[2]], tag='author')
meta(mypaper[[2]])
class(mypaper)
#단어+특수문자+단어 패턴을 추출
myfunc <- function(x){
  str_extract_all(x$content,'[[:alnum:]]{1,}[[:punct:]]{1}?[[:alnum:]]{1,}') 
  #x$content = mypaper안의 모든 컨텐트 
  #extract함수 boundary에 '정규표현식'가능
}
mypuncts <- lapply(mypaper,myfunc)
table(unlist(mypuncts))

#대문자로 시작하는 단어들의 빈도수
upperx <- function(x){
  str_extract_all(x$content,'[A-Z]{1}[[:alnum:]]{1,}')
  #str_extract_all(mypaper$content,'[[:upper:]]{1}[[:alnum:]]{1,}')
}
table(unlist(lapply(mypaper,extractx)))

#숫자로만 이루어진 단어들의 빈도수
numx <- function(x){
  str_extract_all(x$content,'\\d{1,}')
}
mydigits <- lapply(mypaper,numx)
table(unlist(mydigits))

smsraw <- read.csv('sms_spam_ansi.txt')
str(smsraw)
smsraw$type <- factor(smsraw$type)
smsraw
class(smsraw)
#smsraw로 코퍼스 생성 => text열 vector형식이므로 vectorsource
smsCorpus <- VCorpus(VectorSource(smsraw$text))
smsCorpus[[1]]$content

inspect(smsCorpus[1:5])
inspect(smsCorpus[[1]])
lapply(smsCorpus[1:3],as.character)

#tm_map(코퍼스에 대해 전처리(변환작업)를 수행하는 함수)
#소문자 변환
smsCorpusClean <- tm_map(smsCorpus,content_transformer(tolower))
smsCorpusClean[[1]]$content
lapply(smsCorpusClean[1:3],as.character)

#tm_map에 활용가능한 함수들 알아보기
tm_map(smsCorpus,removeNumbers) #숫자 모두 제거
tm_map(smsCorpus,content_transformer(removeNumbers)) #숫자 모두 제거
res <- tm_map(smsCorpus,tolower)
res[[5]]

#단독사용 가능한 함수 5개
removeNumbers, 
removePunctuation, 
removeWords, 
stemDocument,
stripWhitespace
#그 외(사용자함수 포함)는 content_transformer()안에


#특수문자 제거
smsCorpusClean <- tm_map(smsCorpusClean,removePunctuation)
smsCorpusClean[[4]]$content

#stopwords 제거
stopwords()
smsCorpusClean <- tm_map(smsCorpusClean,removeWords, stopwords())
smsCorpusClean[[4]]$content

removePunctuation('helloo...RP')
remPunc <- function(x){  #살짝 변환시킨
  gsub('[[:punct:]]+',' ',x)
}
remPunc('hello...RP')

#word stemming 어근추출할때 많이 씀
install.packages('SnowballC')
library(SnowballC)
wordStem(c('run','runs','running'))
wordstem(c('name','named','naming'))
```

연습

```
#텍스트 불러오기
smsraw <- read.csv('sms_spam_ansi.txt')
smsraw$type <- factor(smsraw$type)
class(smsraw)
str(smsraw)

#smsraw로 코퍼스 생성
library(stringr)
library(tm)
smsCorpus <- VCorpus(VectorSource(smsraw$text))

#첫번째 메일내용 프린트하기(inspect=corpus유지, as.character=문자벡터)
inspect(smsCorpus[[4]])
as.character(smsCorpus[[4]])

#1. 수치데이터 추출
digits <- function(x){
  str_extract_all(x,'\\d{1,}') 
}
smsdigits <- unlist(lapply(smsCorpus,digits))
smsdigits

#1-2 수치데이터 제거
smsCorpusNoNum <- tm_map(smsCorpus,removeNumbers)
inspect(smsCorpusNoNum[[4]])

#2 불용어 제거
stopwords()
smsCorpusNoStopwords <- tm_map(smsCorpus,removeWords, stopwords())
inspect(smsCorpusNoStopwords[[4]])

#3. 대소문자 통일
smsCorpusLower <- tm_map(smsCorpus, content_transformer(tolower))
inspect(smsCorpusLower[[4]])

#4. 특수문자 제거
smsCorpusNoPunct <- tm_map(smsCorpus, removePunctuation)
inspect(smsCorpusNoPunct[[4]])

#5.단어 길이 2미만 제거
smsCorpusRemove <- tm_map(smsCorpus,removeWords,'[[:alpha:]]{1}')
inspect(smsCorpusRemove[[12]])


#6. 가장 많이 나온 단어
#소문자로 통일하고 숫자 제거 불용어 제거 후 단어만 출력
smsCorpusClean <- tm_map(smsCorpus,content_transformer(tolower))
smsCorpusClean <- tm_map(smsCorpusClean,removeNumbers)
stopwords('SMART')
smsCorpusClean <- tm_map(smsCorpusClean,removeWords,stopwords('SMART'))
#smsCorpusClean <- tm_map(smsCorpusClean,str_replace_all,'[^[:alpha:]]{1,}',' ')
myfunc <- function(x){
  str_extract_all(x,'[[:alpha:]]{1,}')
}
sort(table(unlist(lapply(smsCorpusClean,myfunc))),decreasing=T)[1:10]

```

