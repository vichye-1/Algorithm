var input = readLine()!.split{ $0 == " " }.map{ Int($0)! }
let cards = readLine()!.split{$0 == " " }.map{ Int($0)! }
let n = input[0], m = input[1]
print(compare(n, m, cards))

func compare(_ n: Int, _ m: Int, _ cards: [Int]) -> Int{
  var maxNum = 0
  for i in 0..<n {
    for j in i + 1..<n {
      for k in j + 1..<n {
        let sum = cards[i] + cards[j] + cards[k]
        if m >= sum && sum >= maxNum {
          maxNum = sum
        }
      }
    }
  }
  return maxNum
}
