var countingSort = [Int](repeating: 0, count: 10001)

for _ in 1...Int(readLine()!)! {
  countingSort[Int(readLine()!)!] += 1
}

var answer = ""

for i in 1...10000 {
  answer += String(repeating: "\(i)\n", count: countingSort[i])
}

print(answer)
