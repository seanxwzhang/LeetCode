from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyval = {}
        self.dictlist = defaultdict(lambda : OrderedDict())
        self._size = 0
        self._largest_freq = 0
            
        
    def get(self, key: int) -> int:
        # print("getting {}".format(key))
        # print(self.dictlist)
        # print(self.keyval)
        if key in self.keyval:
            val, freq = self.keyval[key]
            del self.dictlist[freq][key]
            self.keyval[key] = (val, freq + 1)
            self.dictlist[freq + 1][key] = val
            self._largest_freq = max(self._largest_freq, freq + 1)
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # print("putting {}".format(key))
        # print(self.dictlist)
        # print(self.keyval)
        if self.capacity == 0:
            return
        if key in self.keyval:
            _, freq = self.keyval[key]
            self.keyval[key] = (value, freq + 1)
            del self.dictlist[freq][key]
            self.dictlist[freq + 1][key] = value
            self._largest_freq = max(self._largest_freq, freq + 1)
        else:
            if self._size == self.capacity:
                for i in range(1, self._largest_freq + 1):
                    if len(self.dictlist[i]):
                        removed_key, _ = self.dictlist[i].popitem(last=False)
                        break
                del self.keyval[removed_key]
                self._size -= 1
            self.dictlist[1][key] = value
            self.keyval[key] = (value, 1)
            self._size += 1
            self._largest_freq = max(self._largest_freq, 1)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)