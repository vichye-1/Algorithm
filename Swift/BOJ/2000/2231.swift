let input = Int(readLine()!)!
var sum = 0
var answer = 0

// 원래는 1부터 input값까지의 숫자를 모두 계산했다
// 하지만 그렇게 하면 시간이 너무 오래걸리기때문에, 
// 각 자리의 숫자가 9일때, 즉 '각 자리 * 9' 인 값을 최소 시작 지점으로 두었다. 
for i in input - String(input).count * 9...input where i >= 0{
  sum = i
  for j in String(i) {
    sum += Int(String(j))!
  }
  if sum == input {
    answer = i
    break
  } 
}

print(answer)
