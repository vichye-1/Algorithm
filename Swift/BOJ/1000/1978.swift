// 1001개의 boolean 배열을 만든다(인덱스를 편하게 사용하기위해 0, 1001 사용)
var prime = [Bool](repeating: true, count: 1001)
prime[0] = false
prime[1] = false

// 반복문을 사용하여 '배수'에 해당하는 값들을 false로 바꾼다
// 마지막에 소수에 해당하는 값들은 true로 다시 변경한다
for i in 1...1000 {
  if prime[i] == true {
    var divisor = i
    while divisor <= 1000 {
      prime[divisor] = false
      divisor += i
    }
    prime[i] = true
  }
}

// 입력값을 받고, 만약 위 배열의 값이 true면 answer에 +1을 해준다
// answer를 출력한다
_ = readLine()
let array = readLine()!.split(separator: " ").map{ Int($0)! }
var answer = 0
for num in array {
  if prime[num] == true { answer += 1 }
}
print(answer)
