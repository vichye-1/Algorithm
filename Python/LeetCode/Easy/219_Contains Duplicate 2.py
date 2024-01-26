class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1. use defaultdict
        dic = defaultdict(list)  # {1: [0, 3], 2: [1], 3: [2]}
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        
        for val in dic.values():  # dic.values() = [[0, 3], [1], [2]]
            if len(val) > 1:
                for i in range(1, len(val)):
                    if abs(val[i] - val[i - 1]) <= k:
                        return True
        return False

       # 2. use dictionary & enumerate
        dic = {}  # {1: 3, 2: 4, 3: 5}
        for idx, num in enumerate(nums):
            if num in dic and abs(idx - dic[num]) <= k:
                return True
            else:
                dic[num] = idx
        return False
