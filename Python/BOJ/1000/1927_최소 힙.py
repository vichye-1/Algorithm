import sys
import heapq

heap = []
for _ in range(int(input())):
    a = int(sys.stdin.readline())
    if a:
        heapq.heappush(heap, a)
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
