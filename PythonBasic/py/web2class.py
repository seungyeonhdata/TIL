# dic = {
#     '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#     '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#     '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',

#     '-.--':'Y','--..':'Z'
# }
# def morse(src):
#     res=[]
#     for word in src.split("  "): #word에는 단어가 저장, 입력된 문장에 저장된 단어 3개
#         for c in word.split(" "): #c에는 문자가 저장
#             res.append(dic[c])
#         res.append(" ") #단어와 단어가 공백문자로 구분
#     return "".join(res)
#
# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))



# def ngram(s, num):
#     res=[]
#     slen=len(s)-num+1
#     for i in range(slen):
#         ss=s[i:i+num]
#         res.append(ss)
#     return res
#
# def diff_ngram(sa, sb, num):
#     a=ngram(sa, num)
#     b=ngram(sb, num)
#     # print(a)
#     # print(b)
#     # ['오늘', '늘 ', ' 멀', '멀티', '티캠', '캠퍼', '퍼스', '스에', '에서', '서 ', ' 너', '너무', '무 ', ' 쉬', '쉬운', '운 ', ' 프', '프로', '로그',
#     #  '그래', '래밍', '밍을', '을 ', ' 공', '공부', '부했', '했다']
#     # ['멀티', '티캠', '캠퍼', '퍼스', '스에', '에서', '서 ', ' 공', '공부', '부했', '했던', '던 ', ' 오', '오늘', '늘의', '의 ', ' 프', '프로', '로그',
#     #  '그래', '래밍', '밍은', '은 ', ' 너', '너무', '무 ', ' 쉬', '쉬웠', '웠다']
#     cnt=0 #일치한 단어의 개수를 저장하기 위한 변수
#     r=[] #일치한 단어를 저장하기 위한 변수
#     for i in a:
#         for j in b:
#             if i==j: #두 단어(i, j)가 일치한다면
#                 cnt+=1
#                 r.append(i)
#     return cnt/len(a), r
# a="오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# b="멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
# r2, word2=diff_ngram(a, b, 2)
# print("2-gram", r2, word2) #유사도, bigram으로 묶인 단어셋
#
# r3, word3=diff_ngram(a, b, 3)
# print("3-gram", r3, word3)
#
# #수정사항
# #1)중복 허용 안되도록...
# #2) 두 문장에서 길이가 긴 문장의 단어 개수를 분모
#
# # def 입력()
# #     return 저장변수
# # def 처리()
# #     return 결과
# # def 출력()
# #     화면 출력
# #
# # 입력데이터변수=입력(데이터1, 데이터2,...)
# # 결과=처리(입력데이터변수)
# # 출력(결과)
#
# #[a-zA-Z]
# #[0-9]
# #[^0-9] : [not 0-9]
#
# # \d : 숫자([0-9])와 같음
# # \D : not \d 의미, [^0-9]과 같음
# #
# # \s : 공백문자, 탭문자, 엔터문자 등
# # \S : not 공백문자, 탭문자, 엔터문자 의미
# #
# # \w : 문자 + 숫자를 의미, [a-zA-Z0-9_]과 같음
# # \W : not 문자 + 숫자를 의미, [^a-zA-Z0-9_]과 같음
#
# #? 또는 .  : 문자가 1개만 있는지 판단
# #?는 문자가 0개 또는 1개 있으면 매치 = {0,1} = 최소 0개 이상 최대 1개 = 있어도 되고 없어도 됨
# #.은 문자가 1개인지 판단
#
# #ab?c => a + b가 있어도 없어도 됨 + c
#
# import re
# print(re.match('h?','h')) #매치됨
# print(re.match('h?','he'))
# print(re.match('h?','his'))
#
# print(re.match('ab?c','abc')) #a + b가 있어도 없어도 됨 + c
# print(re.match('ab?c','ac'))
# print(re.match('ab?c','abbc'))
# #print(re.match('abbc','abbc'))
#
# #print(re.match('h.', 'hello'))
#
#
# print(re.match('a.b', 'aab'))
# print(re.match('a.b', 'a0b'))
# print(re.match('a.b', 'ab'))
# print(re.match('a.b', 'abb'))
#
# print(re.match('a.b', 'abb'))
# print(re.match('a[.]b', 'abb'))
# # [123]
# print(re.match("[123]", "3"))
# print(re.match("[123]", "32"))
# print(re.match("[123]", "32321"))
# print(re.match("[123]+", "32321"))
# print(re.match("[123]+", "3235217"))
# print(re.match("[1-7]+", "3235217"))
# print(re.match("\d+", "3235217")) #[0-9]+
# print(re.match("[1]+", "111222"))
#
# print(re.match('a.b', 'abbbbbbb')) #.은 모든 문자 1개
# print(re.match('a[.]b', 'a.b')) #[.]은 특수문자(마침표) .
# print(re.match('a[.^#$]b', 'a#b')) #[.]은 특수문자(마침표) .
# print(re.match('a[.^#$]b', 'a%b')) #[.]은 특수문자(마침표) .
#
# # 빅데이터(파일)
# # abc.txt    [a-zA-Z0-9]+[.]+[a-zA-Z]+
# # gabc.exe
# # # abc.cf
# # 파일명.확장자
# # ...
# # sadkljf    잘못된 파일명
# # dsflkjds.dskldsfl.dslkdsfl   잘못된 파일명
#
# # fn="abctxt"
# # res=re.match("[a-zA-Z0-9]+[.]+[a-zA-Z]+",fn)
# # if  res:
# #     print("정상적인 파일명")
# # else:
# #     print("잘못된 파일명")
#
#
# print(re.match("do*g", "dg")) #o가 0번 이상 반복
# print(re.match("do*g", "dog")) #o가 0번 이상 반복
# print(re.match("do*g", "doooooooog")) #o가 0번 이상 반복
# print(re.match("do*g", "dooooooookg")) #None
#
# print(re.match("do+g", "dg")) #None
# print(re.match("do+g", "dog")) #o가 1번 이상 반복
# print(re.match("do+g", "doooooooog")) #o가 1번 이상 반복
# print(re.match("do+g", "dooooooookg")) #None
#
# #반복 :
# # {최소,최대} : 최소 횟수 이상, 최대 횟수 이하 반복
# # {최소,} : 최소 횟수 이상 반복
# # {,최대} : 최대 횟수 이하 반복
# # {숫자} : 숫자 만큼 반드시 반복
#
# print(re.match("do{2}g","dog")) #o문자가 반드시 2번 반복
# print(re.match("do{2}g","doog")) #o문자가 반드시 2번 반복
# print(re.match("do{2}g","dooooooooog")) #o문자가 너무 많이 반복 -> None
#
# print(re.match("do{2,5}g","dog")) #o문자가 2번 이상 5번 이하 반복
# print(re.match("do{2,5}g","doog")) #o문자가 반드시 2번 반복
# print(re.match("do{2,5}g","dooooooooog")) #o문자가 5번 초과 -> None
# print(re.match("do{2,5}g","dooooog")) #o문자가 5번
#
# print(re.match("do{2,}g","dog")) #o가 2번 이상
# print(re.match("do{,2}g","dog"))
# print(re.match("do{,2}g","dooog"))
#
#
# #퀴즈1
# #print(re.match("구현부분", "다양한 전화번호"))
# print(re.match("구현부분", "010-1234-5678"))
#
# # 휴대폰 전화번호
# # 3자리-4자리-4자리 (모두 숫자)
# # 010-1234-5678 정상 전화번호
# # 010-1234-5678 비정상 전화번호
# # abc-1234-5678 비정상 전화번호
# # 01c-1234-5678 비정상 전화번호
# # 010-12345-5678 비정상 전화번호
# # 010-1234-56789 비정상 전화번호
# # 010-1234-567k 비정상 전화번호
# # 01012345678 비정상 전화번호
# # 010-12345678 비정상 전화번호
# # 010-1234&5678 비정상 전화번호
# # ...
#
# print(re.match("^01([0-9])[-](\d{4})[-](\d{4})","010-1234-5677"))
# print(re.match("\d{3}[-]\d{4}[-]\d{4}","010-1234-5678"))
# print(re.match("[0-9]{3}[-][0-9]{4}[-][0-9]{4}","010-1234-5678"))
#
# # match, search, \
# # findall:정규식과 매치되는 모든 문자열을 리스트로 리턴
# # finditer: 정규식과 매치되는 모든 문자열을 반복가능한 객체 형태로 리턴
#
# print(re.match("[a-z]+", "python"))
#
# pat=re.compile("[a-z]+") #정의한 패턴을 pat에 저장
# res=pat.match("python") #패턴객체(pat)가 가지고 있는 match함수를 이용하여 주어진 문자열이 패턴에 매치되는지 확인
# print(res)
#
# print("="*50)
# print(re.match("[a-z]+", "python"))
# print(re.search("[a-z]+", "python"))
#
# print(re.match("[a-z]+", "7python"))
# print(re.search("[a-z]+", "7python8java9cpp"))
# #search 결과는 1개의 매치 객체가 리턴
#
# print(re.findall("[a-z]+", "7python8java9cpp"))
#
# # pat=re.compile("[0-9]+") #정의한 패턴을 pat에 저장
# # res=pat.findall("뉴스기사") #패턴객체(pat)가 가지고 있는 match함수를 이용하여 주어진 문자열이 패턴에 매치되는지 확인
# # print(res)
#
# # pat=re.compile("[0-9]+") #정의한 패턴을 pat에 저장
# # res=pat.findall("(서울=연합뉴스) 전명훈 김서영 기자 = 정부가 다음 주부터 적용할 새 '사회적 거리두기' 조정안을 이번 주말인 16일에 발표한다.")
# # print(res)
#
#
# res=re.finditer("[a-z]+", "7python8java9cpp")#반복 가능한 객체로 리턴
# for i in res:
#     print(i)
#     print(i.start()) #매치 시작 위치 : 1
#     print(i.end()) #매치 끝 위치 : 7
#     print(i.group()) #매치된 문자열
#     print(i.span()) #매치 시작, 끝 위치
#
# #. : 점(.) 메타문자는 모든 문자 1개와 매치. 예외(줄바꿈 문자:\n)
# print(re.match("a.b", "a0b"))
# print(re.match("a.b", "a\nb")) #None
#
# pat=re.compile("a.b", re.DOTALL) # \n문자도 포함
# print(pat.match("a\nb"))
#
# pat=re.compile("[a-z]")
# print(pat.match("python"))
# print(pat.match("Python"))
# print(pat.match("PYTHON"))
#
# pat=re.compile("[a-z]", re.I) #ignorecase
# print(pat.match("python"))
# print(pat.match("Python"))
# print(pat.match("PYTHON"))

