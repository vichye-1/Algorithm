# 1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        # nums1 = [2, 2, 2, 3]
        # nums2 = [0, 1, 3, 0, 4, 0, 4, 2]
        return count

# 2. This answer accepted but did not meet the in-place condition.
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             i -= count
#             if nums[i] == val:
#                 nums.remove(nums[i])
#                 count += 1
#         return len(nums)
