var angle: [Int] = []

for _ in 1...3 {
  angle.append(Int(readLine()!)!)
}

let sum = angle.reduce(0, +)

if sum != 180 {
  print("Error")
} else {
  if angle.filter{ $0 == 60 }.count == 3 {
    print("Equilateral")
  } else if (angle[0] == angle[1] || angle[1] == angle[2] || angle[0] == angle[2]) {
    print("Isosceles")
  } else {
    print("Scalene")
  }
}
