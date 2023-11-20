# - **Description**: Directs traffic to the server with the fewest active connections. This is more intelligent than Round Robin as it considers the current load on each server.
# - **Use Case**: Useful in environments where the server load is not evenly distributed, and some requests take longer to process than others.

class LeastConnectionsBalancer:
    def __init__(self, servers):
        """Initialize the balancer with a list of servers and a corresponding list of connection counts."""
        self.servers = servers
        self.connections = {server: 0 for server in servers}

    def get_server(self):
        """Get the server with the least number of connections."""
        if not self.servers:
            raise ValueError("No servers available")

        # Find the server with the least connections
        least_connections_server = min(self.connections, key=self.connections.get)
        self.connections[least_connections_server] += 1
        return least_connections_server

    def release_server(self, server):
        """Release a connection from a server."""
        if self.connections[server] > 0:
            self.connections[server] -= 1

# Usage
servers = ["Server1", "Server2", "Server3", "Server4"]
lc_balancer = LeastConnectionsBalancer(servers)

# Simulate requests
for _ in range(6):
    server = lc_balancer.get_server()
    print(f"Request directed to {server}")
    # Simulate releasing connections
    if _ % 2 == 1:
        lc_balancer.release_server(server)
