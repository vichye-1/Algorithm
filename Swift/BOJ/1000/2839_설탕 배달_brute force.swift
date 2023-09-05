let input = Int(readLine()!)!
var temp = input
var count = 0

while temp >= 3 {
  if temp % 5 == 0 {
    count += temp / 5
    temp = 0
  } else {
    temp -= 3
    count += 1
  }
}

if temp == 0 {
  print(count)
} else {
  print(-1)
}
