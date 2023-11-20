#    - **Description**: Data is distributed cyclically to shards in a round-robin fashion.
#    - **Use Case**: Suitable for scenarios with a relatively uniform data access pattern and when simplicity in shard allocation is desired.
class RoundRobinSharding:
    def __init__(self, num_shards):
        self.num_shards = num_shards
        self.current_shard = 0  # Initialize the current shard pointer

    def add_data(self, data):
        # Determine the shard to which data should be added
        shard_id = self.current_shard
        self.current_shard = (self.current_shard + 1) % self.num_shards  # Move to the next shard

        # Simulated storage in the corresponding shard (you can replace this with actual storage)
        print(f"Storing data in Shard {shard_id}: {data}")

# Example Usage
num_shards = 3
sharding = RoundRobinSharding(num_shards)

data = ["Data 1", "Data 2", "Data 3", "Data 4", "Data 5"]

# Add data to shards in a round-robin fashion
for item in data:
    sharding.add_data(item)
