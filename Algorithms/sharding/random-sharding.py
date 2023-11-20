#    - **Description**: Data is assigned to shards randomly.
#    - **Use Case**: Simplicity and unpredictability make it useful in scenarios where strict data access patterns are not a concern.
import random

class RandomSharding:
    def __init__(self, num_shards):
        self.num_shards = num_shards

    def add_data(self, data):
        # Determine a random shard to which data should be added
        shard_id = random.randint(0, self.num_shards - 1)

        # Simulated storage in the corresponding shard (you can replace this with actual storage)
        print(f"Storing data in Random Shard {shard_id}: {data}")

# Example Usage
num_shards = 3
sharding = RandomSharding(num_shards)

data = ["Data 1", "Data 2", "Data 3", "Data 4", "Data 5"]

# Add data to random shards
for item in data:
    sharding.add_data(item)
