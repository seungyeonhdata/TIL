# Javascript

:객체 기반 클라이언트 스크립트 작성 언어. 생성된 객체를 이용하여 동적인 페이지를 기술한다. 확장자는 js

※`/* 주석은 // 여러 줄이면 별과 슬래시로 감싸기 */`

※`/* 주석은 // 여러 줄이면 별과 슬래시로 감싸기 */`



### 작성법

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

8.  



### 조건문

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





### 함수

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
alert("1"==1); //내부적으로 여산을 하기 전에 자동 형 변환 True
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

* `Date 클래스`

```javascript

```

