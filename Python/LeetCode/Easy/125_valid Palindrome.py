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
        
