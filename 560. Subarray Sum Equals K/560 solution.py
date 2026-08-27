class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        count = 0
        sums = {0 : 1}

        for num in nums:
            sum_ += num
            diff = sum_ - k

            if diff in sums:
                count += sums[diff]
            
            if sum_ not in sums:
                sums[sum_] = 0
            
            sums[sum_] += 1
        
        return count


