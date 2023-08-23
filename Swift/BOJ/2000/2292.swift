let input = Int(readLine()!)!
var honeycomb = 1
var count = 1

while input > honeycomb {
  honeycomb += 6 * count
  count += 1
}
print(count)