# import re
# print(re.search("\section","kldsfkljdsfkld sdkljdskld ds \section klskds"))
# #패턴 : \s 는 엔터, 공백, 탭 등 문자
#
# print(re.search("\\\section","kldsfkljdsfkld sdkljdskld ds \section klskds"))
# print(re.search("\\\section","kldsfkljdsfkld sdkljdskld ds \section klskds"))
# #\ 문자가 문자열 자체임을 나타내기 위해서 역슬래쉬 \\\
# print(re.search("\\\section","kldsfkljdsfkld sdkljdskld ds \section klskds"))
#
# print(re.search(r"\\section", "kldsfkljdsfkld sdkljdskld ds \section klskds"))
# #r"\\section"  => \section
#
# print("="*50)
# print(re.match("ab[0-9]?c","abc"))
# print(re.match("ab[0-9]?c","ab9c"))
# print(re.match("ab.c","ab9c"))
#
# print(re.match("h{3}","hhhiii"))
# #hi가 3번 반복
# print(re.match("hi{3}","hihihihelloworld"))
# print(re.match("(hi){3,5}","hihihihelloworld"))
#
# print(re.match("[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}","042-1234-5678"))
#
# print(re.match("[ㄱ-ㅎ]+", "ㅋㅋㅋㅋ캬캬캬캬ㅋㅋㅋㅋㅎㅎㅎㅎㅎ"))
# print(re.findall("[^ㄱ-ㅎ가-힣]+", "ㅋㅋsdfㅋㅋ캬캬캬캬ㅋㅋ234ㅋㅋㅎㅎ^&%ㅎㅎㅎ"))
#
# print(re.findall("[ㄱ-ㅎ가-힣]","문자열")) #한글만 모두 추출
# print(re.findall("[^ㄱ-ㅎ가-힣]","문자열")) #한글을 제외한 모든 문자 추출

