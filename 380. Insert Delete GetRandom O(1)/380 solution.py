import random

class RandomizedSet:


    def __init__(self):
        self.nums = []
        self.val_to_ind = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.val_to_ind:
            return False
        if self.size == len(self.nums):
            self.nums.append(val)
        else:
            self.nums[self.size] = val
        self.val_to_ind[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_ind:
            return False
        
        index = self.val_to_ind[val]
        self.nums[index], self.nums[self.size - 1] = self.nums[self.size - 1], self.nums[index]
        self.size -= 1
        self.val_to_ind[self.nums[index]] = index
        del self.val_to_ind[val]
        return True

    def getRandom(self) -> int:
        ind = random.randint(0, self.size - 1)
        return self.nums[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()