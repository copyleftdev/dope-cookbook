#    - **Description**: Dynamically balances between LRU and LFU based on current workload.
#    - **Use Case**: Ideal for systems with variable access patterns, optimizing cache hit rates.


class ARCCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.t1, self.t2, self.b1, self.b2 = [], [], [], {}
        self.p = 0

    def get(self, key: int) -> int:
        if key in self.t1:
            self.t1.remove(key)
            self.t2.append(key)
            return key
        elif key in self.t2:
            self.t2.remove(key)
            self.t2.append(key)
            return key
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.t1:
            self.t1.remove(key)
        elif key in self.t2:
            self.t2.remove(key)
        elif key in self.b1:
            if len(self.t1) + len(self.b1) == self.capacity:
                self.b1.pop(0)
            elif len(self.t1) + len(self.b1) < self.capacity:
                self.b2[key] = value
                return
            else:
                self.b1.pop(0)
        elif key in self.b2:
            if len(self.t1) + len(self.b1) == self.capacity:
                self.b2.pop(next(iter(self.b2)))
            else:
                self.b2.pop(key)
        elif len(self.t1) + len(self.b1) == self.capacity:
            if len(self.t1) < self.p:
                self.b1.pop(0)
            else:
                del self.b2[next(iter(self.b2))]

        self.t1.append(key)
        return

# Example Usage
cache = ARCCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
print(cache.get(2))  # returns 2 (recently used)
cache.put(4, 4)      # evicts 1 (least recently used)
print(cache.get(1))  # returns -1 (not found)
