//dictionary 버전

// 등급에 따른 과목평점 딕셔너리로 저장 
let gradeDict: [String: Double] = ["A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0":	2.0, "D+": 1.5, "D0": 1.0, "F":	0.0]

var sum = 0.0
var totalSum = 0.0

for _ in 1...20 {
  let input = readLine()!.split(separator: " ").map{ String($0) }

  // dictionary에서 subscript 값은 optional로 반환된다. 따라서 if let을 사용해야 에러가 나지 않는다
  if let grade = gradeDict[input[2]] {  
    sum += Double(input[1])!
    totalSum += Double(input[1])! * grade  
  }
}
print(totalSum / sum)
