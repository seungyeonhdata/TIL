# Github - Basic

## Git이란?

파일의 변경사항을 추적하고 여러 사용자들 간의 작업을 조율하기 위한 분산 버전 관리 시스템이다. 무료이고 오픈소스들을 제공해 빠른 속도와 효율성을 가지고 크고 작은 프로젝트들을 다룰 수 있다. 

## Git 설치

1. git-scm.com 에서 다운로드
2. 계속 next로 설치

## Git 사용법

### 최초 설정

컴퓨터에 처음 git을 설치하면 사용자의 이메일과 닉네임 적어준다. 앞으로 일어나는 커밋에 서명을 하기 위해서 필요하다.

```
$ git config --gloabal user.email 'email'

$ git config --global user.name 'name'
```

잘 설정되었나 확인하려면

```
git config user.email

git config user.name
```

이메일과 이름을 출력할 수 있다. 

### 상태점검

`git status`

<img src="basic.assets/image-20201222165058452.png" alt="image-20201222165058452" style="zoom:80%;" />

수시로 해주기

### 초기화

초기화는 `git init`을 통해 진행한다.

```
$ git init
```

<img src="basic.assets/image-20201222165058452.png" alt="image-20201222165058452" style="zoom:80%;" />



### stage 올리기

untracked 상태인 디렉토리의 파일들은 stage에 올려야 commit할 수 있다.

tracking을 하려면 `$ git add`을 이용하면 된다.

<img src="basic.assets/image-20201222173749932.png" alt="image-20201222173749932" style="zoom:80%;" />

`$ git status`를 통해 상태를 확인해보면 처음에는 untracked였던 first.py(빨간색)가 초록색으로 변한다.



### commit 하기



### Summary

| 명령어                              | 설명                                        |
| ----------------------------------- | ------------------------------------------- |
| `$ mkdir`                           | 폴더 만들기                                 |
| `$ touch`                           | 파일 만들기                                 |
| `$ rm (/-r/-rf)`                    | 삭제 (파일/폴더/강제적으로 다)              |
| `$ cd <dir>` / `$ cd ..`            | 디렉토리 들어가기 / 위로 가기               |
| `$ ls  (-a)`                        | 리스트 (숨겨진 파일까지)                    |
| `$ git init`                        | 빈 디렉토리를 git 저장소(repo)로 초기화하기 |
| `$ git add <filename> `             | 스테이지에 올리기 (전부)                    |
| `$ git commit -m "commit msg"`      | 스테이지에서 커밋하기                       |
| `$ git log`                         | 지금까지의 기록 보기                        |
| `$ git restore --staged <filename>` | 스테이지에서 내리기                         |
| `$ mv <before> <after>`             | 이름 변경                                   |
|                                     |                                             |

