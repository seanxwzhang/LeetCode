from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_val = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.key_val:
            val = self.key_val[key]
            del self.key_val[key]
            self.key_val[key] = val
            return self.key_val[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.key_val:
            if len(self.key_val) == self.capacity:
                self.key_val.popitem(last=False)
        else:
            del self.key_val[key]
        self.key_val[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)