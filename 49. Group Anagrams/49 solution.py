class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_list = {}


        for string in strs:
            counter = [0] * 26
            for char in string:
                counter[ord(char) - ord('a')] += 1
            
            key = tuple(counter)
            if key not in counter_to_list:
                counter_to_list[key] = []
            
            counter_to_list[key].append(string)
        
        return list(counter_to_list.values())
