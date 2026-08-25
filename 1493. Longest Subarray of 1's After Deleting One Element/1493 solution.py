class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        count_0 = 0
        
        for right in range(len(nums)):

            if nums[right] == 0:
                count_0 += 1
            if count_0 >= 2:
                if nums[left] == 0:
                    count_0 -= 1
                left += 1
        
        return right - left


