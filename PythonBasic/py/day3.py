# t1=(1,2,3)
# print(type(t1))

# t1=(1,2,3)
# t2=('a',3,4)
# t3=5,6
# print(t1[:2])
# print(t1+t2)
# print(t3*3)

# x=tuple(range(1,5))
# print(list(x))
# tempx=list(x)
# tempx[2]=30
# print(tempx)

# print(list(range(0,91,10)))
# print(list(range(0,4))+list(range(4,6)))

# dic={'name':'kim','add':'seoul','nn':['사과','바나나']}
# a=dict(name='kim',add='seoul',nn=['사과','바나나'])
# print(dic)
# print(a)
# print(dic['name'])

# print(dict(zip(['a','b'],[1,2]))) #zip 객체를 dict로 변환
#{'a': 1, 'b': 2}

# dic={'nn':'bear','add':'seoul','age:10'}
# print(dic.keys()) #키만 추출
# print(dic.values()) #값만 추출
# print(dic.items())
# mykey=dic.keys()
# listmykey=list(mykey)
# print(listmykey[1])
# print(len(dic))


#1. 리스트 생성
#2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
movie_rank=['닥터 스트레인지', '스플릿', '럭키']

# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키


# 2. movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append('배트맨')

# 3. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank[1:1]=['슈퍼맨']
#movie_rank.insert(1,'슈퍼맨')

# 4. movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del (movie_rank[3])
#movie_rank.remove('럭키')


# 5. movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank[2:]=[]

# 6. price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)

price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]
print(price[1:])

# 7.슬라이싱을 사용해서 홀수만 출력하라.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 8.슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.

nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]
print(nums[::-1])

# 9.interest 리스트에는 아래의 데이터가 저장되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자 Naver
print(' '.join(interest[::2]))

# 10. interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print(' '.join(interest))

#
# 11. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
#
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print('\n'.join(interest))


# 12. 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 13.
# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
# ※ 문자열 슬라이싱 기법을 사용해 보자.
number='881120-1068234'
print(number[:6])

# 14
# (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
# ※ 더하기(+)를 사용해 보자.
tu=1,2,3
tu2=4,
print(tu+tu2)

a=(1,2,3)
a+=(4,)
print(a)

# 15
# 다음과 같은 딕셔너리 a가 있다.
a = dict()
a
{}

# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
a['name'] = 'python'
a[('a',)] = 'python'
#a[[1]] = 'python' #리스트는 키가 될 수 없음
#오류: 딕셔너리는 시퀀스가 아님 -> 인덱싱으로 참조할 수 없다
a[250] = 'python'

# 16
# 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A':90, 'B':80, 'C':70}
# ※ 딕셔너리의 pop 함수를 사용해 보자.
print(a.pop('B'))





