while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    numlist = sorted([a, b, c])
    if numlist[-1] ** 2 == numlist[0] ** 2 + numlist[1] ** 2:
        print("right")
    else:
        print("wrong")
