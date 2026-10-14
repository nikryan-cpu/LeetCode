class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        left = 0
        letters_p = [0] * 26
        letters_s = [0] * 26
        diff = 0
        all_ind = []

        for ch in p:
            pos = ord(ch) - ord('a')
            letters_p[pos] += 1
        
        for ch in s[:len(p)]:
            pos = ord(ch) - ord('a')
            letters_s[pos] += 1
        
        for i in range(len(p)):
            if letters_p[i] != letters_s[i]:
                diff += 1

        if diff == 0:
            all_ind.append(left)

        for right in range(len(p) - 1, len(s) - 1):
            
            #left
            left_pos = ord(s[left]) - ord('a')

            if letters_s[left_pos] == letters_p[left_pos]:
                diff += 1
            elif letters_s[left_pos] == letters_p[left_pos] + 1:
                diff -= 1
            letters_s[left_pos] -= 1
            left += 1

            #right
            right_pos = ord(s[right + 1]) - ord('a')

            if letters_s[right_pos] == letters_p[right_pos]:
                diff += 1
            elif letters_s[right_pos] == letters_p[right_pos] - 1:
                diff -= 1
            letters_s[right_pos] += 1
            if diff == 0:
                all_ind.append(left)
        
        return all_ind

# bp|aa| - [2, 0]
# aa - [2, 0]
# diff = 0

solution = Solution()
nums = solution.findAnagrams("bpaa", "aa")
print(nums)