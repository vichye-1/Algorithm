let input = readLine()!.split(separator: " ").map{ Int($0)! }
print(String(input[0], radix: input[1]).uppercased())

// input[0], input[1]은 모두 Int