# news="""
# (서울=연합뉴스) 신선미 기자 = 국내 신종 코로나바이러스 감염증(코로나19) '3차 대유행'이 완만한 감소세로 접어든 가운데 이번 주 신규 확진자 발생 추이가 주목된다.
#
# 신규 확진자 감소세 지속이냐 재확산이냐의 흐름을 가늠해 볼 수 있기 때문이다.
#
# 지난달 말까지만 해도 연일 1천명 안팎으로 발생하던 신규 확진자는 새해 들어 600명대로 줄었다가 11일 400명대 중반까지 더 떨어진 뒤 12일에는 500명대로 소폭 증가한 상태다.
#
# 큰 틀의 통계만 보면 확실한 감소 내지 안정국면으로 접어드는 것 아니냐는 관측이 나온다.
#
# 하지만 신규 확진자가 400명∼500명대까지 낮아진 데는 주말과 휴일 검사건수 감소 영향도 있어 아직 상황을 낙관하기에는 이르다는 게 감염병 전문가들의 공통된 의견이다.
#
# 방역당국 역시 긴장의 끈을 풀기에는 위험 요인이 너무 많다며 국민 개개인의 지속적인 방역 협조를 당부하고 있다.
# """
# import re
# print(re.findall("[ㄱ-ㅎ가-힣]+",news))
#
# print(re.findall("[ㄱ-ㅎ가-힣]+[0-9]+",news))
# print(re.findall("[0-9]+[명|천]+",news))
#
# #코로나19
#
# print(re.match("[^A-Z]+", 'Hello'))
# print(re.match("[^A-Z]+", 'hello'))
#
# print(re.match("[0-9]+", 'hello119'))
# print(re.search("[0-9]+$", 'hello119'))
#
#
# print(re.search("[*]", '3 * 5')) #* 문자가 있는지 판단
# print(re.search("[*]+", '3 ** 5'))
# #print(re.search("*", '3 * 5')) #* 문자가 있는지 판단, error
# #print(re.search("*", '3 * 5'))
#
# print(re.search("\*", '3 * 5')) #특수문자 앞에 역슬래쉬(\)를 붙여주면 됨
# print(re.search("[*]+", '3 ** 5'))
#
# print(re.search("\*+", '3 **** 5'))
#
# print(re.search("\$\([a-z]+\)","$(document)"))
#
# print(re.search("[$()a-z]+","$(document)"))


