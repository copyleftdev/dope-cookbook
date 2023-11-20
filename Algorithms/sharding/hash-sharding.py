#    - **Description**: Data is partitioned based on a hash function applied to a specific attribute (e.g., the primary key). The hash value determines the shard.
#    - **Use Case**: Commonly used for even distribution of data across shards in distributed databases, ensuring data access scalability.

class HashBasedSharding:
    def __init__(self, num_shards):
        self.num_shards = num_shards
        self.shards = [[] for _ in range(num_shards)]

    def hash_key(self, key):
        # Simple hash function to determine the shard based on the key
        return hash(key) % self.num_shards

    def add_data(self, key, data):
        shard_id = self.hash_key(key)
        self.shards[shard_id].append((key, data))

    def get_data(self, key):
        shard_id = self.hash_key(key)
        for k, data in self.shards[shard_id]:
            if k == key:
                return data
        return f"Data for key {key} not found in shard {shard_id}."

# Example Usage
num_shards = 4
sharding = HashBasedSharding(num_shards)

sharding.add_data(1, "Data for Key 1")
sharding.add_data(5, "Data for Key 5")
sharding.add_data(9, "Data for Key 9")

print(sharding.get_data(1))   # Returns: "Data for Key 1"
print(sharding.get_data(5))   # Returns: "Data for Key 5"
print(sharding.get_data(9))   # Returns: "Data for Key 9"
print(sharding.get_data(10))  # Returns: "Data for key 10 not found in shard 2."
