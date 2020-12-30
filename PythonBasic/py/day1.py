# a,b = input("두 수 입력해").split()
 # split앞에 있는 문자열을 공백으로 분리

# a,b=(input("숫자 두 개 입력 : ").split())
# print(int(a)+int(b))

# a,b=map(int,input("숫자 두 개 입력 : ").split())
# print(a+b)

# x = 'life is too short'
# print(x[8:-3])

# i를 y로 바꾸고 싶을 때
# x='pithon'
# x=x[0:1]+"y"+x[2:]
# print(x)

# 연습 문제
# 1. 첫번째와 세번째 문자를 출력하세요.
letters='python'
print(letters[0]+letters[2])

# 2.뒤에 4자리만 출력하세요.
cn="24가 2210"
print(cn[-4:])

# 3. 문자열에서 '파' 만 출력하세요.
s="파이썬파이썬파이썬"
print(s[::3])

# 4.문자열 '720'를 정수형으로 변환해보세요.
num_str="720"
num_int=int(num_str)
print(type(num_int))

# 5. 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
data="15.79"
f_data=float(data)
print(type(f_data))

# 6. 에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서
# 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요.
pay=48584
month=36
total=pay*month
print("총 금액은",total,"원입니다.")

