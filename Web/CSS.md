# CSS

:웹페이지에 출력할 내용과 스타일을 분리하기 위해 생겨남

어떤 태그들에게 어떤 스타일 효과를 적용하는 언어.



### **CSS 작성 3가지 방법**

1. html 문서의 style 속성

   ```html
   <div style="color:red">문서입니다</div>
   ```

   <div style="color:red">문서입니다</div>

2. `<style>` 태그 이용

   ```html
   <style type="text/css">
       .my-text{color:blue}
   </style>
   ```

   <!--my text라는 클래스로 묶인 내용의 글자 색상을 파랑색으로 설정-->

   * **선택자** : 어떤 태그들에 스타일을 적용할 것인지 정의하기 위한 문법

     ```html
     >>>tag 선택자
     태그{속성1:값;속성2:값;}
     
     >>>id 선택자
     #아이디{속성1:값;속성2:값;}
     
     >>>class 선택자
     .클래스{속성1:값;속성2:값;}
     
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <style>
             h3{color:#F00;}
         	span{color:#00F;}
         	#mybox{background-color:#F0B;width:200px;height:40px;}
             .yourbox{background-color:#AB0; width:200px;height:40px;}
         </style>
     </head>
     <body>
         <h3>태그로 정의된 제목</h3>
         <span>태그로 정의된 스타일</span>
         <div id="mybox">id로 정의된 스타일</div>
         <div class="yourbox">class로 정의된 스타일</div>
       
     </body>
     </html>
     ```

     ```html
     >>>부모자식 선택자
     선택자1 선택자2{속성1:값; 속성2:값;...}
     
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <style>
             div.yellowbox span{background-color:yellow;}
             div>span.blue_span{background-color:blue;}
             
             .aa >.bb>.cc{color:red}
             .aa .bb{color:skyblue}
             .xx .yy{color:green} <!--중간 뛰어넘기 가능-->
             
         </style>
     </head>
     <body>
         <div class="yellowbox">
             <span>부모자식 태그로 정의된 스타일</span></div>
         <div>
             <span class="blue_span">부모자식 태그로 정의된 스타일</span>		</div>
         
         <div class="aa">
         	<div class="bb">중간에 낀 bb
             	<div class="cc">aa와 cc</div>
         </div></div>
         <div class="xx">
             <div class="kk">중간에 낀 kk
                 <div class="yy">xx와 yy</div>
             </div>
         </div>
         
     </body>
     </html>
     ```

     ```html
     >>>다중 조건 선택자: AND, OR (선택자 사이에 공백)
     
     or 조건
     #아이디, .클래스{}
     태그, .클래스{}
     
     <head>
         <style>
             div.box{color:red;}
             div, .box{color:skyblue;} 
             <!--div태그이거나 클래스가 box면 하늘색-->
             
         </style>
     </head>
         <div class="box">box</div> <!--빨강 조건이 우선-->
     	<div>div태그</div> <!--하늘색-->
     	<span>span</span> <!--하늘색-->
     
     ```

     

3. 또 다른 방법

   