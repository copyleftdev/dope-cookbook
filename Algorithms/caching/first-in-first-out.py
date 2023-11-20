#    - **Description**: Evicts cache entries in the order they were added, without considering the frequency or recency of access.
#    - **Use Case**: Useful in environments with uniform access patterns where data age is a key factor for eviction.

from queue import Queue

class FIFOCache:
    def __init__(self, capacity: int):
        self.cache = set()
        self.order = Queue()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            return key
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.order.qsize() >= self.capacity:
                # Remove the oldest item from the cache
                oldest_key = self.order.get()
                self.cache.remove(oldest_key)
            self.cache.add(key)
            self.order.put(key)

# Example Usage
cache = FIFOCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)      # evicts key 1
print(cache.get(1))  # returns -1 (not found)
print(cache.get(2))  # returns 2
print(cache.get(3))  # returns 3
