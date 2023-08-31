let input = readLine()!.split{ $0 == " " }.map{ Int($0)! }.sorted()
if input.last! < input[0] + input[1] {
  print(input.reduce(0, +))
} else {
  print((input[0] + input[1]) * 2 - 1)
}
