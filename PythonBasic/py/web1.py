#정규표현식
# jumin="""
# park 850201-1264597
# kim 95d544-1523654
# """

import re
# p=re.compile("(\d{6})[-]\d{7}")
# print(p.sub("\g<1>-*******",jumin))

# re.match("패턴","문자열") #문자열이 패턴에 부합되나요?

# print(re.match("hi", "hello, world"))
#None (거짓)

print(re.match("[abcdef]","a")) #매치됨
print(re.match("[abcdef]","g")) #매치 안됨
print(re.match("[abcdef]","abc")) #매치됨
print(re.match("[abcdef]","c")) #매치됨

# print(re.match("hello", "hello, world")) #매치는 일치하지 않는 부분 나오면 바로 끝남
#<re.Match object; span=(0,5), match='hello'>

#특정 문자열이 맨앞/뒤에 오는지 판단
#^맨앞
#$맨뒤
# print(re.search("^hello", "hello, world"))
#print(re.search("world$", "hello, world"))

#hello 또는 world 문자열이 포함되어 있는지 확인
# print(re.match("hello|world", "hello")) #or의 의미

#[] :안에 써 있는 문자들 중 하나와 매치가 되는가

#[from-to] : [a-z0-9] -로 문자범위 명세. 소문자나 숫자만 가능
#[\d]=[0-9]
print(re.match('[0-9]','1234')) #앞에서부터 하나만 매치
print(re.match('[0-9]*','1234'))#*은 문자(숫자)가 0개 이상 있으면 매치
print(re.match('[0-9]*','a1234')) # *있으면 0개로 판단, 없으면 none
print(re.match('[0-9]+','1234')) #+는 1개 이상 있으면 매치
print(re.match('[0-9]+','a1234')) #None
print(re.match('a*b','b')) #a가 0개 이상 있고 b가 나오면 매치
print(re.match('a+b','b')) #a가 1개 이상 있고 b가 나오면 매치
#[a-z],[A-Z],[a-zA-Z] 알파벳 겁색
#[^0-9] ^뒤에 오는 문자를 제외

print(re.search('^hi','hello,hi')) #문자열이 hi로 시작하나
