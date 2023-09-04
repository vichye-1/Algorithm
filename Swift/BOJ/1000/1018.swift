let input = readLine()!.split{ $0 == " " }.map{ Int($0)! }
var chess: [[String]] = []

for _ in 1...input[0] {
  let line = readLine()!.map{ String($0) } 
  chess.append(line)
}

let gapX = input[0] - 8
let gapY = input[1] - 8

var answer = 64

for i in 0...gapX {
  for j in 0...gapY {
    var countW = 0
    var countB = 0
    
    for x in 0 + i..<8 + i {
      for y in 0 + j..<8 + j {
        if (x + y) % 2 == 0 {
          if chess[x][y] == "W" {
            countB += 1
          } else {
            countW += 1
          }
        } else {
          if chess[x][y] == "W" {
            countW += 1 
          } else {
            countB += 1
          }
        }
      }
    }
    answer = min(answer, countW, countB)
  }
}
print(answer)
