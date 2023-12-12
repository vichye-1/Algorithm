import sys
from heapq import heappush, heappop

heap = []
for _ in range(int(input())):
    a = int(sys.stdin.readline())
    if a:
        heappush(heap, (-a, a))
    else:
        if len(heap) > 0:
            print(heappop(heap)[1])
        else:
            print(0)
