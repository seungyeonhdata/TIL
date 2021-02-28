# 데이터 입출력

## 입력

- 비어있는 데이터프레임 편집하기

```
데이터 프레임 만들기
product <- data.frame()

편집창 켜서 수정
edit(product)
fix(product)
```



## 저장

```R
write.csv(x,file='파일명')
write.csv(product,file='myproduct.csv',row.names=F)

디렉토리에서 직접 실행하면 엑셀로 열림
```

- 엑셀에서 데이터 복사해오기(ctrl+c)

```R
클립보드 내용 불러오기
p <- readClipboard()
p
[1] "id\tname\tprice" "A001\tMouse\t30000" "A002\tMonitor\t50000" 
[4] "A003\tKeyboard\t20000"
--->테이블 형태

클립보드 내용 테이블로 저장
read.table(file='clipboard', sep='\t')
    V1       V2    V3
1   id     name price
2 A001    Mouse 30000
3 A002  Monitor 50000
4 A003 Keyboard 20000
read.table(file='clipboard', sep='\t',header=T) #1행을 열이름으로
    id     name price
1 A001    Mouse 30000
2 A002  Monitor 50000
3 A003 Keyboard 20000
```



## 파일 불러오기

```R
파일을 작업하는 R파일과 같은 폴더에 넣어두면 파일명으로 바로 불러짐

read.csv('file명',header=TRUE,sep=',') #csv는 ,로 데이터 구분
read.table('file명',header=False) #table은 구분자 구분 없음. header 없음.

#엑셀 데이터 읽기
install.packages('openxlsx')
library(openxlsx)
read.xlsx('myproduct.xlsx')
```

- 구분자

```R
#구분자가 :인 경우
read.table('product-colon.txt',header=T,sep=':')
```

- NA 표기

```R
> read.table('product-missing.txt',header=T, na.strings=c('.','idk'))
#--> .이나 idk는 NA로 표기
    id     name price
1 A001    Mouse 30000
2 A002 Keyboard    NA
3 A003     <NA> 50000 #문자는 <NA>
```

- txt의 주석문(#)은 무시(속성 comment.char = "#")

- url로 데이터 불러오기

```R
url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
read.csv(url,header=F)
```

- 파일 다운로드

```R
download.file(url=url, destfile='myIris.csv')
#현재 디렉토리에 저장됨

#zip파일
baseball <- 'http://seanlahman.com/files/database/baseballdatabank-master_2016-03-02.zip'
download.file(baseball,'baseball.zip')
unzip('baseball.zip','baseballdatabank-master/core/Salaries.csv')
#salary파일만 압축 풀었음
```



## 출력

ㅇㅅㅇ