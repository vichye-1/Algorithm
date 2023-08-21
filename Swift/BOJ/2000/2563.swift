// "0"으로 된 100 * 100 2차원 배열 만듦
var array = [[Character]](repeating: [Character](repeating: "0", count: 100), count: 100)

// 종이의 갯수 입력받음
let countPapers = Int(readLine()!)!

// x좌표, y좌표 입력받고, 색종이가 붙여지는 10 * 10 칸 만큼 "0"을 "1"로 바꿈
// 종이가 겹치는 부분이 있을 수 있기 때문
for _ in 1...countPapers {
  let input = readLine()!.split(separator: " ").map{ Int($0)! }
  let x = input[0]
  let y = input[1]
  for i in x...x + 9 {
    for j in y...y + 9 {
      array[i][j] = "1"
    }
  }
}

# 2차원 배열을 1차원 배열로 평탄화 하고, 값이 "1"인 값만 추출해 갯수를 구한다
print(array.flatMap{ $0 }.filter{ $0 == "1" }.count)
