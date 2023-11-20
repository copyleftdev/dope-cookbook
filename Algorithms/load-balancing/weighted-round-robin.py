# - **Description**: An extension of the Round Robin algorithm, where each server is assigned a weight based on its capacity (CPU, RAM). Servers with higher capacities handle more requests.
# - **Use Case**: Ideal when servers in the pool have different capabilities.
class WeightedRoundRobinBalancer:
    def __init__(self, server_weights):
        """
        Initialize the balancer with a dictionary of servers and their weights.
        server_weights format: {'Server1': weight1, 'Server2': weight2, ...}
        """
        self.servers = list(server_weights.keys())
        self.weights = list(server_weights.values())
        self.server_count = len(self.servers)
        self.current_index = -1
        self.current_weight = 0

    def get_server(self):
        """Get the next server according to weighted round robin algorithm."""
        while True:
            self.current_index = (self.current_index + 1) % self.server_count
            if self.current_index == 0:
                self.current_weight = self.current_weight - 1
                if self.current_weight <= 0:
                    self.current_weight = max(self.weights)
                    if self.current_weight == 0:
                        return None
            if self.weights[self.current_index] >= self.current_weight:
                return self.servers[self.current_index]

# Usage
server_weights = {"Server1": 1, "Server2": 3, "Server3": 2}
wrr_balancer = WeightedRoundRobinBalancer(server_weights)

for _ in range(10):
    print(wrr_balancer.get_server())
