#    - **Description**: A centralized directory service maintains data-to-shard mappings. Clients query the directory to locate data.
#    - **Use Case**: Helpful in scenarios where data access patterns change frequently, as it provides flexibility in shard mappings.
class DirectoryBasedSharding:
    def __init__(self):
        # Initialize the directory as an empty dictionary
        self.directory = {}

    def assign_shard(self, key, shard_id):
        # Assign a key to a specific shard
        self.directory[key] = shard_id

    def get_shard(self, key):
        # Retrieve the shard for a given key from the directory
        if key in self.directory:
            return self.directory[key]
        else:
            return -1  # Key not found in any shard

    def add_data(self, key, data):
        # Determine the shard for the key
        shard_id = self.get_shard(key)

        if shard_id != -1:
            # Store the data in the corresponding shard (simulated here)
            print(f"Storing data in Shard {shard_id}: {data}")
        else:
            # Handle cases where the key does not belong to any shard
            print(f"Key {key} does not belong to any shard.")

# Example Usage
sharding = DirectoryBasedSharding()

# Assign keys to specific shards
sharding.assign_shard("Key1", "Shard A")
sharding.assign_shard("Key2", "Shard B")
sharding.assign_shard("Key3", "Shard C")

# Add data using assigned keys
sharding.add_data("Key1", "Data for Key1")
sharding.add_data("Key2", "Data for Key2")
sharding.add_data("Key4", "Data for Key4")  # Key4 does not belong to any shard

# Retrieve data using assigned keys
print(f"Retrieving data for Key1 from {sharding.get_shard('Key1')}")
print(f"Retrieving data for Key2 from {sharding.get_shard('Key2')}")
print(f"Retrieving data for Key4 from {sharding.get_shard('Key4')}")
