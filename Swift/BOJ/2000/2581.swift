// boolean 값을 최대로 주어질 수 있는 값만큼의 숫자로 만든다.
// 에라토스테네스의 체를 만드는 과정
var prime = [Bool](repeating: true, count: 10001)
prime[0] = false
prime[1] = false

// 2부터 10,000까지 돌며 각 숫자의 배수들은 false로 바꾸고, 본래의 값인 i는 true로 바꾼다
for i in 2...10000 {
  if prime[i] == true {
    var temp = i
    while temp <= 10000 {
      prime[temp] = false
      temp += i
    }
    prime[i] = true
  }
}

// 입력값을 받는다
let num1 = Int(readLine()!)!
let num2 = Int(readLine()!)!

// 소수를 담을 빈 배열을 만든다
// 입력값의 범위만큼 enumerated로 index와 value를 받고, value가 true이면 빈 배열에 index + num1한 값을 넣는다
// index는 입력값이 60부터 시작하더라도 index는 0부터 시작하기때문이다
var primeArray: [Int] = []
for (index, value) in prime[num1...num2].enumerated() {
  if value == true { 
    primeArray.append(index + num1)
  } 
}

// 소수가 존재하면 소수의 합과 소수의 최솟값을 프린트
// 존재하지 않으면 -1 출력
if primeArray.count > 0 {
  print(primeArray.reduce(0, +))
  print(primeArray[0])
} else { print(-1) }
