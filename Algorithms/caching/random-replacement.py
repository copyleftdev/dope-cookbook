#    - **Description**: Randomly selects cache entries for eviction.
#    - **Use Case**: Effective in smaller or simpler caching systems where managing the cache with minimal overhead is desired.
import random

class RRCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.keys = []

    def get(self, key: int) -> int:
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.keys) >= self.capacity:
            # Evict a random key
            evict_key = random.choice(self.keys)
            self.keys.remove(evict_key)
            del self.cache[evict_key]

        self.cache[key] = value
        if key not in self.keys:
            self.keys.append(key)

# Example Usage
cache = RRCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)      # randomly evicts either key 1 or 2
print(cache.get(2))  # returns -1 if key 2 was evicted, else returns 2
