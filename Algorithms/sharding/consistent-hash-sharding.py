#    - **Description**: Data is partitioned based on a hash function applied to a specific attribute (e.g., the primary key). The hash value determines the shard.
#    - **Use Case**: Commonly used for even distribution of data across shards in distributed databases, ensuring data access scalability.

import hashlib

class ConsistentHashingSharding:
    def __init__(self, num_replicas=3):
        self.num_replicas = num_replicas  # Number of virtual replicas for each shard
        self.ring = {}  # Hash ring mapping hashed keys to shards

    def hash_key(self, key):
        # Simulated hash function (you can use a more robust one in practice)
        return int(hashlib.md5(str(key).encode()).hexdigest(), 16)

    def add_shard(self, shard_id):
        # Add a shard to the hash ring with multiple virtual replicas
        for i in range(self.num_replicas):
            virtual_key = f"{shard_id}_replica_{i}"
            hashed_key = self.hash_key(virtual_key)
            self.ring[hashed_key] = shard_id

    def remove_shard(self, shard_id):
        # Remove a shard from the hash ring and its virtual replicas
        for i in range(self.num_replicas):
            virtual_key = f"{shard_id}_replica_{i}"
            hashed_key = self.hash_key(virtual_key)
            del self.ring[hashed_key]

    def get_shard(self, key):
        # Find the appropriate shard for a given key
        if not self.ring:
            return None

        hashed_key = self.hash_key(key)
        sorted_keys = sorted(self.ring.keys())

        for ring_key in sorted_keys:
            if hashed_key <= ring_key:
                return self.ring[ring_key]

        # If the key is greater than all ring keys, use the first shard
        return self.ring[sorted_keys[0]]

# Example Usage
sharding = ConsistentHashingSharding()

# Add shards to the hash ring
sharding.add_shard("Shard A")
sharding.add_shard("Shard B")
sharding.add_shard("Shard C")

# Assign data to shards based on consistent hashing
data = {
    "Key1": "Data for Key1",
    "Key2": "Data for Key2",
    "Key3": "Data for Key3"
}

for key, value in data.items():
    shard_id = sharding.get_shard(key)
    print(f"Storing data in {shard_id}: {value}")
