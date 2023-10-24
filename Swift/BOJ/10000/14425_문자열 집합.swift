let input = readLine()!.split(separator: " ")
let n = Int(input[0])!
let m = Int(input[1])!
var answer = 0

var dict: [String : Bool] = [:]

for _ in 1...n {
  dict[readLine()!] = true
}

for _ in 1...m {
  if dict[readLine()!] != nil {
    answer += 1
  }
}
print(answer)
