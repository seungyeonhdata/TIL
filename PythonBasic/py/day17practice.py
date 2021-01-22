# import random
#
# while True:
#     option=["가위","바위","보"]
#     com=random.choice(option)
#     user=input("가위 바위 보!(그만하려면 0):")
#     if user=="가위":
#         if com=="가위":
#             res="비겼습니다."
#         elif com=="바위":
#             res="졌습니다."
#         else:
#             res="이겼습니다."
#     elif user=="바위":
#         if com=="가위":
#             res="이겼습니다."
#         elif com=="바위":
#             res="비겼습니다."
#         else:
#             res="졌습니다."
#     elif user=="보":
#         if com=="가위":
#             res="졌습니다."
#         elif com=="바위":
#             res="이겼습니다."
#         else:
#             res="비겼습니다."
#     elif user=='0':
#         break
#     print("컴퓨터는",com, res)
# print("잘 싸웠습니다.")

def lotto():
    import random
    winner = random.sample(range(1, 45), 6)
    amount = int(input("로또를 몇개 구매하시겠습니까?:"))
    won = "현재 당첨번호는 {} 입니다.".format(winner)
    print(won)
    for n in range(amount):
        yours = random.sample(range(1, 45), 6)
        res=[i for i in winner if i in yours]
        if len(res) < 3:
            rank="입니다."
        elif len(res) < 4:
            rank="4등입니다(5천원)"
        elif len(res) < 5:
            rank="3등입니다(5만원)"
        elif len(res) < 6:
            rank="2등입니다(2백만원)"
        else:
            rank="1등입니다(10억원)"
        print("구매하신 추첨번호는",yours,rank)
lotto()
