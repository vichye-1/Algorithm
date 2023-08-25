// 1st submission
class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var answer: [String] = []
        for i in 1...n {
            if i % 3 == 0, i % 5 == 0 { answer.append("FizzBuzz") }
            else if i % 3 == 0 { answer.append("Fizz") }
            else if i % 5 == 0 { answer.append("Buzz") }
            else { answer.append("\(i)") }
        }
        return answer
    }
}

// 2nd submission
class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var answer: [String] = []
        for num in 1...n {
            switch (num % 3, num % 5) {
                case (0, 0): answer.append("FizzBuzz")
                case (0, _): answer.append("Fizz")
                case (_, 0): answer.append("Buzz")
                default: answer.append("\(num)")
            }
        }
        return answer
    }
}
