class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            i -= count
            if nums[i] == val:
                nums.remove(nums[i])
                count += 1
        return len(nums)
