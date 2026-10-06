class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = list()

        intervals = sorted(intervals)
        curr = intervals[0].copy()

        for i in range(1, len(intervals)):
            if intervals[i][0] <= curr[1]:
                curr[1] = max(curr[1], intervals[i][1])
            
            else:
                merged.append(curr)
                curr = intervals[i].copy()
        
        merged.append(curr)
        
        return merged
        
        