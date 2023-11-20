#    - **Description**: Prioritizes the eviction of items accessed least frequently.
#    - **Use Case**: Best for situations with stable access patterns, where frequently accessed data should remain in cache.
class LFUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_map = {}
        self.freq_map = {}

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._update(node)
        else:
            if len(self.key_map) >= self.capacity:
                self._evict()
            node = LFUNode(key, value)
            self.key_map[key] = node
            if 1 not in self.freq_map:
                self.freq_map[1] = {}
            self.freq_map[1][key] = node
            self.min_freq = 1

    def _update(self, node):
        # Remove the node from its current frequency list
        del self.freq_map[node.freq][node.key]
        if not self.freq_map[node.freq]:
            if self.min_freq == node.freq:
                self.min_freq += 1
            del self.freq_map[node.freq]
        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = {}
        self.freq_map[node.freq][node.key] = node

    def _evict(self):
        # Evict the least frequently used item
        freq_list = self.freq_map[self.min_freq]
        key, _ = next(iter(freq_list.items()))
        del self.key_map[key]
        del freq_list[key]
        if not freq_list:
            del self.freq_map[self.min_freq]

# Example Usage
cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))   # returns 1
cache.put(3, 3)       # evicts key 2
print(cache.get(2))   # returns -1 (not found)
print(cache.get(3))   # returns 3
cache.put(4, 4)       # evicts key 1
print(cache.get(1))   # returns -1 (not found)
print(cache.get(3))   # returns 3
print(cache.get(4))   # returns 4
