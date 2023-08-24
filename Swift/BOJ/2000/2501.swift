let input = readLine()!.split{ $0 == " " }.map{ Int($0)! }
var array: [Int] = [1]

for i in 2...input[0] {
  if input[0] % i == 0 { array.append(i) }
}

if array.count < input[1] { print(0) }
else { print(array[input[1] - 1]) }
