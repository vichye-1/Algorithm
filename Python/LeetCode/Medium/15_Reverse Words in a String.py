class Solution:
    def reverseWords(self, s: str) -> str:
        trimS = s.split(" ")
        answer = ""
        for i in reversed(range(len(trimS))):
            if trimS[i] != "":
                answer += trimS[i] + " "
        return answer[:-1]

# follow up 만족 못 시킴(공간 복잡도 O(1) 만족 못 함)
