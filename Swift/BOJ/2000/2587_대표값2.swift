// reduce사용 - 시간 복잡도 O(n) / sort - 시간복잡도 O(nlogn)
var array = [Int]()
for _ in 0..<5 {
  array.append(Int(readLine()!)!)
}
array.sort()
print(array.reduce(0, +) / 5)
print(array[2])

// append사용 - 시간복잡도 O(1) / sort - 시간복잡도 O(nlongn)
var array = [Int]()
var sum = 0
for _ in 0..<5 {
  let n = Int(readLine()!)!
  array.append(n)
  sum += n
}
array.sort()
print(sum / 5)
print(array[2])
