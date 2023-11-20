#    - **Description**: Data is partitioned based on geographic or physical location, ideal for distributed systems with data centers in multiple regions.
#    - **Use Case**: Ensures data is stored and accessed from nearby data centers to minimize latency.

class LocationBasedSharding:
    def __init__(self):
        # Initialize shard mapping
        self.shard_mapping = {}

    def assign_location(self, key, location):
        # Assign a key to a specific geographical location
        self.shard_mapping[key] = location

    def get_shard(self, key):
        # Retrieve the shard for a given key based on its associated location
        if key in self.shard_mapping:
            return self.shard_mapping[key]
        else:
            return "Default Shard"  # Use a default shard for keys without a specified location

    def add_data(self, key, data):
        # Determine the shard for the key based on location
        shard_location = self.get_shard(key)
        
        # Store the data in the corresponding shard (simulated here)
        print(f"Storing data in Shard at Location: {shard_location} - Data: {data}")

    def get_data(self, key):
        # Determine the shard for the key based on location
        shard_location = self.get_shard(key)
        
        # Retrieve the data from the corresponding shard (simulated here)
        print(f"Retrieving data from Shard at Location: {shard_location}")

# Example Usage
sharding = LocationBasedSharding()

# Assign keys to specific geographical locations
sharding.assign_location("Key1", "US")
sharding.assign_location("Key2", "Europe")
sharding.assign_location("Key3", "Asia")

# Add data using assigned keys
sharding.add_data("Key1", "Data for Key1")
sharding.add_data("Key2", "Data for Key2")
sharding.add_data("Key4", "Data for Key4")  # Key4 does not have a specified location

# Retrieve data using assigned keys
sharding.get_data("Key1")
sharding.get_data("Key2")
sharding.get_data("Key4")  # Use default shard for Key4
