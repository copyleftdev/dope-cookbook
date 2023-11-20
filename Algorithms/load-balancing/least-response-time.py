# - **Description**: Directs traffic to the server with the fewest active connections and the lowest average response time.
# - **Use Case**: Good for high-traffic websites where minimizing response time is crucial.
class LeastResponseTimeBalancer:
    def __init__(self, servers):
        """
        Initialize the balancer with a list of servers.
        """
        self.servers = servers
        self.response_times = {server: 1.0 for server in servers}  # Initialize with default response time

    def update_response_time(self, server, response_time):
        """
        Update the response time of a server.
        """
        self.response_times[server] = response_time

    def get_server(self):
        """
        Get the server with the least response time.
        """
        if not self.servers:
            raise ValueError("No servers available")

        # Select the server with the minimum response time
        return min(self.response_times, key=self.response_times.get)

# Usage
servers = ["Server1", "Server2", "Server3"]
lrtb = LeastResponseTimeBalancer(servers)

# Updating response times based on some external metrics or monitoring
lrtb.update_response_time("Server1", 0.2)
lrtb.update_response_time("Server2", 0.5)
lrtb.update_response_time("Server3", 0.3)

# Getting the server for a request
print(f"Request directed to {lrtb.get_server()}")
