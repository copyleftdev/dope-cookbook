#  - **Description**: Each shard is assigned a weight, and data distribution is proportional to the shard's weight.
#     - **Use Case**: Beneficial when some shards need more capacity or resources than others, ensuring load balancing.
import random

class WeightedSharding:
    def __init__(self):
        # Initialize shard mapping
        self.shard_mapping = {}

    def assign_weight(self, shard_id, weight):
        # Assign a weight to a specific shard
        self.shard_mapping[shard_id] = weight

    def get_shard(self, key):
        # Retrieve the shard for a given key based on weights
        total_weight = sum(self.shard_mapping.values())
        if total_weight == 0:
            return "No Shards Available"

        random_value = random.uniform(0, total_weight)
        cumulative_weight = 0

        for shard_id, weight in self.shard_mapping.items():
            cumulative_weight += weight
            if random_value <= cumulative_weight:
                return shard_id

    def add_data(self, key, data):
        # Determine the shard for the key based on weights
        shard_id = self.get_shard(key)
        
        # Store the data in the corresponding shard (simulated here)
        print(f"Storing data in Shard {shard_id} - Data: {data}")

# Example Usage
sharding = WeightedSharding()

# Assign weights to specific shards
sharding.assign_weight("Shard A", 2)
sharding.assign_weight("Shard B", 3)
sharding.assign_weight("Shard C", 1)

# Add data using assigned keys
data = ["Data 1", "Data 2", "Data 3", "Data 4", "Data 5"]

for key, value in enumerate(data):
    sharding.add_data(key, value)
