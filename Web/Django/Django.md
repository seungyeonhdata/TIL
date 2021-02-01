# Django



## 환경설정

- 명령프롬프트에서 python치면 바로 연결되게 고급설정
- C드라이브에 가상환경 폴더 venvs 만들기

#### 장고가 설치된 가상환경

- 파이썬 가상환경 만들기(venv모듈 사용해서 mysite이름의 가상환경 생성)

  `python -m venv mysite`  ( => mysite 폴더도 만들어짐)

- mysite->Scripts->들어가서 `activate`하여 가상환경 들어가기

  +activate 명령어는 Scripts 안에 있음

  +Scripts 안에 장고도 있고 파이썬도 있음

<img src="Django.assets/image-20210129154248694.png" alt="image-20210129154248694" style="zoom:67%;" />

- 장고 깔기 `pip install django==3.1.3`

- 업그레이드 하라고 뜨면 `python -m pip install --upgrade pip`

  *명령어 잘 보고 적당히 변형해서 적용하기*

<img src="Django.assets/image-20210129155008165.png" alt="image-20210129155008165" style="zoom: 67%;" />

- 끌 때는 `exit`

#### 루트 디렉토리

- c\에서 새로운 폴더 **project** 만들기

- C:\project>`C:\venvs\mysite\Scripts\activate`입력해 가상환경 연결

  ```
  가상환경 : 프로젝트를 독립적으로 수행하기 위해 사용
  (서로 다른 버전에서 개발 가능)
  ```

- 또 mysites폴더 만들고 그 안에 <strong>장고 프로젝트</strong> 시작

  `django-admin startproject config .`
  
  <img src="Django.assets/image-20210129161614059.png" alt="image-20210129161614059" style="zoom:67%;" />

- 가상환경 나가려면 `deactivate`
- 나가지 말고 `python manage.py runserver`

<img src="Django.assets/image-20210129162414368.png" alt="image-20210129162414368" style="zoom:67%;" />

​	※헷갈려서 mysite->mysites로 바꿈

#### 내가 그린 요약도

<img src="Django.assets/KakaoTalk_20210201_150850553.jpg" alt="KakaoTalk_20210201_150850553" style="zoom:15%;" />



잘 됐는지 브라우저에 http://127.0.0.1:8000 나 http://localhost:8000로 확인

<img src="Django.assets/image-20210129163235934.png" alt="image-20210129163235934" style="zoom:50%;" />



※**부록** : 매번 가상환경 연결 주소 치기 귀찮으니 명령창에 `mysite`만 줘도 (mysite)가상환경 연결되게 설정하기

```
메모장에
"@echo off
cd c:/project/mysites
c:/venvs/mysite/scripts/activate"
다른이름으로 저장->venvs에 저장(시스템파일로 자동 변경됨)
내PC->고급설정->환경변수->Path에 'C:\venvs' 경로 추가

이제 명령창에 mysite만 쳐도 어디에 있든 project\mysites 가상환경으로 연결됨
```



#### 파이참 연결

: 파이참에 파이썬도 가상환경에 있는 파이썬으로 연결해주어야한다

- existing environment에서 경로-> venvs\mysite\Scripts\python.exe

<img src="Django.assets/image-20210201145115587.png" alt="image-20210201145115587" style="zoom:67%;" />

- settings.py에서 

```
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

​	로 변경해주면 웹사이트 한국어로 나온다.





## mysites 프로젝트

: mysites는 내가 만드려는 웹사이트 이름인 셈.



### 게시판 

- mybo라는 게시판 앱 만들기

`django-admin startapp mybo`

- 게시판 주소는 http://127.0.0.1:8000/mybo 가 된다.

```
1) http://127.0.0.1:8000/mybo 페이지 요청
2) 장고가 url 매핑 확인(config/urls.py에서)
3) 등록되어 있으면 해당 페이지 제공, 안됐으면 404 오류
```

#### url 매핑

```python
주소로 가보면 404오류가 남.
config/urls.py에서 매핑

from django.contrib import admin
from django.urls import path
from mybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mybo/', views.index),    
]
```

그리고 실행하면 에러

```python
AttributeError: module 'mybo.views' has no attribute 'index'
```

```python
mybo/views.py에서 설정

from django.http import HttpResponse

def index(request):
    return HttpResponse("제가 만든 홈페이지입니다.")
```







