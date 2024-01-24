class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        p_list, s_list = [], []

        for c in pattern:
            p_list.append(pattern.index(c))
        
        for word in s:
            s_list.append(s.index(word))
        
        return p_list == s_list
