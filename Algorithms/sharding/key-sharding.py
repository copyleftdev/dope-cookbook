#   - **Description**: Data is partitioned based on explicitly specified keys, allowing for more control over data placement.
#    - **Use Case**: Useful when specific data items need to be assigned to particular shards for regulatory or compliance reasons.
class KeyBasedSharding:
    def __init__(self):
        # Initialize shard mapping
        self.shard_mapping = {}

    def assign_shard(self, key, shard_id):
        # Assign a key to a specific shard
        self.shard_mapping[key] = shard_id

    def get_shard(self, key):
        # Retrieve the shard for a given key
        if key in self.shard_mapping:
            return self.shard_mapping[key]
        else:
            return -1  # Key not found in any shard

    def add_data(self, key, data):
        # Determine the shard for the key
        shard_id = self.get_shard(key)

        if shard_id != -1:
            # Store the data in the corresponding shard (simulated here)
            if shard_id not in self.shard_mapping:
                self.shard_mapping[shard_id] = {}
            self.shard_mapping[shard_id][key] = data
        else:
            # Handle cases where the key does not belong to any shard
            print(f"Key {key} does not belong to any shard.")

    def get_data(self, key):
        # Determine the shard for the key
        shard_id = self.get_shard(key)

        if shard_id != -1:
            # Retrieve the data from the corresponding shard (simulated here)
            if shard_id in self.shard_mapping and key in self.shard_mapping[shard_id]:
                return self.shard_mapping[shard_id][key]
            else:
                return f"Data for key {key} not found in shard {shard_id}."
        else:
            # Handle cases where the key does not belong to any shard
            return f"Key {key} does not belong to any shard."

# Example Usage
sharding = KeyBasedSharding()

# Assign keys to specific shards
sharding.assign_shard(1, "Shard A")
sharding.assign_shard(2, "Shard B")
sharding.assign_shard(3, "Shard C")

# Add data using assigned keys
sharding.add_data(1, "Data for Key 1")

sharding.add_data(2, "Data for Key 2")
sharding.add_data(4, "Data for Key 4")  # Key 4 does not belong to any shard

# Retrieve data using assigned keys
print(sharding.get_data(1))   # Returns: "Data for Key 1"
print(sharding.get_data(2))   # Returns: "Data for Key 2"
print(sharding.get_data(4))   # Returns: "Key 4 does not belong to any shard."
print(sharding.get_data(5))   # Returns: "Data for key 5 not found in shard -1."
