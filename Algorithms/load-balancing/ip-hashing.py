# - **Description**: A hash function is used to determine which server will handle the request based on the IP address of the client.
# - **Use Case**: Effective for ensuring that a user will consistently connect to the same server, which can be important for session consistency.
import hashlib

class IPHashBalancer:
    def __init__(self, servers):
        """Initialize the balancer with a list of servers."""
        self.servers = servers
        self.server_count = len(servers)

    def get_server(self, ip_address):
        """Get the server for a given IP address using a hash function."""
        if not self.servers:
            raise ValueError("No servers available")

        # Create a hash of the IP address and use it to determine the server
        hash_value = int(hashlib.sha256(ip_address.encode()).hexdigest(), 16)
        server_index = hash_value % self.server_count
        return self.servers[server_index]

# Usage
servers = ["Server1", "Server2", "Server3", "Server4"]
ip_hash_balancer = IPHashBalancer(servers)

# Simulating client requests with different IP addresses
client_ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "192.168.1.2"]
for ip in client_ips:
    server = ip_hash_balancer.get_server(ip)
    print(f"Client {ip} directed to {server}")