word = list(input())
array = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        w1 = word[:i]
        w2 = word[i : j]
        w3 = word[j:]
        w1.reverse()
        w2.reverse()
        w3.reverse()
        result = w1 + w2 + w3
        array.append(result)

array.sort()
print("".join(array[0]))
