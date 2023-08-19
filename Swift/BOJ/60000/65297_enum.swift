// enum.ver

// 변수 두 개 생성 
var totalSum = 0.0
var sum = 0.0

// 20개의 과목이 입력됨
for _ in 0..<20 {
  let input = readLine()!.split(separator: " ")
  guard input[2] != "P" else { continue }  // 과목이 "P"일 땐 continue
  
  var multiple = 0.0
  switch input[2] {
    case "A+": multiple = 4.5
    case "A0": multiple = 4.0
    case "B+": multiple = 3.5
    case "B0": multiple = 3.0
    case "C+": multiple = 2.5
    case "C0": multiple = 2.0
    case "D+": multiple = 1.5
    case "D0": multiple = 1.0
    case "F": multiple = 0.0
    default: break  // 까먹지 말자 default
  }
  let num = Double(input[1])!
  totalSum += (num * multiple)
  sum += num
}

print(totalSum / sum)
