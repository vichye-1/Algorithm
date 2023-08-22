let count = Int(readLine()!)!

for _ in 1...count {
  var money = Int(readLine()!)!
  
  let quarter = money / 25
  money %= 25
  
  let dime = money / 10
  money %= 10
  
  let nickel = money / 5
  money %= 5
  
  let penny = money / 1

  print(quarter, dime, nickel, penny)
}
