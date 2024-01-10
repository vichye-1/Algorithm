class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        palindrome = ""
        for c in s:
            if c.isalnum():
                palindrome += c

        if palindrome == palindrome[::-1]:
            return True
        else:
            return False

# 2번째 풀이(24. 1. 10. 수)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in s:
            if c.isalnum():
                result += c
        result = result.lower()
        return result == result[::-1]
