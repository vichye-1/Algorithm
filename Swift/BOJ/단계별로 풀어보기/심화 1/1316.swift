var countInput = Int(readLine()!)!
var words = countInput

for _ in 1...countInput {
  let inputStr = readLine()!
  var arr: [Character] = []
  
  for str in inputStr {
    if !arr.contains(str) { 
      arr.append(str) 
    } else if arr.last != str { 
        arr.removeAll()
        break
      }
    }
    if arr.isEmpty { words -= 1 }
  }  
print(words)
