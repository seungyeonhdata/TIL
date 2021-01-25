# Javascript

:객체 기반 클라이언트 스크립트 작성 언어. 생성된 객체를 이용하여 동적인 페이지를 기술한다. 확장자는 js

※`/* 주석은 // 여러 줄이면 별과 슬래시로 감싸기 */`





## 작성법

1. html 문서 내에 작성

   ```html
   <head>
   	<script type="text/javascript">
           여기에 작성
       </script>
   </head>
   ```

2. js파일로 작성하여 html 문서에 포함

   ```html
   <head>
   	<script type="text/javascript" src="test.js">
         	test.js파일 불러옴
       </script>
   </head>
   ```

3. 함수 정의: function (파이썬 def)

   ```javascript
   function myfunc(){
   	return 3;
   }
   ret=myfunc(); //함수 호출
   document.write(ret);
   ```

4. 변수 선언

   ```javascript
   var로 선언. 브라우저가 알아서 type 분류.
   
   var a=10;
   var b='k';
   document.write(a); //print임
   
   type확인
   document.write(typeof '스크립트');
   document.write(typeof 1);
   ```

5. 자료 유형

   ```
   Boolean:참/거짓
   String:문자열
   Number:숫자형
   null:빈 값
   NaN:Not a Number, 숫자 아님
   Infinity:무한대
   ```

6. 차이점

   ```javascript
   html태그 사용가능.
   document.write('b는'+'<br>'+'bee'+'<br>');
           
   \n은 띄어쓰기
   document.write('b는\nbee');
   ```

7. True 값은 1

   ```javascript
   그 외는 False
   document.write(true==1); //True
   document.write(true=='1'); //True
   document.write(true==0); //False
   document.write('one'==1); //False
   document.write(true==2); //False
   document.write('one'!==1); //True
   
   document.write(1>2); //False
   ```

8. style 바꾸기

   ```javascript
   '<태그>'+'</태그>'로 감싸준다
   
   for(var i=0;i<100;i++){
       for(var j=0;j<10;j++){
           document.write('<font color="blue">'+String(i)+String(j)+"<br/>"+'</font>');
           }
       }
   
   ```

   

9. on 이벤트 속성명

   : 이벤트가 발생하게 하는 속성명은 on으로 시작하는 함수

   ```html
   <input type="button" value="click me" onclick="alert('why click me?')">
   ```

   <img src="Javascript.assets/image-20210125112754046.png" alt="image-20210125112754046" style="zoom: 67%;" />



### 조건문

* if 조건문

```javascript
if(조건){
수행할 문장;
}
else if(조건){
}
```

```javascript
if(2>1){
alert("2가 1보다 큽니다");
}

if(false){
alert("1");
}
else if{
alert('참');    
}
alert("3"); //조건문과 별개로 동작


아이디 넣기
id=prompt("아이디:")
if(id=='master'){
alert("아이디가 일치합니다");
document.write(id+'<br/>');
}
else{
alert("아이디가 일치하지 않습니다");
}

아이디 맞으면 비번 넣기
id=prompt("아이디:")
if(id=='master'){
alert("아이디가 일치합니다");
document.write(id+'<br/>');
pw=prompt("비밀번호:");
if(pw=='1234'){
alert("인증에 성공하였습니다");
}
else{
alert("인증에 실패하였습니다");
}}
else{
alert("아이디가 존재하지 않습니다");
}
```

### 반복문

* while 문

```javascript
주로 무한반복할 때
while(조건){
반복할 문장;
}
```

```javascript
var i=0;
while(i<10){
document.write("무한 코딩");
i++; //i+=1
}
```

* for 문

