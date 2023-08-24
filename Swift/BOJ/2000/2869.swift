// 올라가는 횟수가 x이면, 내려가는 횟수는 x-1이 될 것이다
// 식으로 적어보면, Ax - B(x - 1) = V
// 식을 풀면 x = (V - B) / (A - B) 가 된다
// 이때, 나머지가 생기면 낮에 한 번 더 올라야 한다는 뜻이므로, +1 을 해준다
// 나머지가 생기지 않으면 그냥 x = (V - B) / (A - B) 값을 산출한다

let input = readLine()!.split(separator: " ").map{ Int($0)! }
let day = input[0]
let night = input[1]
let tree = input[2]

let remain = (tree - night) % (day - night)
let goUp = (tree - night) / (day - night)

if remain > 0 {
  print(goUp + 1)
} else { print(goUp) }
