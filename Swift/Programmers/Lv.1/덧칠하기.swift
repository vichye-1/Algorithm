import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {
    guard !section.isEmpty else { return 0 }
    var answer = 0
    var paint = 0
    for num in section {
        if paint <= num {
            paint = num + m
            answer += 1
        }
    }
    return answer
}
