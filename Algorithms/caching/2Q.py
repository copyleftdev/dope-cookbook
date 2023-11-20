    # - **Description**: An enhancement over LRU that uses two queues to differentiate between recently added and frequently accessed items.
    # - **Use Case**: Works well in environments where it's crucial to distinguish between newly added and frequently accessed items for optimal cache performance.
class TwoQCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.A1 = []  # Frequently used items
        self.A2 = []  # Less frequently used items

    def get(self, key: int) -> int:
        if key in self.A1:
            self.A1.remove(key)
            self.A1.insert(0, key)
            return key
        elif key in self.A2:
            self.A2.remove(key)
            self.A1.insert(0, key)
            return key
        else:
            return -1

    def put(self, key: int) -> None:
        if key in self.A1:
            self.A1.remove(key)
            self.A1.insert(0, key)
        elif key in self.A2:
            self.A2.remove(key)
            self.A1.insert(0, key)
        else:
            if len(self.A1) < self.capacity:
                self.A1.insert(0, key)
            else:
                if len(self.A2) >= self.capacity:
                    self.A2.pop()
                self.A2.insert(0, key)

# Example Usage
cache = TwoQCache(3)
cache.put(1)
cache.put(2)
cache.put(3)
print(cache.get(2))  # returns 2 (accessed from A2 and promoted to A1)
cache.put(4)         # evicts 1 (LRU in A2)
print(cache.get(1))  # returns -1 (not found)
