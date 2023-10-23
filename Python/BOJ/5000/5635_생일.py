students = []
for _ in range(int(input())):
    name, day, month, year = input().split()
    students.append([name, int(day), int(month), int(year)])
students.sort(key = lambda x: (x[3], x[2], x[1]))
print(students[-1][0])
print(students[0][0])
