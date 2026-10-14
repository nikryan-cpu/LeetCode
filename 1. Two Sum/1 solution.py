class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_nums = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev_nums:
                return [i, prev_nums[diff]]
            
            prev_nums[nums[i]] = i