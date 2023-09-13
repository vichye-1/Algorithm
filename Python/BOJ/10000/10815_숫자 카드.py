# dictionary
n = input()
cards = input().split(" ")
m = input()
nums = input().split(" ")

dict = {}
for card in cards:
    dict[card] = 0

for num in nums:
    if num not in dict:
        print(0, end = " ")
    else:
        print(1, end = " ")

# binary search
n = int(input())
cards = sorted(input().split(" "))
m = input()
nums = input().split(" ")

for num in nums:
    low = 0
    high = n - 1
    temp = False
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] > num:
            high = mid - 1
        elif cards[mid] < num:
            low = mid + 1
        else:
            temp = True
            break
    print(1 if temp else 0, end = " ")
