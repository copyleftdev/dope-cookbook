#    - **Description**: ZAB is used in Apache ZooKeeper to maintain a consistent and replicated state. It provides linearizable updates to a distributed state machine by sequencing and broadcasting transactions.
#    - **Use Case**: Apache ZooKeeper itself is a distributed coordination service. It's used in various applications for leader election, distributed locks, and configuration management.
import threading
import time

class ZabNode:
    def __init__(self, node_id, all_nodes):
        self.node_id = node_id
        self.all_nodes = all_nodes
        self.current_epoch = 0
        self.pending_broadcast = None
        self.state = "FOLLOWER"
        self.last_seen_leader = None

    def start(self):
        while True:
            if self.state == "FOLLOWER":
                self.handle_follower_state()
            elif self.state == "LEADER":
                self.handle_leader_state()

    def handle_follower_state(self):
        # Follower logic: Wait for broadcasts and check leader heartbeats
        if self.pending_broadcast:
            self.receive_broadcast(self.pending_broadcast)
            self.pending_broadcast = None

        if self.last_seen_leader and time.time() - self.last_seen_leader > 3:
            # If no leader heartbeats for a while, transition to candidate
            self.state = "CANDIDATE"
            print(f"Node {self.node_id} transitioned to CANDIDATE state")

    def handle_leader_state(self):
        # Leader logic: Continuously send heartbeats and broadcast messages
        self.last_seen_leader = time.time()
        print(f"Node {self.node_id} is the leader")

        # Simulate broadcasting a message
        message = f"Message from Leader Node {self.node_id}"
        self.send_broadcast(message)

    def receive_broadcast(self, message):
        # Handle received broadcast message
        print(f"Node {self.node_id} received broadcast: {message}")

    def send_broadcast(self, message):
        for node in self.all_nodes:
            if node.node_id != self.node_id:
                node.pending_broadcast = message

# Create ZabNodes
nodes = [ZabNode(1, []), ZabNode(2, []), ZabNode(3, [])]
nodes[0].all_nodes = nodes
nodes[1].all_nodes = nodes
nodes[2].all_nodes = nodes

# Start ZabNodes in separate threads
threads = []
for node in nodes:
    thread = threading.Thread(target=node.start)
    threads.append(thread)

for thread in threads:
    thread.start()

# Simulate a broadcast message from one node to others
nodes[0].send_broadcast("Message from Node 1")
