#    - **Description**: Prioritizes removing the most recently accessed items.
#    - **Use Case**: Suitable for scenarios where the most recent data quickly becomes irrelevant, like in certain data analysis processes.

from collections import OrderedDict

class MRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the key to the end to show that it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move the key to the end to show that it was recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        # If the cache exceeds the capacity, remove the last item (most recently used)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=True)  # last=True pops the last item

# Example Usage
cache = MRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)           # evicts key 1 (most recently used)
print(cache.get(1))       # returns -1 (not found)
cache.put(4, 4)           # evicts key 3 (most recently used)
print(cache.get(3))       # returns -1 (not found)
print(cache.get(4))       # returns 4
