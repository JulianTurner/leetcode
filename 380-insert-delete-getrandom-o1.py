from random import choice

class RandomizedSet:

    def __init__(self):
        self.value_list = []
        self.value_dict = {}
        

    def insert(self, val: int) -> bool:
        if val in self.value_dict:
            return False
        
        self.value_list.append(val)
        self.value_dict[val] = len(self.value_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_dict:
            return False
        
        self.value_list[self.value_dict[val]] = self.value_list[len(self.value_list) - 1]
        self.value_dict[self.value_list.pop()] = self.value_dict[val] 
        del self.value_dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.value_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

randomizedSet = RandomizedSet()
print(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2)) # Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom()) #  getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1)) # Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2))  # 2 was already in the set, so return false.
print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.