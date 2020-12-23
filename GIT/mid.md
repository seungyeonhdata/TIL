# Git - Intermediate



## Branch



### Branch 생성하기

```
$ git branch <branchname>
```

#### Branch 생성하면서 넘어가기

​	`$ git switch -c <branchname>` 

​	`$ git checkout -b <branchname>`

새로 생성된 branch로 head가 넘어감.



### Branch 옮기기

```
$ git switch <branchname>
```

head가 <branchname>으로 옮겨간다.



### Branch 확인하기

```
$ git branch
```

모든 branch의 종류와 현재 head 위치



### Branch 합치기

```
$ git merge <branchname>
```

<branchname>의 내용을 현재 branch로 가져오기



### Branch 삭제하기

```
$ git branch -d <branchname>
```