#"abcabcabc ok" 문자열 있을 때 abc가 있는지 조사
# print(re.search("abc","abcabcabc ok"))
#
# s="abc"
# print(re.search("(abc)+","abcabcabc ok"))
#
# print(re.search("\w+\s+\d+[-]\d+[-]\d+", "kim 010-1234-1234"))
# #이름 +" "+ 전화번호
# res=re.search("\w+\s+\d+[-]\d+[-]\d+", "kim 010-1234-1234")
# print(res.group())
# #print(res.group().split()[0])
#
# res=re.search("(\w+)\s+(\d+[-]\d+[-]\d+)", "kim 010-1234-1234")
# print(res)
# print(res.group(0))
# print(res.group(1))
# print(res.group(2)) #2번째 그룹은 없으므로 에러


#그룹 이름을 부여

# res=re.search("(?P<name>\w+)\s+(\d+[-]\d+[-](?P<num>\d+))", "kim 010-1234-1234")
# #작성형식 : (?P<그룹명>...)
#
# print(res.group('name'))
# print(res.group('num'))
#
#
# print(re.findall("hello|hi","hello how are you bye hi hi"))

# 1.
# 입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
# 출력 예시: True False False True False

# nums=list(input("번호 10개 입력 : "))
# print(len(nums)==10 and len(nums)==len(set(nums)))

