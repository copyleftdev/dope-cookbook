#    - **Description**: Data is partitioned based on a predefined range of values, such as key ranges or timestamps.
#    - **Use Case**: Suitable for scenarios where data can be logically divided into continuous ranges, like partitioning user data by registration date.
class RangeBasedSharding:
    def __init__(self):
        # Initialize shard ranges and shard mapping
        self.shard_ranges = [(0, 100), (101, 200), (201, 300)]  # Example shard ranges
        self.shard_mapping = {}

    def get_shard(self, key: int) -> int:
        # Find the shard for the given key
        for shard_id, (start, end) in enumerate(self.shard_ranges):
            if start <= key <= end:
                return shard_id
        # Key is not within any range, return -1 or handle accordingly
        return -1

    def add_data(self, key: int, data: str):
        # Determine the shard for the key
        shard_id = self.get_shard(key)
        
        if shard_id != -1:
            # Store the data in the corresponding shard (simulated here)
            if shard_id not in self.shard_mapping:
                self.shard_mapping[shard_id] = []
            self.shard_mapping[shard_id].append((key, data))
        else:
            # Handle cases where the key does not belong to any shard range
            print(f"Key {key} does not belong to any shard range.")

    def get_data(self, key: int) -> str:
        # Determine the shard for the key
        shard_id = self.get_shard(key)
        
        if shard_id != -1 and shard_id in self.shard_mapping:
            # Retrieve the data from the corresponding shard (simulated here)
            shard_data = self.shard_mapping[shard_id]
            for k, data in shard_data:
                if k == key:
                    return data
            # Key not found in the shard
            return f"Data for key {key} not found in shard {shard_id}."
        else:
            # Handle cases where the key does not belong to any shard range
            return f"Key {key} does not belong to any shard range."

# Example Usage
sharding = RangeBasedSharding()
sharding.add_data(50, "Data for Key 50")
sharding.add_data(150, "Data for Key 150")
sharding.add_data(250, "Data for Key 250")

print(sharding.get_data(50))   # Returns: "Data for Key 50"
print(sharding.get_data(150))  # Returns: "Data for Key 150"
print(sharding.get_data(300))  # Returns: "Key 300 does not belong to any shard range."
