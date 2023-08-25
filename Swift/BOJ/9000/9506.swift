while let input = Int(readLine()!) {
  if input == -1 { break }
  var array: [Int] = []
  for i in 1..<input {
    if input % i == 0 { array.append(i) }
  }
  let joinedArr = array.map{ String($0) }.joined(separator: " + ")
  if input == array.reduce(0, +) {
    print("\(input) = \(joinedArr)")
  } else {
    print("\(input) is NOT perfect.")
  }
}
