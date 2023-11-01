from collections import deque

n = int(input())
students = deque(map(int, input().split()))
stack = []
target = 1

while students:
    if students[0] == target:
        students.popleft()
        target += 1
    else:
        stack.append(students.popleft())
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

print("Nice" if not stack else "Sad")
