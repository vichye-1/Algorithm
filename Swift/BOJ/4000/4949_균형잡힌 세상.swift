while true {
  let input = readLine()!

  if input == "." { break }

  var stack: [Character] = []

  for c in input {
    if c == "(" || c == "[" {
      stack.append(c)
    } else if c == ")" {
      if stack.last == "(" {
        stack.popLast()
      } else {
        stack.append(c)
        break
      }
    } else if c == "]" {
      if stack.last == "[" {
        stack.popLast()
      } else {
        stack.append(c)
        break
      }
    }
  }
  print(stack.count == 0 ? "yes" : "no")
}
