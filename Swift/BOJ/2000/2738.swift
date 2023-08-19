// 행과 열의 값을 받고, 따로 변수 명을 설정해줌
let countMatrix = readLine()!.split(separator: " ").map{ Int($0)! }
let row = countMatrix[0], column = countMatrix[1]

// 두 개의 행렬을 만들고, 더한 값을 저장할 수 있는 행렬 하나를 만든다
var matrixA: [[Int]] = []
var matrixB: [[Int]] = []
var answer = [[Int]](repeating: [Int](repeating: 0, count: column), count: row)

// 행렬 A에 input값 저장
for _ in 1...row {
  matrixA.append(readLine()!.split(separator: " ").map{ Int($0)! })
}

// 행렬 B에 input값 저장
for _ in 1...row {
  matrixB.append(readLine()!.split(separator: " ").map{ Int($0)! })
}

// 행렬 A, B 더한 값 answer 행렬에 값 저장
for x in 0..<row {
  for y in 0..<column {
    answer[x][y] = matrixA[x][y] + matrixB[x][y]
  }
}

// answer array 안에 들어있는 값 꺼내기 
for i in 0..<row {
  print(answer[i].map{ String($0) }.joined(separator: " "))
}

/* 마지막에 값 도출할 때 forEach{ } 도 쓸 수 있음. 하지만 map과 joined를 사용하는 게 시간이 더 적게 걸림.
for i in 0..<row {
  answer[i].forEach{ print($0, terminator: " ") }
  print()
}
*/

