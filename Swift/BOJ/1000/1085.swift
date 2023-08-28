let input = readLine()!.split{ $0 == " " }.map{ Int($0)! }
let x = input[0], y = input[1], width = input[2], height = input[3]
print(min(x, y, width - x, height - y))
