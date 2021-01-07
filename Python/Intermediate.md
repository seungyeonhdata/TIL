



```
입출력 종류 : 표준, 파일, 네트워크
```

## 파일

### 파일 입출력

open() : 파일 열기

read()/write() : 파일 입력/출력

close() : 파일 닫기

```python

```



### 피클(pickle) 

 : 파이썬 객체를 파일로 저장하고자 할때 사용하는 모듈

```python

피클링 : 객체 -> 파일
언피클링 : 파일 -> 객체
    
#객체를 파일로 저장
import pickle
내용물="단팥"
색상="파랑"
너비="20cm"
가족명단={'잉어':30,'게':10,'문어':40}
#객체 저장할때는 wb 모드로 파일 열기
with open ("myfish.p","wb") as f:
    pickle.dump(내용물, f)
    pickle.dump(색상, f)
    pickle.dump(너비, f)
    pickle.dump(가족명단, f)

with open ("myfish.p","rb") as f:
    내용물=pickle.load(f)
    색상 = pickle.load(f)
    너비 = pickle.load(f)
    가족명단 = pickle.load(f)
#저장된 순서와 읽어들이는 순서가 일치해야함
    print(내용물)
    print(색상)
    print(너비)
    print(가족명단)

```

## Class