from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.vals = {} # key -> value
        self.counts = {} # key -> times used
        self.lists = defaultdict(lambda: set()) # times used -> set(key)
        self.lists[1] = set()
    
        self.cap = capacity
        self.min = -1
    
    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        
        count = self.counts[key]
        self.counts[key] += 1
        self.lists[count].remove(key)

        if(count == self.min and (not self.lists[count])):
            self.min += 1

        self.lists(count+1).add(key)
        return self.vals[key]


    def put(self, key: int, value: int) -> None:
        if(self.cap <= 0):
            return

        if key in self.vals:
            self.vals[key] = value
            self.get(key)
            return

        if len(self.vals) >= self.cap:
            self.lists(self.min)


# Your LFUCache object will be instantiated and called as such:
lfu = LFUCache(2)

lfu.put(1, 1) # cache=[1,_], cnt(1)=1
lfu.put(2, 2) # cache=[2,1], cnt(2)=1, cnt(1)=1
assert 1 == lfu.get(1)    # return 1

# cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3); # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
# cache=[3,1], cnt(3)=1, cnt(1)=2
assert -1 == lfu.get(2);    # return -1 (not found)
assert 3 == lfu.get(3)    # return 3

# cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4); # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
# cache=[4,3], cnt(4)=1, cnt(3)=2
assert -1 == lfu.get(1);    # return -1 (not found)
assert 3 == lfu.get(3);    # return 3

# cache=[3,4], cnt(4)=1, cnt(3)=3
assert 4 == lfu.get(4);    # return 4
# cache=[4,3], cnt(4)=2, cnt(3)=3