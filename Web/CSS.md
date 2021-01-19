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

     ```
     >>>tag 선택자
     태그{속성1:값;속성2:값;}
     
     >>>id 선택자
     #아이디{속성1:값;속성2:값;}
     
     >>>class 선택자
     .클래스{속성1:값;속성2:값;}
     
     >>>부모자식 선택자
     선택자1 선택자2{속성1:값; 속성2:값;...}
     ```

     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <style>
             h3{color:#F00;}
         	span{color:#00F;}
         	#mybox{background-color:#F0B;width:200px;height:40px;}
             .yourbox{background-color:#AB0; width:200px;height:40px;}
             div.yellowbox span{background-color:yellow;}
         </style>
     </head>
     <body>
         <h3>태그로 정의된 제목</h3>
         <span>태그로 정의된 스타일</span>
         <div id="mybox">id로 정의된 스타일</div>
         <div class="yourbox">class로 정의된 스타일</div>
         <div class="yellowbox">
             <span>부모자식 태그로 정의된 스타일</span>
         </div>
     </body>
     </html>
     ```

     ```
     
     ```

     

3. 또 다른 방법

   