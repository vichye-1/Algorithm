class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif stack and i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif stack and i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif stack and i == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True 
