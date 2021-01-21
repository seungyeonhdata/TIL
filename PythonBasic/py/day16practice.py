def triangle():
    angle=[int(i) for i in input("값:").split(',')]
    if sum(angle)!=180 or len(angle)!=3 or any(a<=0 for a in angle):
        print("삼각형이 아니다")
    elif any(a>90 for a in angle):
        print("둔각삼각형")
    elif any(a==90 for a in angle):
        print("직각삼각형")
    else:
        print("예각삼각형")
triangle()