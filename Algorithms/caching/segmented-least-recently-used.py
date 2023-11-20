#    - **Description**: Combines two LRU lists, one for recently accessed items and another for frequently accessed items.
#    - **Use Case**: Useful for differentiating between frequently and recently accessed data, especially in mixed workload environments.
from collections import OrderedDict

class SLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent_cache = OrderedDict()  # LRU for recently accessed items
        self.freq_cache = OrderedDict()    # LRU for frequently accessed items

    def get(self, key: int) -> int:
        if key in self.freq_cache:
            # Move the key to the end of freq_cache (recently accessed)
            self.freq_cache.move_to_end(key)
            return self.freq_cache[key]
        elif key in self.recent_cache:
            # Move the key from recent_cache to freq_cache
            self.recent_cache.move_to_end(key)
            self.freq_cache[key] = self.recent_cache.pop(key)
            return self.freq_cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.freq_cache:
            # Update the value and move the key to the end of freq_cache
            self.freq_cache[key] = value
            self.freq_cache.move_to_end(key)
        else:
            # Add the key-value pair to freq_cache or recent_cache based on capacity
            if len(self.freq_cache) >= self.capacity:
                # Evict the least recently used item from freq_cache
                removed_key, _ = self.freq_cache.popitem(last=False)
                self.recent_cache[removed_key] = value
            else:
                self.freq_cache[key] = value

# Example Usage
cache = SLRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
print(cache.get(1))  # returns 1 (recently accessed)
cache.put(4, 4)      # evicts 2 (least recently used in freq_cache)
print(cache.get(2))  # returns -1 (not found)
