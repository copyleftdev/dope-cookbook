#    - **Description**: Considers both the size and age of cache items, giving preference to smaller and older items.
#    - **Use Case**: Effective in limited-space environments where storing larger items is more costly.
class GDSCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = {}
        self.access_order = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update access time
            self.access_order[key] = max(self.access_order.values()) + 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int, size: int) -> None:
        # Check if the cache is full
        if len(self.cache) >= self.capacity:
            self._evict()
        
        self.cache[key] = value
        self.size[key] = size
        self.access_order[key] = max(self.access_order.values(), default=-1) + 1

    def _evict(self):
        max_size_key = max(self.size, key=self.size.get)
        oldest_access_key = min(self.access_order, key=self.access_order.get)

        if self.size[max_size_key] > self.size[oldest_access_key]:
            # Evict the item with the largest size
            self._remove(max_size_key)
        else:
            # Evict the item with the oldest access
            self._remove(oldest_access_key)

    def _remove(self, key):
        del self.cache[key]
        del self.size[key]
        del self.access_order[key]

# Example Usage
cache = GDSCache(3)
cache.put(1, 1, 3)  # Set size to 3
cache.put(2, 2, 2)  # Set size to 2
cache.put(3, 3, 4)  # Set size to 4
print(cache.get(1))  # returns 1
cache.put(4, 4, 5)  # Evicts key 2 (smallest size)
print(cache.get(2))  # returns -1 (not found)