```javascript
break 하고 continue 다 들어가 있음

var i=0;
for(i=0;i<10;i++){
document.write("무한 코딩<br/>");
}

5빼고 출력:
var i=0;
for(i=0;i<10;i++){
if(i==5){
continue;}
document.write(i+"무한 코딩<br/>");
}

3의배수 출력:
for(i=1;i<101;i++){
if(i%3==0){
document.write(i+'<br/>');
}}

앞자리를 문자로 바꿔서 00부터 99까지 표현(하나만 문자여도 다 문자로 변환해서 더한다)
for(var i=0;i<10;i++){
    for(var j=0;j<10;j++){
        document.write(String(i)+j+"<br/>");
        }
    }

function numbering(){
for(var i=0;i<5;i++){
    j=0;
    while(j<10){
    document.write(j);
    j++;}
    document.write('<br>');}
    }
numbering();
```

* 연습

```html
구구단
function gugu(){
    for(var i=1;i<10;i++){
        for(var j=1;j<10;j++){
        document.write(i*j+'\n');
        }
    document.write("<br/>");
    }
}
gugu();

function gugu(){
    var i=1;
    while(i<10){
        var j=1;
        while(j<10){
        document.write(i*j+'\n');
        j++;
        }
    i++;
    document.write("<br/>");
    }
}
gugu();

최대최소 구하기
var arr=[52,273,103,32,57,103,31,2];
function Max(){
    var max=arr[0];
    for(var a=1;a<arr.length;a++){
        if(max<arr[a]){
            max=arr[a];
            }
        }
    return max;
}
document.write(Max()+"<br/>");

function Min(){
    return Math.min.apply(null,arr);
    }
document.write(Min());

다이아몬드 그리기
for(var i=1;i<=5;i++){
    for(var j=5;j>i;j--){
        document.write('&nbsp;');
    }
    for(var k=0;k<i*2-1;k++){
        document.write('*');
    }
    document.write('<br>');
}
for(var i=4;i>0;i--){
    for(var j=4;j>=i;j--){
        document.write('&nbsp;');
    }
    for(var k=0;k<i*2-1;k++){
        document.write('*');
    }
    document.write('<br>');
}

                              
2)
for(var i=1;i<11;i++){
    for(var k=1; k<(11-i)/2;k++){  //공백 4,3,2,1
        document.write('&nbsp');
        }
    for(var j=1;j<i+1;j++){    // * 1,3,5,7
        document.write("*");
        }
    document.write("<br/>")
    i++;
}

    for(var i=1;i<9;i++){
   	 for(var k=1;k<=(i+1)/2;k++){   //공백 1,2,3,4
     document.write('&nbsp');
       }
     for (var j=1;j<9-i;j++){  // * 7,5,3,1
        document.write("*");
        }
      document.write("<br/>")
      i++;
 }

```







## 함수

```javascript
function 함수이름(인수들){
코드1;
if(조건)return;
코드2;
코드3;
return 반환값

function myf(a,b){
return a+b;}
alert(myf(10,5));

/*
var myf=function (a1,a2){
document.write(a1+a2){
}
myf(10,20)
안되는데? */
```



* `parseInt()`

:문자로 된 숫자를 숫자로 변환

```javascript
var k='5';
document.write(k+2) //문자+숫자는 문자 결합 52
document.write(parseInt(k)+2); //숫자로 인식해서 7
document.write(parseInt('hello'); //NaN
```

* `alert()`

:창 뜰때 메세지로 내용 출력

```javascript
연산 사용 가능
alert('Hello World');
alert(2*4);
alert("안녕\n하세요"); //줄바꿈
alert("안녕".length); //문자열 길이
alert("1"==1); //내부적으로 연산을 하기 전에 자동 형 변환 True
alert("1"===1); //형 변환 안됨 False
```

* `Math 클래스`

```javascript
Math.pow(3,4) //지수 81
Math.sqrt(4) //루트 2
Math.round() 반올림
Math.ceil() 올림
Math.floor() 내림
Math.random() 난수
```

* `Date 클래스`

```javascript
document.write(new Date()); //데이트 클래스에서 새 객체를 만든다
```

* `Date 클래스`

```javascript

```

* `Date 클래스`

```javascript

```

#### 버튼

:`<body>` 내용 버튼으로 조작하기

