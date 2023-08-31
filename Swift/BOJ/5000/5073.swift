while true {
  // sorted()로 정렬하여 input값 받기
  let input = readLine()!.split{ $0 == " " }.map{ Int($0)! }.sorted()

  // 값이 모두 0이면 break
  if input == [0, 0, 0] { break }

  // 가장 마지막 값(가장 큰 값)이 나머지 변의 길이의 합보다 크거나 같으면 삼각형의 조건을 만족하지 않음
  if input.last! >= input[0] + input[1] {
    print("Invalid")

  // set()을 사용해서 중복된 값 제거. 모두 같으면 1개, 2개가 같으면 2개, 3개가 다 다르면 3개가 된다
  } else {
    switch Set(input).count {
      case 1: print("Equilateral")
      case 2: print("Isosceles")
      case 3: print("Scalene")
      default: break
    }
  }
}
