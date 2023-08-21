var array = [[String]](repeating: [String](repeating: "", count: 15), count: 5)

for i in 0..<5 {
  let row = readLine()!.map{ String($0) }
  let rowIndex = row.count - 1
  array[i].replaceSubrange(0...rowIndex, with: row)
}

for i in 0..<15 {
  for j in 0..<5 {
    print(array[j][i], terminator: "")
  }
}
