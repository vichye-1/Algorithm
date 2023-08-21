let input = readLine()!.split{ $0 == " " }.map{ String($0) }
let strnum = input[0]
let num = input[1]

// Int일때는 바꾸려는 숫자(strnum 자리)가 Stirng 타입이어야한다.
print(Int(strnum, radix: Int(num)!)!)