# if len(nums)==10 and len(nums)==len(set(nums)):
#     print("True")
# else:
#     print("False")



# stnum=list(range(10))
# def oncenum(num):
#     num=str(num)
#     for i in num:
#         if int(i) in stnum:
#             stnum.remove(int(i))
#         else: break
#     if len(stnum) == 0:
#         return True
#     else:return False
# print(oncenum(6789012345))

#2.
emails =[
'python@mail.example.com',
'python+kr@example.com',
'python-dojang@example.co.kr',
'python_10@example.info',
'python.dojang@e-xample.com',
'@example.com', 'python@example', 'python@example-com'] # 잘못된 형식


# import re
# right=re.compile('\S+@\S+[.]\w+')#검사 대상이 리스트일때는 compile하고 요소 조사
# for i in emails:
#     if right.findall(i):
#         print(right.findall(i))
#     else: print("잘못된 형식")
#
#
# for i in emails:
#     if right.findall(i):
#         print(right.findall(i))
#     else: print("잘못된 형식")



# print(emails)

# p=re.compile('(.+)[@](\w.+[.]\w+)')
# print(p.match("python@example-com"))
# for i in emails:
#     if p.match(i):
#         print("올바른 형식",p.findall(i))
#     else:
#         print("잘못된 형식")

#3.
# 1)[캐스터]가 캐스팅한 내용만 추출하시오
# 2)달린 댓글의 개수를 출력하시오
# 3)대전의 온도를 출력하시오
# 4)가장 많이 등장한 단어가 무엇인가요?
# 5)가장 많이 등장한 글자는 무엇이며, 총 몇 번 등장했나요? (형태소분석기)

news="""

연합뉴스TV
[날씨] 추위 대신 미세먼지 말썽…밤까지 중부 중심 눈
기사입력 2021.01.12. 오후 1:40 기사원문 스크랩 본문듣기  설정
화나요 후속기사원해요 좋아요 평가하기9 댓글9
글자 크기 변경하기
 인쇄하기 
보내기
동영상 뉴스
[앵커]

오늘은 추위가 풀리는 대신 서쪽 지역의 공기 질이 나쁘겠습니다.

중부지방을 중심으로 눈도 내리겠습니다.

기상캐스터 연결해서 날씨 정보 더 자세히 알아보겠습니다.

김민지 캐스터.

[캐스터]

네, 추위가 한층 풀렸습니다.

어제보다 옷차림을 조금 더 가볍게 하고 나왔는데도 크게 춥지 않습니다.

내륙에 내려졌던 한파특보는 모두 해제가 됐고요.

오늘 한낮에 전국에 영상권으로 올라서겠습니다.

한낮에 서울은 1도, 대전 3도, 대구 5도 등 어제보다 5도 정도 기온이 높겠습니다.

따뜻한 서풍이 불어오면서 추위의 힘이 약해지는 건데요.

이 서풍을 타고 또 미세먼지가 들어오겠습니다.

대기 정체로 먼지가 쌓이면서 오늘은 서쪽 지역을 중심으로 미세먼지 농도 나쁨 수준 보이겠고요.

밤에 중국발 오염물질까지 들어와서 내일은 전국적으로 공기 질 상황이 나쁘겠습니다.

오늘 전국에 구름이 많습니다.

차츰 중부를 중심으로 눈이 내리겠습니다.

수도권과 충남, 전북에 1~3cm, 강원 영서와 충북, 경북과 제주 산지에 최고 5cm의 눈이 내려 쌓이겠습니다.

대부분 오늘 밤이면 그칠 텐데요.

강원 영서 지역은 내일 새벽까지 눈이 이어지겠습니다.

지금은 눈발 정도만 날리고 있습니다.

눈이 쌓이면서 퇴근길 무렵에는 길이 많이 미끄럽겠습니다.

조심히 이동하시기 바랍니다.

날씨 전해 드렸습니다.
"""

