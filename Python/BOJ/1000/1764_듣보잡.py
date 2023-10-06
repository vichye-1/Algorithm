# dictionary 풀이
n, m = map(int, input().split())
person = {}
answer = 0
names = []
for i in range(n):
    listen = input()
    if listen not in person:
        person[listen] = 1
for j in range(m):
    see = input()
    if see in person:
        person[see] += 1
for (a, b) in person.items():
    if b == 2:
        answer += 1
        names.append(a)
names.sort()
print(answer)
print("\n".join(names))

# set()이용 풀이
# set()의 '&'기능을 사용하는 풀이법이 참신했다. 처음 풀이보다 짧기도했고, 소요시간도 덜했다.
n, m = map(int, input().split())
listen = []
see = []
for _ in range(n):
    listen.append(input())
for _ in range(m):
    see.append(input())
same = sorted(list(set(listen) & set(see)))
print(len(same))
print("\n".join(same))
