# - **Description**: Similar to Least Connections but with server weighting. The server's weight is considered along with the number of current connections.
# - **Use Case**: Useful for a mixed environment where servers have different processing capabilities.
class WeightedLeastConnectionsBalancer:
    def __init__(self, server_weights):
        """
        Initialize the balancer with a dictionary of servers and their weights.
        server_weights format: {'Server1': weight1, 'Server2': weight2, ...}
        """
        self.servers = list(server_weights.keys())
        self.weights = list(server_weights.values())
        self.connections = {server: 0 for server in self.servers}

    def get_server(self):
        """Get the server with the least number of connections adjusted by weight."""
        if not self.servers:
            raise ValueError("No servers available")

        # Calculate the weight per connection for each server
        weight_per_connection = {server: self.connections[server] / weight if weight > 0 else float('inf') 
                                 for server, weight in zip(self.servers, self.weights)}

        # Select the server with the lowest weight per connection
        selected_server = min(weight_per_connection, key=weight_per_connection.get)
        self.connections[selected_server] += 1
        return selected_server

    def release_server(self, server):
        """Release a connection from a server."""
        if self.connections[server] > 0:
            self.connections[server] -= 1

# Usage
server_weights = {"Server1": 5, "Server2": 3, "Server3": 2}
wlcb = WeightedLeastConnectionsBalancer(server_weights)

# Simulate requests
for _ in range(10):
    server = wlcb.get_server()
    print(f"Request directed to {server}")
    # Simulate releasing connections
    if _ % 3 == 0:
        wlcb.release_server(server)
