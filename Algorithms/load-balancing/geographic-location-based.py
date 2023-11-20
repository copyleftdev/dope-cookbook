# - **Description**: Routes traffic based on the geographical location of the client, often used to serve content from a server nearest to the user.
# - **Use Case**: Best for global applications where reducing latency is critical.

import math

def calculate_distance(user_location, server_location):
    """
    Calculate the distance between two locations.
    For simplicity, this function uses a basic Euclidean distance.
    In reality, you would use a more accurate method for geographical distances.
    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(user_location, server_location)))

class Server:
    def __init__(self, name, location):
        self.name = name
        self.location = location  # Location represented as (latitude, longitude)

class GeoLocationBalancer:
    def __init__(self, servers):
        self.servers = servers

    def get_server(self, user_location):
        """
        Selects the server closest to the user's geographic location.
        """
        closest_server = min(self.servers, key=lambda server: calculate_distance(user_location, server.location))
        return closest_server

# Setup
servers = [
    Server("Server_USA", (37.7749, -122.4194)),  # San Francisco
    Server("Server_EU", (52.5200, 13.4050)),     # Berlin
    Server("Server_ASIA", (35.6895, 139.6917))   # Tokyo
]
balancer = GeoLocationBalancer(servers)

# Simulating user request from a location (latitude, longitude)
user_location = (48.8566, 2.3522)  # Paris
selected_server = balancer.get_server(user_location)
print(f"User request from {user_location} directed to {selected_server.name}")
