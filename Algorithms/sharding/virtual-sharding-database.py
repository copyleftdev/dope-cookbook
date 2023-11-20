#    - **Description**: Virtual shards act as an additional layer of abstraction, allowing for easier movement and rebalancing of data between physical shards.
#     - **Use Case**: Useful in scenarios where data distribution needs to be managed dynamically without affecting application logic.
import sqlite3
import hashlib
import os

class VirtualShardingDatabase:
    def __init__(self, num_virtual_shards):
        self.num_virtual_shards = num_virtual_shards
        self.shard_connections = {}
        self.db_file_paths = []

    def connect_virtual_shards(self):
        # Create connections to virtual shards (SQLite databases)
        for i in range(self.num_virtual_shards):
            shard_name = f"shard_{i}.db"
            self.db_file_paths.append(shard_name)
            connection = sqlite3.connect(shard_name)
            self.shard_connections[i] = connection
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, key TEXT, value TEXT)''')
            connection.commit()

    def calculate_virtual_shard(self, key):
        # Calculate the virtual shard for a given key using a hash function
        hash_value = int(hashlib.sha256(key.encode()).hexdigest(), 16)
        return hash_value % self.num_virtual_shards

    def insert_data(self, key, value):
        # Determine the virtual shard and insert data into the appropriate shard
        virtual_shard = self.calculate_virtual_shard(key)
        connection = self.shard_connections[virtual_shard]
        cursor = connection.cursor()
        cursor.execute("INSERT INTO data (key, value) VALUES (?, ?)", (key, value))
        connection.commit()

    def query_data(self, key):
        # Determine the virtual shard and query data from the appropriate shard
        virtual_shard = self.calculate_virtual_shard(key)
        connection = self.shard_connections[virtual_shard]
        cursor = connection.cursor()
        cursor.execute("SELECT value FROM data WHERE key=?", (key,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return "Data not found."

    def close_connections(self):
        # Close connections to virtual shards
        for connection in self.shard_connections.values():
            connection.close()

    def remove_db_files(self):
        # Remove the SQLite database files
        for db_file_path in self.db_file_paths:
            if os.path.exists(db_file_path):
                os.remove(db_file_path)

# Example Usage
num_virtual_shards = 10
sharding_db = VirtualShardingDatabase(num_virtual_shards)

# Connect to virtual shards (SQLite databases)
sharding_db.connect_virtual_shards()

# Insert data into the virtual sharding database
sharding_db.insert_data("Key1", "Value1")
sharding_db.insert_data("Key2", "Value2")
sharding_db.insert_data("Key3", "Value3")

# Query data from the virtual sharding database
print(sharding_db.query_data("Key1"))  # Returns: "Value1"
print(sharding_db.query_data("Key4"))  # Returns: "Data not found."

# Close connections to virtual shards and remove the database files
sharding_db.close_connections()
sharding_db.remove_db_files()
