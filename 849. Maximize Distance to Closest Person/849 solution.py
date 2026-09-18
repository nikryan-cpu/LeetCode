class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        left = -1
        best = 1
        for right in range(len(seats)):
            if seats[right] == 1:
                if left == -1:
                    best = max(best, right)
                
                else:
                    best = max(best, (right-left) // 2)

                left = right
        
        if left < right:
            best = max(best, right - left)

        return best