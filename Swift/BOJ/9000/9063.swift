let count = Int(readLine()!)!

var array1: [Int] = []
var array2: [Int] = []

for _ in 1...count {
  let spot = readLine()!.split{ $0 == " " }.map{ Int($0)! }
  let x = spot[0], y = spot[1]
  array1.append(x)
  array2.append(y)
}

let width = array1.max()! - array1.min()!
let height = array2.max()! - array2.min()!

// 그냥 print(width * height)를 해도 주어진 점이 1개일때 0이 나오긴한다.
// 하지만 이 코드의 시간이 좀 더 적게 걸린다 4ms의 차이이긴 하지만..
if count == 1 {
  print(0)
} else {
  print(width * height)
}
