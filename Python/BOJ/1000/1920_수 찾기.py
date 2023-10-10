n = int(input())
A = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
A.sort()

for num in check:
    left, right = 0, n - 1
    exist = False

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == num:
            exist = True
            print(1)
            break
        elif A[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    
    if not exist:
        print(0)

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for b in B:
    print(1) if b in A else print(0)
