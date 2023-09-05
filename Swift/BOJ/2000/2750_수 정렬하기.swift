let count = Int(readLine()!)!
var array = [Int]()
for _ in 1...count {
  array.append(Int(readLine()!)!)
}
array.sort()
for num in array {
  print(num)
}
