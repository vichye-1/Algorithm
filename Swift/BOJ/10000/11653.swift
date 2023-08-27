var inputNum = Int(readLine()!)!

var divisor = 2

while true {
  if inputNum % divisor == 0 {
    print(divisor)
    inputNum = inputNum / divisor
  } else {
  divisor += 1
  if inputNum == 1 { break }
  }
} 
