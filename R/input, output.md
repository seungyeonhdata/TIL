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

- 화면에서 데이터 입력받기

```R
install.packages('svDialogs')
library(svDialogs)
dlgInput() : 데이터 입력창 팝업
$res : 실행 결과에서 입력값을 추출해냄
dlgInput('Input income')$res #입력값은 무조건 문자형
income <- as.numeric(user.input) 
```



## 저장

```R
write.csv(x,file='파일명')
write.csv(product,file='myproduct.csv',row.names=F)
#저장할 데이터 이름(product), 저장할 파일의 이름, 행 번호/이름 제외

디렉토리에서 직접 실행하면 엑셀로 열림
```



## 파일 불러오기

- 작업폴더 설정

```
getwd() : 현재 작업 폴더
setwd('C:/rwork') : 작업 폴더 변경

작업폴더 경로명 길면 탐색기에서 복붙, \하나씩 있으므로 \\로 만들어주면됨
```

- 파일 불러오기

```R
파일을 작업하는 R파일과 같은 폴더에 넣어두면 파일명으로 바로 불러짐
다른 폴더면 경로명 붙여서 파일명

read.csv('file명',header=TRUE,sep=',') #csv는 ,로 데이터 구분
read.table('file명',header=False) #table은 구분자 구분 없음. header 없음.

#엑셀 데이터 읽기
install.packages('openxlsx')
library(openxlsx)
read.xlsx('myproduct.xlsx',sheetIndex=1) #엑셀은 여러워크시트 포함가능하므로

엑셀파일을 '다른 이름으로 저장'해 csv파일로 저장한다음 csv를 읽어들여도됨
```

- 구분자가 있는 경우 sep=

```R
#구분자가 :인 경우
read.table('product-colon.txt',header=T,sep=':')
```

- 클립보드 내용 불러오기

```R
엑셀에서 데이터 복사해오기(ctrl+c)
p <- readClipboard()
p
[1] "id\tname\tprice" "A001\tMouse\t30000" "A002\tMonitor\t50000" 
[4] "A003\tKeyboard\t20000"
--->테이블 형태

클립보드 내용 테이블로 저장 #write 아니고 read!
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

```
print()
- 하나의 값을 출력할때
- 데이터프레임과 같은 2차원 자료구조 출력
- 출력 후 자동 줄바꿈
```

```
cat()
- 여러 개의 값을 연결해서 출력
- 벡터는 출력되나 2차원 자료구조는 출력되지 않음
- 출력 후 줄바꿈 하려면 '\n'
```

- 실행결과 파일로 출력하기

```R
처리과정이 길고 시간 걸리는 작업은 나중에 결과를 파일로 확인해야할 수 있음

sink('test.txt',append=T) #test.txt 파일로 출력 시작
cat('a+b=',a+b,'\n')      #화면에 안나옴
sink()                    #파일로 출력 정지
```









