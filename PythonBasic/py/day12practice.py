#
# from selenium import webdriver
# driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
# url="https://movie.naver.com/movie/bi/mi/review.nhn?code=163834&page=1"
# driver.get(url)
#
# def select_page(driver):
#     while True:
#         try:
#             n = int(input("페이지 번호를 입력하세요 :"))
#             if n > 0:
#                 n_page="https://movie.naver.com/movie/bi/mi/review.nhn?code=163834&page="+str(n)
#                 driver.get(n_page)
#                 break
#         except:
#             print("0보다 큰 정수를 입력하세요.")
#
# select_page(driver)
#
# def select_comments(driver):
#     while True:
#         try:
#             n = int(input("댓글 번호를 입력하세요 :"))
#             if n > 0:
#                 n_comments = driver.find_element_by_css_selector("#reviewTab > div > div > ul > li:nth-child({}) > p > a".format(n))
#                 n_comments.click()
#                 break
#         except:
#             print("1에서 10 사이의 정수를 입력하세요.")
# select_comments(driver)
#
# def read_comments(driver):
#     # import time
#     from bs4 import BeautifulSoup
#     # time.sleep(2)
#     source=driver.page_source
#     soup=BeautifulSoup(source,"html.parser")
#     comments=soup.select("#content > div.article > div.obj_section.noline.center_obj > div.review > div.user_tx_area>p")
#     print(comments)
# read_comments(driver)


# def largest_number(list):
# list=[3,30,34,5,9]
# sum=0
# nums=[]
# num=[]
# for li in list:
#     li=str(li)
#     for i in li:
#         nums.append(i)
# for n in nums:
#     n=int(n)
#     num.append(n)
# num.sort(reverse=True)
# for i in num:
#     print(i)



# list = [3,30,34,5,9]
# a = [] # 뽑아낸수저장 장소
# for i in range(len(list)):
#     b = str(list[i])
#     for j in range(len(b)):
#         a.append(b[j])
#
# c = int(''.join(map(str,sorted(a, reverse=True))))
# # c=''.join(c)
# # c=int(c)
# print(c)

# def largest_combi(list):
#     nums=''
#     li=[]
#     for i in list:
#         li.append(str(i))
#     for num in nums:
#         li.append(num)
#     li.sort(reverse=True)
#     print(''.join(li))
# largest_combi([3,30,34,5,9])


# chart=[[0 for x in range(8)] for y in range(8)]
# print(chart)
#
# ans=0
# for n in range(4):
#     l_x,l_y,r_x,r_y=map(int,input("왼쪽 아래x,y좌표, 오른쪽 위 x,y좌표 순서대로 입력 :").split())
#
#     for i in range(l_x,r_x):
#         for j in range(l_y,r_y):
#             chart[j][i]=1
#
# print(chart)
# for one in chart:
#     ans+=sum(one)
#
# print("겹쳐진 직사각형들이 차지하는 면적:",ans)


# whole=[[0 for i in range(1001)] for i in range(1001)]
#
# for i in range(4):
#     x1, y1, x2, y2 = map(int, input().split())
#
#     # 사각형 부분만 1로 바꾸어줌
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             whole[i][j] = 1
# ans=0
# for row in paper:
#     ans+=sum(row)
# print(ans)

# base = [[0 for _ in range(1001)] for _ in range(1001)]
# # x, y좌표는 1 이상이고 1000 이하, 그 좌표들을 0으로 채움
# cnt=0
#
# for x in range(4):
#     x1, y1, x2, y2 = map(int, input('%d번 직사각형 좌표를 입력하세요: ' %(x+1)).split())
#
#     # 사각형 1로 채우기
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             base[i][j] = 1
#
# res = 0
# for a in base:
#     res += sum(a) #결과 = 1로 채워진 부분의 합
# print(res)

# #직사각형 면적 구하기
# arr = [[0] * 100 for _ in range(100)]
# x, y좌표는 1 이상이고 1000 이하, 그 좌표들을 0으로 채움
# cnt = 0
# for i in range(4):
#     x_l, y_l, x_r, y_r = map(int, input().split())
#     for j in range(x_l, x_r):
#         for k in range(y_l, y_r):
#             if arr[k][j] == 0:
#                 arr[k][j] = 1
#                 cnt += 1
# print(cnt)

# def squareArea():
#     area=set()
#     for i in range(4):
#         sq = list(map(int, input().split()))
#         for x in range(sq[0],sq[2]):
#             for y in range(sq[1],sq[3]):
#                 area.add((x,y))
#     print(len(area))
#
#
# squareArea(1 2 4 4 2 3 5 7 3 1 6 5 7 3 8 6)














