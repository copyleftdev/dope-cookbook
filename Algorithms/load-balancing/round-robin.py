# Description: The simplest form of load balancing algorithms. It distributes incoming requests sequentially among all servers in the pool. Once it reaches the end of the list, it starts again at the first server.
# Use Case: Best for scenarios where all servers are of equal specification and there are not many persistent connections.
class RoundRobinBalancer:
    def __init__(self, servers):
        """Initialize the balancer with a list of servers."""
        self.servers = servers
        self.server_count = len(servers)
        self.index = 0

    def get_server(self):
        """Get the next server in a round-robin fashion."""
        if not self.servers:
            raise ValueError("No servers available")

        server = self.servers[self.index]
        self.index = (self.index + 1) % self.server_count
        return server

# Usage
servers = ["Server1", "Server2", "Server3", "Server4"]
rr_balancer = RoundRobinBalancer(servers)

for _ in range(10):
    print(rr_balancer.get_server())
