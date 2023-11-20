#  - **Description**: Data is tagged with labels, and shards are assigned one or more tags. Data is routed to shards based on matching tags.
#     - **Use Case**: Useful for scenarios where data needs to be categorized and distributed based on specific attributes or characteristics.
class TagBasedSharding:
    def __init__(self):
        # Initialize shard mapping
        self.shard_mapping = {}

    def assign_tags(self, key, tags):
        # Assign tags to a specific key
        self.shard_mapping[key] = tags

    def get_shard(self, key):
        # Retrieve the shard for a given key based on its associated tags
        if key in self.shard_mapping:
            return self.shard_mapping[key]
        else:
            return "Default Shard"  # Use a default shard for keys without tags

    def add_data(self, key, data):
        # Determine the shard for the key based on tags
        shard_tags = self.get_shard(key)
        
        # Store the data in the corresponding shard (simulated here)
        print(f"Storing data in Shard with Tags: {shard_tags} - Data: {data}")

    def get_data(self, key):
        # Determine the shard for the key based on tags
        shard_tags = self.get_shard(key)
        
        # Retrieve data from the appropriate shard (simulated here)
        print(f"Retrieving data from Shard with Tags: {shard_tags}")

# Example Usage
sharding = TagBasedSharding()

# Assign tags to specific keys
sharding.assign_tags("Key1", ["Tag1", "Tag2"])
sharding.assign_tags("Key2", ["Tag2", "Tag3"])
sharding.assign_tags("Key3", ["Tag1", "Tag3"])

# Add data using assigned keys
sharding.add_data("Key1", "Data for Key1")
sharding.add_data("Key2", "Data for Key2")
sharding.add_data("Key4", "Data for Key4")  # Key4 does not have tags

# Retrieve data using assigned keys
sharding.get_data("Key1")
sharding.get_data("Key2")
sharding.get_data("Key4")  # Use default shard for Key4
