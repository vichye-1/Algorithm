var array = [Int]()
for _ in 1...Int(readLine()!)! {
  array.append(Int(readLine()!)!)
}
array.sort()
print(array.map{ String($0) }.joined(separator: "\n"))
