# second solution - much simple & faster than first solution : use list
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_list, t_list = [], []

        for i in s:
            s_list.append(s.index(i))
        for j in t:
            t_list.append(t.index(j))

        return s_list == t_list

# first solution : use defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict, t_dict = defaultdict(list), defaultdict(list)

        def dic(word, dictionary):
            for i in range(len(word)):
                dictionary[word[i]].append(i)
            return dictionary
        dic(s, s_dict)
        dic(t, t_dict)
 
        return list(s_dict.values()) == list(t_dict.values())

        # s_dict = {'p': [0, 2], 'a': [1], 'e': [3], 'r': [4]}
        # t_dict = {'t': [0, 2], 'i': [1], 'l': [3], 'e': [4]}
        
        ##### values #####
        # s_dict.values = [[0, 2], [1], [3], [4]] 
        # t_dict.values = [[0, 2], [1], [3], [4]] 