```html
<body>

<h1><a href="index.html">WEB</a></h1>
<h2 style="background-color:coral; color:skyblue; width=300;">JavaScript</h2>
그냥 글자<br>
<input type="button" value="black" onclick="
document.querySelector('body').style.backgroundColor='black';
document.querySelector('body').style.color='white';
">
<input type="button" value="white" onclick="
document.querySelector('body').style.backgroundColor='white';
document.querySelector('body').style.color='black';
">

<!--toggle 눌렀을 때, 화이트면 블랙으로, 블랙이면 그대로-->
<input id="mywhite" type="button" value="toggle" onclick="
if(document.querySelector('#mywhite').value=='white'){
document.querySelector('#myblack').value='black';
document.querySelector('body').style.backgroundColor='white';
document.querySelector('body').style.color='white';
}else{
document.querySelector('body').style.backgroundColor='black';
document.querySelector('body').style.color='white';}
">
<!--버튼 눌렀을 때 블랙이면 화이트로, 화이트면 블랙으로-->
<input type="button" value="black" onclick="
var target=document.querySelector('body');
if(this.value=='black'){
target.style.backgroundColor='black';
target.style.color='white';
this.value='white';
}else{
target.style.backgroundColor='white';
target.style.color='black';
this.value='black';
}
">
</body>

```



## 배열

:값 여러개 저장

```javascript
배열을 선언하는 여러가지 방법

var n=['kim','lee',100,'park'];
var myarr1=[];
var odd=[1,3,5,7];
var even=new Array(2,4,6,8); //even=[2,4,6,8]
var mixarr=['a',1,3,new Date(), "today"];
document.write(odd[2]);

function f(){
    return['aaa','bbb'];
    }
var m=f()
document.write(m[0]);


배열 정보
document.write(arr.index0f(3)); //3이라는 자료의 인덱스 출력(0부터 시작) 없으면 -1

```

* 배열 편집

```javascript
배열 추가
var arr=[1,2,3,4];

arr.push(5); //끝에 5 추가
arr.unshift(999); //앞에 999 추가

배열 삭제
var arr=[1,2,3,4];
arr.pop(); //끝값 꺼내고 그 값을 리턴
arr.shift(); //첫값 꺼내고 그 값을 리턴
arr.splice(1,2); //(시작인덱스, 제거항목개수)를 꺼내고 그 값을 리턴

배열 정렬
var fruits=['banana','apple','orange'];
fruits.sort(); //오름차순 정렬
fruits.reverse(); //반대로 정렬(sort 먼저 해주면 내림차순)
```

* 

```javascript

```



### 객체

#### 속성

: {속성:속성값, 속성:속성값,...} (파이썬의 딕셔너리{키:값, 키:값, ...}와 비슷)

* 작성

```javascript
1)
var hgd={};
hgd['name']='honggildong';
hgd['age']=28;
hgd['gender']='m';
document.write(hgd['name']);

2)
var hgd={
'name':'honggildong',
'age':28,
'gender':'m',
}
document.write(hgd['name']);

3)new 클래스명
var hgd=new Object();
hgd['name']='honggildong';
hgd['age']=28;
hgd['gender']='m';
document.write(hgd['name']+"<br/>");


for(k in hgd){
document.write(k+"<br/>"); //속성 출력
}
for(k in hgd){
document.write(hgd[k]+"<br/>"); //속성값 출력
}
```

* 편집

```
hgd.birth=1994; //접근할 때 . 사용
document.write(hgd['birth']);

```

#### 동작

```javascript
메서드. 속성값이 함수
```

* 작성

```javascript
var hgd={
'list':{
'name':'honggildong',
'age':28,
'gender':'m'},    //속성 정의

'show':function(){  //this:현재의 객체(hgd),파이썬 self
    for(var n in this.list){
        document.write(n+":"+this.list[n]+"<br/>");
        }
    } //메서드 정의
};
hgd.show();

/*
name:honggildong
age:28
gender:m
*/
```

```javascript

```

