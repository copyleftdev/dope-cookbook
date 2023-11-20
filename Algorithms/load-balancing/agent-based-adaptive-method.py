# - **Description**: In this method, an agent on the server reports the current load to the load balancer, which then makes decisions based on this real-time data.
# - **Use Case**: Useful in dynamic environments where server load can change rapidly.

class ServerAgent:
    """
    Represents an agent residing on a server, reporting server metrics.
    """
    def __init__(self, name, load_balancer):
        self.name = name
        self.load_balancer = load_balancer
        self.load = 0

    def update_load(self, load):
        """Update the server load and report to the load balancer."""
        self.load = load
        self.load_balancer.report_load(self.name, load)

class AdaptiveLoadBalancer:
    def __init__(self):
        self.server_loads = {}

    def report_load(self, server_name, load):
        """Receive load update from a server agent."""
        self.server_loads[server_name] = load

    def get_server(self):
        """Select the server with the least load."""
        if not self.server_loads:
            raise ValueError("No server load data available")

        return min(self.server_loads, key=self.server_loads.get)

# Setup
load_balancer = AdaptiveLoadBalancer()
servers = [ServerAgent(f"Server{i}", load_balancer) for i in range(1, 4)]

# Simulating server load updates
servers[0].update_load(70)
servers[1].update_load(50)
servers[2].update_load(30)

# Load balancer selects server
selected_server = load_balancer.get_server()
print(f"Request directed to {selected_server}")
