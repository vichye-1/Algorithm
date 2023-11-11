def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    list1, list2 = [], []
    
    for i in range(len(str1) - 1):
        if str1[i : i + 2].isalpha():
            list1.append(str1[i: i + 2])
        
    for j in range(len(str2) - 1):
        if str2[j : j + 2].isalpha():
            list2.append(str2[j : j + 2])
            
    set1, set2 = set(list1), set(list2)
    unions, intersections = set1 | set2, set1 & set2
    
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    
    union_len = 0
    for union in unions:
        union_len += max(list1.count(union), list2.count(union))
        
    intersection_len = 0
    for intersection in intersections:
        intersection_len += min(list1.count(intersection), list2.count(intersection))
        
    return int((intersection_len / union_len) * 65536)
