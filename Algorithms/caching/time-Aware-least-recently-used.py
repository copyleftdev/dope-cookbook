#    - **Description**: An LRU variant where each item in the cache has a time-to-live (TTL).
#    - **Use Case**: Suitable for caching time-sensitive data, like web sessions or TTL-based data.
import time

class TLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.access_order = {}
        self.ttl = {}

    def get(self, key: int) -> int:
        current_time = time.time()
        if key in self.cache:
            if current_time < self.ttl[key]:
                # Update access time
                self.access_order[key] = current_time
                return self.cache[key]
            else:
                # TTL has expired, remove the key
                self._remove(key)
        return -1

    def put(self, key: int, value: int, ttl_seconds: int) -> None:
        current_time = time.time()
        # Check if the cache is full
        if len(self.cache) >= self.capacity:
            self._evict(current_time)
        
        # Set TTL for the key
        self.ttl[key] = current_time + ttl_seconds
        self.access_order[key] = current_time
        self.cache[key] = value

    def _evict(self, current_time):
        # Evict the least recently used item
        min_key = min(self.access_order, key=self.access_order.get)
        if current_time >= self.ttl[min_key]:
            self._remove(min_key)
        else:
            raise Exception("TTL has not expired for the least recently used item.")

    def _remove(self, key):
        del self.cache[key]
        del self.access_order[key]
        del self.ttl[key]

# Example Usage
cache = TLRUCache(2)
cache.put(1, 1, 3)  # Set TTL to 3 seconds
cache.put(2, 2, 5)  # Set TTL to 5 seconds
print(cache.get(1))  # returns 1 (within TTL)
time.sleep(4)
print(cache.get(1))  # returns -1 (TTL has expired)
