    # - **Description**: Data is partitioned based on timestamps or time intervals, making it suitable for time-series data.
    # - **Use Case**: Ideal for storing and managing time-series data, such as logs, sensor readings, or historical records.

from datetime import datetime, timedelta

class TimeBasedSharding:
    def __init__(self, shard_interval_minutes):
        self.shard_interval_minutes = shard_interval_minutes
        self.shards = {}
        self.current_shard = None
        self.initialize_shards()

    def initialize_shards(self):
        # Create and initialize shards
        self.current_shard = self.get_current_shard_name()
        self.shards[self.current_shard] = {}

    def get_current_shard_name(self):
        # Generate a shard name based on the current time
        now = datetime.now()
        shard_name = now.strftime("%Y%m%d%H%M")
        return shard_name

    def check_and_create_new_shard(self):
        # Check if it's time to create a new shard
        now = datetime.now()
        current_shard_name = self.get_current_shard_name()

        if current_shard_name != self.current_shard:
            # Create a new shard and switch to it
            self.current_shard = current_shard_name
            self.shards[self.current_shard] = {}

    def insert_data(self, key, value):
        # Check and create a new shard if necessary
        self.check_and_create_new_shard()

        # Insert data into the current shard
        self.shards[self.current_shard][key] = value

    def query_data(self, key):
        # Check and create a new shard if necessary
        self.check_and_create_new_shard()

        # Query data from the current shard
        current_shard_data = self.shards[self.current_shard]
        if key in current_shard_data:
            return current_shard_data[key]
        else:
            return "Data not found."

# Example Usage
shard_interval_minutes = 30
time_based_sharding = TimeBasedSharding(shard_interval_minutes)

# Insert data into the time-based sharding
data = {
    "Sensor1": "Measurement data 1",
    "Sensor2": "Measurement data 2",
    "Sensor3": "Measurement data 3",
    "Sensor4": "Measurement data 4",
}

for key, value in data.items():
    time_based_sharding.insert_data(key, value)

# Query data from the time-based sharding
print(time_based_sharding.query_data("Sensor1"))  # Returns: "Measurement data 1"
print(time_based_sharding.query_data("Sensor4"))  # Returns: "Measurement data 4"

# Wait for a new shard to be created (simulated)
# After waiting for some time, a new shard will be created automatically
# You can continue inserting and querying data, and it will be stored in the new shard.
