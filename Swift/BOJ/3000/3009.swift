// x값과 y값이 2개씩 있어야 직사각형이 완성됨
// 딕셔너리를 이용하여 개수를 세고, 개수가 1이면 x값과 y값을 프린트하도록 한다

var tuple: [(Int, Int)] = []

for _ in 1...3 {
  let input = readLine()!.split{ $0 == " " }.map{ Int($0)! }
  tuple.append((input[0], input[1]))
}

let dictX = Dictionary(tuple.map{ ($0.0, 1) }, uniquingKeysWith: +)
let dictY = Dictionary(tuple.map{ ($0.1, 1) }, uniquingKeysWith: +)

print(dictX.first{ $0.value == 1 }!.key, dictY.first{ $0.value == 1 }!.key)
