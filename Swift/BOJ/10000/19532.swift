let num = readLine()!.split{ $0 == " " }.map{ Int($0)! }
let range = [Int](-999...999)

let a = num[0], b = num[1], c = num[2], d = num[3], e = num[4], f = num[5]

for x in range {
  for y in range {
    if (a * x + b * y) == c && (d * x + e * y == f) {
      print("\(x) \(y)")
      break
    }
  }
}
