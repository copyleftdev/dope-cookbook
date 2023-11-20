# - **Description**: Requests are sent to a preferred server first, and if that server is unavailable, the next server in a predetermined list is used.
# - **Use Case**: Ideal for disaster recovery setups where primary and secondary (backup) servers are used.

class Server:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.load = 0
        self.active = True

    def can_handle_request(self):
        return self.active and self.load < self.weight

    def handle_request(self):
        if self.can_handle_request():
            self.load += 1
            return True
        return False

    def release_resources(self):
        if self.load > 0:
            self.load -= 1

class ChainedFailoverBalancer:
    def __init__(self, servers):
        self.servers = servers

    def get_server(self):
        for server in self.servers:
            if server.handle_request():
                return server
        raise Exception("No available servers to handle the request")

    def release_resources(self, server):
        server.release_resources()

# Setup
servers = [Server(f"Server{i}", weight) for i, weight in enumerate([10, 20, 30], start=1)]
balancer = ChainedFailoverBalancer(servers)

# Simulating request handling
try:
    selected_server = balancer.get_server()
    print(f"Request handled by {selected_server.name}")
    # After request is processed
    balancer.release_resources(selected_server)
except Exception as e:
    print(str(e))
