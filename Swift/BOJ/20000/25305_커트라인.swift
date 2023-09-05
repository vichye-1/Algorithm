let count = readLine()!.split{ $0 == " " }.map{ Int($0)! }
var scores = readLine()!.split{ $0 == " " }.map{ Int($0)! }.sorted(by: >)
print(scores[count[1] - 1])
