// 2차원 배열을 담을 빈 배열 만들기
var matrix: [[Int]] = []

// 빈 2차원 배열에 숫자 넣기
for _ in 1...9 {
  matrix.append(readLine()!.split(separator: " ").map{ Int($0)! })
}

// flatmap을 사용해서 2차원 배열을 1차원 배열로 평탄화하고, 최댓값을 'maxNum'에 저장
let maxNum = matrix.flatMap{ $0 }.max()!

// 배열을 인덱스 순으로 돌며 최댓값과 같으면 
// 최댓값, 행 인덱스 + 1, 열 인덱스 + 1 한 값을 print하고 반복문을 빠져나옴
for i in 0..<9 {
  for j in 0..<9 {
    if matrix[i][j] == maxNum {
      print(maxNum)
      print(i + 1, j + 1)
      break
    }
  }
}
