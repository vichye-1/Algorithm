let input = readLine()!

// -1 이 26개인 리스트 만듦(알파벳 개수)
var array = [Int](repeating: -1, count: 26)

// 'enumerated()'로 char의 인덱스와 알파벳 추출
for (idx, char) in input.enumerated() {
  let index = Int(char.asciiValue!) - Int(Character("a").asciiValue!)
  // 만약 'array[index]'의 값이 -1이면 위에서 구한 enumerated()의 인덱스 값을 넣는다
  if array[index] == -1 {
    array[index] = idx
  }
}

// 답 추출
array.forEach{ print($0, terminator: " ") }
