# 1.
# a=[1,3,5,7,9,0,2,4,6,8]
# l=int(len(a)/2)
# 혹은 몫구하기 l=len(a)//2
# print(a[:l])
# print(a[l:])
# print(a[::-1])
# print(a[::-2])
# print(a[-2::-2])
#
# 2.
# def fibonacci():
#     n=int(input("n:"))
#     a=[0,1]
#     if n<2:
#         print(a[0])
#     elif n<3:
#         print(a[0], a[1])
#     else:
#         for i in range(3,n+1):
#             b=a[-1]+a[-2]
#             a.append(b)
#         print(a)

# 3.
# def repeat_count():
#     abc=input("문자열 입력:")
#     count=0
#     res=abc[0]
#     for i in abc:
#         if i==res[-1]:
#             count+=1
#         else:
#             res+=str(count)+i
#             count=1
#     print(res)
# repeat_count()


# a = input("압축할 문자열 입력 : ") + chr(32)
# b = ''
# count = 1
# for i in range(len(a) - 1):
#     if a[i] == a[i + 1]:
#         count += 1
#     else:
#         b += a[i]+str(count)
#         count = 1
# print(b)


# test = 'aaabbcccccca'
# dic = {}
#
# for i in range(len(test)):
#   dic[test[i]] = 0
# for i in range(len(test)):
#   dic[test[i]] += 1
#
# l = ''
# for k,v in dic.items():
#   l += k + str(v)
#
# print(l)

# 4.
# list=[]
# for i in range(10):
#     for j in range(10):
#         list.append(i*j)
# for l in range(10):
#     for m in range(10):
#         for n in range(10):
#             list.append(l*m*n)
# print(sum(list))


# sum=0
# for i in range(10,1001):
#     a = 1
#     for j in str(i):
#         a=a*int(j)
#     sum+=a
# print(sum)


# print(sum(eval('*'.join(str(x))) for x in range(10,1001)))


#5.
# n=[[2,4,1,2,1],[3,4,2,3,3],[2,4,1,2,2],[4,4,4,1,2],[4,2,3,3,2]]
# # print(nums)
# #가로 검사
# li=[]
# mark=0
# for i in range(5):
#     # print(i)
#     for j in range(5):
#         while n[i][j]!=0:
#             if j<3 and n[i][j]==n[i][j+1]==n[i][j+2]:
#                 mark=1
#                 x=j
#                 while x<5 and n[i][j]==n[i][x]:
#                     li.append(i,x)
#                     x+=1
# for l in li:
#     n[l[0]][l[1]]=0
# print(n)



# def peung(board):
#     while(peung_chain(board)):
#         filled_board(board)
#
# #3개 이상 연속되어 있는 블럭을 터뜨리는 함수
# def peung_chain(board):
#     peung_list = []
#
#     flag = 0    #3개 이상 연속되는 블럭이 있었는지를 체크하는 플래그
#     for i in range(5):
#         for j in range(5):
#             if board[i][j] != 0:
#                 #같은 열에 3개 이상 같은 블럭이 반복되는지.
#                 if j<3 and (board[i][j] == board[i][j+1] == board[i][j+2]):
#                     flag =1
#                     k = j
#                     while (k<5 and (board[i][j] == board[i][k])):
#                         peung_list.append((i,k))
#                         k+=1
#                 #같은 행에 3개 이상 같은 블럭이 반복되는지
#                 if i<3 and (board[i][j] == board[i+1][j] == board[i+2][j]):
#                     flag = 1
#                     k = i
#                     while (k<5 and (board[i][j] == board[k][j]) ):
#                         peung_list.append((k,j))
#                         k+=1
#
#     for item in peung_list:
#         board[item[0]][item[1]] = 0
#
#     if flag == 1:
#         return True
#     else: return False
#
# #빈공간 채우기 함수
# def filled_board(board):
#     #두번째 행 부터 원소가 0이고 이전 행의 같은 열 원소가 0이 아닌 경우 내리기
#     for i in range(1,5):
#         for j in range(5):
#             k=i
#             while(k> 0):
#                 if board[k][j] == 0 and board[k-1][j] != 0:
#                     board[k][j] = board[k-1][j]
#                     board[k-1][j] = 0
#                     k-=1
#                 else: break
#
# #보드 출력 함수
# def print_board(board):
#     for i in range(5):
#         print("{0} {1} {2} {3} {4}".format(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]))
#     print("")
#
# def main():
#     board = [[2, 4, 1, 2, 1], [3, 4, 2, 3, 3], [2, 4, 1, 2, 2], [4, 4, 4, 1, 2], [4, 2, 3, 3, 2]]
#     peung(board)
#     print_board(board)
#
#
# main()

# greedy
# backtracking
# dp(dynamic programming)

