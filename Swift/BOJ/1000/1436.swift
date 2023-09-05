let input = Int(readLine()!)!
var title = 665
var count = 0

while true {
  title += 1
  var six = 0
  for c in String(title) {
    if c == "6"{
     six += 1 
    } else {
      six = 0
    }
    if six == 3 {
      count += 1
    }
  }

  if count == input {
    print(title)
    break
  }
}
