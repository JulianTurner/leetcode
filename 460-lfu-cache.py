from collections import defaultdict

class LFUCache:
    class ValueContainer:
        def __init__(self, value) -> None:
            self.prev = None # ValueContainer
            self.next = None # ValueContainer
            self.value = value
            self.use_count = 1

    def __init__(self, capacity: int):
        self.main_dict = {} # key -> ValueContainer
        self.count_dict = {} # count -> (headContainer, tailContainer)
        self.capacity = capacity
        self.smallest_container = -1

    def update_prev_next_references(self, container: ValueContainer):
        # update references prev and next
        if container.prev and container.next:
            container.prev.next = container.next
            container.next.prev = container.prev
        elif container.prev:
            container.prev.next = None
        elif container.next:
            container.next.prev = None

        container.prev = None
        container.next = None

    def insert_in_higher_container(self, container: ValueContainer):
        container.use_count += 1
        if container.use_countcount in self.count_dict:
            current_head, current_tail = self.count_dict[container.use_count]
            current_head.prev = container
            container.next = current_head
            self.count_dict[container.use_count] = (container, current_tail)


    def use_existing_key(self, key):
        # update count_dict
        current_container = self.main_dict[key]
        current_bucket = self.count_dict[current_container.use_count]
        if current_bucket[0] is current_container:
            if current_container.next:
                self.count_dict[current_container.use_count] = (current_container.next, current_bucket[1])

        if current_bucket[1] is current_container:
            if current_container.prev:
                self.count_dict[current_container.use_count] = (current_bucket[0], current_container.prev)

        if current_bucket[0] is current_container and current_bucket[1] is current_container:
            del self.count_dict[current_container.use_count]
            if self.smallest_container == current_container.use_count:
                self.smallest_container += 

        # update the references 
        self.update_prev_next_references(current_container)
            
        # insert in higher count_dict container
        self.insert_in_higher_container(current_container)


    
    def get(self, key: int) -> int:
        if key in self.main_dict:
            self.use_existing_key(key)
            return self.main_dict[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if (key not in self.main_dict) and (len(self.main_dict) == self.capacity):

            pass


        if key not in self.main_dict:
            new_container = self.ValueContainer(value)
            self.main_dict[key] = new_container

            if 1 in self.count_dict:
                self.count_dict[1].prev = new_container
                self.count_dict[1] = (new_container, self.count_dict[1][1])
            else:
                self.count_dict[1] = (new_container, new_container)
        else:
            # insert in higher use_count
            self.use_existing_key(key)


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