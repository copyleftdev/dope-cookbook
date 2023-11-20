#   - **Description**: Combines multiple partitioning methods (e.g., range-based and hash-based) to achieve specific data distribution goals.
#     - **Use Case**: Offers flexibility to address diverse data access patterns within a single application.
import random
class HybridSharding:
    def __init__(self):
        # Initialize shard mapping for different sharding techniques
        self.shard_mapping = {
            "range_sharding": {},
            "tag_sharding": {},
            "weighted_sharding": {}
        }

    # Assign ranges for range-based sharding
    def assign_range(self, shard_id, start_range, end_range):
        self.shard_mapping["range_sharding"][shard_id] = (start_range, end_range)

    # Assign tags for tag-based sharding
    def assign_tags(self, shard_id, tags):
        self.shard_mapping["tag_sharding"][shard_id] = tags

    # Assign weights for weighted sharding
    def assign_weight(self, shard_id, weight):
        self.shard_mapping["weighted_sharding"][shard_id] = weight

    def get_shard(self, key, shard_type):
        # Retrieve the shard for a given key based on the specified sharding technique
        if shard_type not in self.shard_mapping:
            return "Invalid Shard Type"

        if shard_type == "range_sharding":
            for shard_id, (start_range, end_range) in self.shard_mapping[shard_type].items():
                if start_range <= key <= end_range:
                    return shard_id
        elif shard_type == "tag_sharding":
            for shard_id, tags in self.shard_mapping[shard_type].items():
                if key in tags:
                    return shard_id
        elif shard_type == "weighted_sharding":
            total_weight = sum(self.shard_mapping[shard_type].values())
            if total_weight == 0:
                return "No Shards Available"

            random_value = random.uniform(0, total_weight)
            cumulative_weight = 0

            for shard_id, weight in self.shard_mapping[shard_type].items():
                cumulative_weight += weight
                if random_value <= cumulative_weight:
                    return shard_id

        return "Default Shard"

    def add_data(self, key, data, shard_type):
        # Determine the shard for the key based on the specified sharding technique
        shard_id = self.get_shard(key, shard_type)

        # Store the data in the corresponding shard (simulated here)
        print(f"Storing data in Shard {shard_id} using {shard_type} - Data: {data}")

# Example Usage
sharding = HybridSharding()

# Assign ranges for range-based sharding
sharding.assign_range("Shard A", 1, 100)
sharding.assign_range("Shard B", 101, 200)

# Assign tags for tag-based sharding
sharding.assign_tags("Shard C", ["Tag1", "Tag2"])
sharding.assign_tags("Shard D", ["Tag2", "Tag3"])

# Assign weights for weighted sharding
sharding.assign_weight("Shard E", 2)
sharding.assign_weight("Shard F", 3)

# Add data using different sharding techniques
data = {
    "Key1": "Data for Key1",
    "Key2": "Data for Key2",
    "Key3": "Data for Key3",
    "Key4": "Data for Key4",
    "Key5": "Data for Key5"
}

for key, value in data.items():
    # Choose the sharding technique based on the key
    shard_type = "range_sharding" if key.isnumeric() else "tag_sharding" if key.startswith("Tag") else "weighted_sharding"
    sharding.add_data(key, value, shard_type)