# 1)
# cast=re.compile('\[캐스터.*',re.DOTALL)
# caster=print(cast.findall(news)[0][len("[캐스터]"):])
# 2)
# comment=re.findall('댓글\d+',news)
# print("댓글 수 :",comment[0][2:])
# 3)
# print("대전 기온 :",re.findall('대전\s\d+',news)[0][2:],"도")
# 4)

# words=news.split()
# counts={}
# for word in words:
#     counts[word]=counts.get(word,0)+1
# counts_max=max(counts.keys(),key=lambda k:counts[k])
# print("'{0}'(이)라는 단어가 {1}번으로 가장 많이 나왔습니다".format(counts_max,counts[counts_max]))
#
#
#
# 혜지님 풀이
# splits=news.replace('\n',' ').replace('-',' ').split(' ')
# lst = [word for word in splits if word!= '']
#
# words_count={}
# for word in lst:
#     if word in words_count:
#         words_count[word] += 1
#     else:
#         words_count[word] = 1
# sorted_words=sorted(words_count.items(), key=lambda x: x[1], reverse=True)
# print('가장 많이 등장한 단어는 "{0}" 입니다. {1}회 등장했습니다.'.format(sorted_words[0][0],sorted_words[0][1]))
#
#
# import re
#
# p=re.compile('\\[캐스터.+',re.DOTALL)
# print(p.findall(news))
# print("댓글수:",re.findall("댓글\d",new)[0][2])
# print("대전의 온도:",re.findall("대전.{,10}",new)[0][3])
#
# p=re.compile('\w+')
# res=p.findall(new)
# print(p.findall(new))
# print(type(res))
# print(res[0])
# l = []
# excount = 0
# for i in res:
# newcount = 0
# for j in res:
# if i==j:
# newcount+=1
# l.append((newcount,i))
# max1=max(l)[0]
# print(l)
# print(set([l[i][1] for i in range(len(l)) if l[i][0] >= max1]),":",max1)
#
# import re
# p=re.compile("[가-힣]+")
# print(p.findall(new))
# l=p.findall(new)
# word=dict()
# for j in l:
# for i in j:
# if i in word.keys():
# word[i]+=1
# else:word[i]=0
# print(word)
# maxnum=max(word.values())
# for i in range(len(word.keys())):
# if list(word.values())[i]==maxnum:
# print(list(word.keys())[i],":",maxnum)
#
# 이소연님 풀이
# import re
# sliced=news.split()
# sliced_s=set(sliced)
# word_cnt={}
# for i in sliced_s:
#     word_cnt[i]=sliced.count(i)
#     cnt_m=max(word_cnt.values())
# for key, value in word_cnt.items():
#     if value == cnt_m:
#         print("가장 많이 등장한 단어는?", key)
#
#
# res=re.findall("[ㄱ-ㅎ가-힣a-zA-Z]", news)
# from collections import Counter
# letters=Counter(res)
# max_let=max(letters.values())
# for key, value in letters.items():
#     if value == max_let:
#         print("가장 많이 등장한 글자는?", key)
#
#

