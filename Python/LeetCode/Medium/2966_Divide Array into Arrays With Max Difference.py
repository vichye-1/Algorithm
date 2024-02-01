# 1
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort() # 1 1 3 3 4 5 7 8 9
        answer = []
        target = 0
        while nums:
            temp = []
            for _ in range(3):
                temp.append(nums.pop())
            answer.append(temp)
        for lists in answer:
            if lists[0] - lists[-1] > k:
                return []
        return answer
      
# 2
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) // 3):
            answer.append(nums[i * 3 : (i + 1) * 3])
            if answer[-1][-1] - answer[-1][0] > k:
                return []
        return answer 
