import Foundation

func solution(_ food:[Int]) -> String {
    var answer = ""
    for i in 1...food.count - 1 {
        answer += String(repeating: String(i), count: food[i] / 2)
    }
    return answer + "0" + answer.reversed()
}
