#    - **Description**: Data is assigned to shards randomly.
#    - **Use Case**: Simplicity and unpredictability make it useful in scenarios where strict data access patterns are not a concern.

class ModuloSharding:
    def __init__(self, num_shards):
        self.num_shards = num_shards
        self.shards = [[] for _ in range(num_shards)]

    def shard_for_key(self, key):
        # Calculate the shard index using modulo operation
        shard_index = hash(key) % self.num_shards
        return shard_index

    def add_data(self, key, data):
        # Determine the shard for the key
        shard_index = self.shard_for_key(key)
        
        # Store the data in the corresponding shard (simulated here)
        self.shards[shard_index].append((key, data))

    def get_data(self, key):
        # Determine the shard for the key
        shard_index = self.shard_for_key(key)
        
        # Retrieve the data from the corresponding shard (simulated here)
        for k, data in self.shards[shard_index]:
            if k == key:
                return data
        
        # Key not found in the shard
        return f"Data for key {key} not found in shard {shard_index}."

# Example Usage
num_shards = 4
sharding = ModuloSharding(num_shards)

sharding.add_data(1, "Data for Key 1")
sharding.add_data(5, "Data for Key 5")
sharding.add_data(9, "Data for Key 9")

print(sharding.get_data(1))   # Returns: "Data for Key 1"
print(sharding.get_data(5))   # Returns: "Data for Key 5"
print(sharding.get_data(9))   # Returns: "Data for Key 9"
print(sharding.get_data(10))  # Returns: "Data for key 10 not found in shard 2."
