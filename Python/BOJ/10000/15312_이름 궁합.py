write = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = input()
B = input()
nums = []

for i in range(len(A)):
    nums.append(write[ord(A[i]) - ord("A")])
    nums.append(write[ord(B[i]) - ord("A")])

temp = []

while len(nums) != 2:
    for j in range(1, len(nums)):
        temp.append((nums[j] + nums[j - 1]) % 10)
    nums = temp
    temp = []
print(f"{nums[0]}{nums[1]}")
