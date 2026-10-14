class Solution:
    def trap(self, height: list[int]) -> int:
        left = 1
        right = len(height) - 2
        left_max = height[0]
        right_max = height[-1]
        total_water = 0
        while left <= right:
            if left_max < right_max:
                total_water += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                total_water += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1

        return total_water
