while let input = readLine() {
  let inputNum = input.split{ $0 == " " }.map{ Int($0)! }
  if inputNum[0] == 0, inputNum[1] == 0 { break }
  
  if inputNum[0] % inputNum[1] == 0 { print("multiple") }
  else if inputNum[1] % inputNum[0] == 0 { print("factor") }
  else { print("neither") }
}
