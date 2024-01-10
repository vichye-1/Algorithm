class Solution:
    def reverseWords(self, s: str) -> str:
        trimS = s.split(" ")
        answer = ""
        for i in reversed(range(len(trimS))):
            if trimS[i] != "":
                answer += trimS[i] + " "
        return answer[:-1]


#2번째 풀이 (24. 1. 10. 수, 5분)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(str, s.split()[::-1]))
