let input = Int(readLine()!)!
var line = 0
var highest = 0

while input > highest {
  line += 1
  highest += line
}

var gap = highest - input
var up = 0
var down = 0

if line % 2 == 1 {
  up = gap  + 1
  down = line - gap
} else {
  up = line - gap
  down = gap + 1
}

print("\(up)/\(down)")
