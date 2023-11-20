# ### 7. Least Bandwidth Method

# - **Description**: Chooses the server that is currently serving the least amount of traffic measured in Mbps (Megabits per second).
# - **Use Case**: Effective in environments where bandwidth is a limiting factor.
class LeastBandwidthBalancer:
    def __init__(self, servers):
        """
        Initialize the balancer with a list of servers.
        """
        self.servers = servers
        self.bandwidth_usage = {server: 0.0 for server in servers}  # Initialize with zero bandwidth usage

    def update_bandwidth_usage(self, server, bandwidth):
        """
        Update the bandwidth usage of a server in Mbps.
        """
        self.bandwidth_usage[server] = bandwidth

    def get_server(self):
        """
        Get the server with the least bandwidth usage.
        """
        if not self.servers:
            raise ValueError("No servers available")

        # Select the server with the minimum bandwidth usage
        return min(self.bandwidth_usage, key=self.bandwidth_usage.get)

# Usage
servers = ["Server1", "Server2", "Server3"]
lbb = LeastBandwidthBalancer(servers)

# Updating bandwidth usage (in Mbps) based on monitoring data
lbb.update_bandwidth_usage("Server1", 50)
lbb.update_bandwidth_usage("Server2", 30)
lbb.update_bandwidth_usage("Server3", 40)

# Getting the server for a request
print(f"Request directed to {lbb.get_server()}")
