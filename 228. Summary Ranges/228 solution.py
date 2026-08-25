class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        result = []

        for right in range(len(nums)):
            if right == len(nums) - 1 or nums[right] + 1 != nums[right + 1]:
                app = f"{nums[right]}" if right == left else f"{nums[left]}->{nums[right]}"
                result.append(app)
                
                left = right + 1
        
        return result