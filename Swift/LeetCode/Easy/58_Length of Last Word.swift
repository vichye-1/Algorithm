class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        return s.split{ $0 == " " }.last!.count
    }
}
