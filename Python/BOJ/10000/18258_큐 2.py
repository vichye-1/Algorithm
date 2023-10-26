import sys
from collections import deque
deq = deque()
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        deq.append(command[1])
    elif command[0] == "pop":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deq))
    elif command[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)
