var array = [Int]()
for _ in 1...Int(readLine()!)! {
  array.append(Int(readLine()!)!)
}

print(array.sorted().map{ String($0) }.joined(separator: "\n"))
