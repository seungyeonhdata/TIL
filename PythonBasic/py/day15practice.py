def inout_log():
    with open ("inout_log.txt","r") as f:
        timelog=f.readline()
    time=timelog.split('\n')
    list=[time[i].split() for i in range(len(time))]
    return list

def check_remaining():
    list=inout_log()
    input_time=input('시간 입력:')
    remain=0
    for i in list:
        if i[0]<=input_time<=i[1]:
            remain+=1
        else:
            break
    print(remain,"명 남았습니다.")

check_remaining()


# def workman(nowtime):
#     a=inout_log()
#     b=len(a)
#     num=0
#     for i in range(b):
#         a[i].append(nowtime)
#         a[i].sort()
#         if a[i][1]==str(nowtime):
#             num+=1
#     print(num)
#
# workman("11:15:11")