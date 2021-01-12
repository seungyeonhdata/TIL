import re
# . 문자 1개
# ? 문자 0개 혹은 1개
# \d [0-9]
# \D [^0-9]
# \s [공백, 탭, 엔터문자]
# \S [not 공백, 탭, 엔터]
# \w [a-zA-Z0-9_]
# \W [^a-zA-Z0-9_]
#
#{a,b} a번 이상 b번 이하 반복

# 핸드폰번호
# 3자리-4자리-4자리
# print(re.match("\d{3}-\d{4}-\d{4}","010-1111-4545"))
# /^\d{3}-\d{3,4}-\d{4}$

# print(re.findall('[a-z]+','7python'))
#
# res=re.finditer("[a-z]+","7python") #반복 가능한 객체로 리턴
# for i in res:
#     print(i)
#     print(i.start())
#     print(i.end())
#
# # . 모든 문자, 줄바꿈문자 예외
# print(re.match("a.b","a0b"))
# print(re.match("a.b","a\nb"))
# pat=re.compile("a.b",re.DOTALL) #\n문자 포함
# print(pat.match("a\nb"))
#
# #대소문자 구분
# pat=re.compile("[a-z]")
# print(pat.match("python"))
# print(pat.match("Python"))
# pat=re.compile("[a-z]",re.I) #대소문자 무시
# print(pat.match("python"))
# print(pat.match("Python"))

# print(re.search(r"\\section","dke jfljs\section"))
# print(re.search(".section","dke jfljs\ssection"))
# #\를 문자열로 인식하려면 \\\ or r"\\"
# print(re.findall("[^ㄱ-ㅎ가-힣]+","ㅋㅋfe#ㅋㅋ캬컇ㅎ22ㅎ"))
# print(re.findall("[ㄱ-ㅎ가-힣]","문자열"))
# print(re.findall("[ㄱ-ㅎ가-힣]+","문자열"))

news="""
(서울=연합뉴스) 신선미 기자 = 국내 신종 코로나바이러스 감염증(코로나19) '3차 대유행'이 
완만한 감소세로 접어든 가운데 이번 주 신규 확진자 발생 추이가 주목된다.
신규 확진자 감소세 지속이냐 재확산이냐의 흐름을 가늠해 볼 수 있기 때문이다.
지난달 말까지만 해도 연일 1천명 안팎으로 발생하던 신규 확진자는 새해 들어 600명대로 
줄었다가 11일 400명대 중반까지 더 떨어진 뒤 12일에는 500명대로 소폭 증가한 상태다.
큰 틀의 통계만 보면 확실한 감소 내지 안정국면으로 접어드는 것 아니냐는 관측이 나온다.
하지만 신규 확진자가 400명∼500명대까지 낮아진 데는 주말과 휴일 검사건수 감소 영향도 있어 
아직 상황을 낙관하기에는 이르다는 게 감염병 전문가들의 공통된 의견이다.
방역당국 역시 긴장의 끈을 풀기에는 위험 요인이 너무 많다며 국민 개개인의 지속적인 
방역 협조를 당부하고 있다.
"""
# print(re.findall("[ㄱ-ㅎ가-힣]+",news))
# print(re.findall("[0-9]+[명|천]+",news))

# data.go.kr
# csv=comma seperated value
# open API 보면 Json-XML 있음

# *문자 매칭
# print(re.search("[*]","3*5"))
# print(re.search("\*","3*5"))


print(re.search("\$\([a-z]+\)","$(document)"))
print(re.search("[$()a-z]+","$(document)"))

