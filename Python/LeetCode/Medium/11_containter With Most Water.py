class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        contain = 0
        while left < right:
            if height[left] < height[right]:
                contain = max(contain, (right - left) * height[left])
                left += 1
            else:
                contain = max(contain, (right - left) * height[right])
                right -= 1
        return contain
