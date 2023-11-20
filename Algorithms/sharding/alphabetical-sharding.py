    # - **Description**: Data is partitioned based on the first letter or character of a specific attribute, such as usernames or product names.
    # - **Use Case**: Applicable when data can be naturally grouped by alphabetical order, e.g., creating separate shards for products starting with different letters.
import string

class AlphabeticalSharding:
    def __init__(self, num_shards):
        self.num_shards = num_shards
        self.shards = {}
        self.initialize_shards()

    def initialize_shards(self):
        # Create and initialize shards
        for i in range(self.num_shards):
            shard_name = f"Shard_{i}"
            self.shards[shard_name] = {}

    def calculate_shard(self, key):
        # Calculate the shard based on the starting character of the key
        starting_char = key[0].upper()  # Consider uppercase for simplicity
        shard_index = ord(starting_char) % self.num_shards
        shard_name = f"Shard_{shard_index}"
        return shard_name

    def insert_data(self, key, value):
        # Determine the shard for the key and insert data into the shard
        shard_name = self.calculate_shard(key)
        self.shards[shard_name][key] = value

    def query_data(self, key):
        # Determine the shard for the key and query data from the shard
        shard_name = self.calculate_shard(key)
        shard_data = self.shards[shard_name]
        if key in shard_data:
            return shard_data[key]
        else:
            return "Data not found."

# Example Usage
num_shards = 5
alphabetical_sharding = AlphabeticalSharding(num_shards)

# Insert data into the alphabetical sharding
data = {
    "Apple": "Red fruit",
    "Banana": "Yellow fruit",
    "Carrot": "Orange vegetable",
    "Dog": "Domestic animal",
    "Elephant": "Large mammal",
    "Giraffe": "Tall herbivore",
}

for key, value in data.items():
    alphabetical_sharding.insert_data(key, value)

# Query data from the alphabetical sharding
print(alphabetical_sharding.query_data("Apple"))     # Returns: "Red fruit"
print(alphabetical_sharding.query_data("Elephant"))  # Returns: "Large mammal"
print(alphabetical_sharding.query_data("Zebra"))     # Returns: "Data not found."
