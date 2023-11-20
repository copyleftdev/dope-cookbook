#    - **Description**: Raft is a consensus algorithm designed for understandability and ease of implementation. It elects a leader in a distributed cluster, and the leader coordinates actions among nodes. Raft divides time into terms and elects leaders in each term.
#    - **Use Case**: Raft is widely used in distributed systems where simplicity and clarity of implementation are crucial. It's often chosen for building distributed key-value stores and fault-tolerant services.
import random

class RaftNode:
    def __init__(self, node_id, all_nodes):
        self.node_id = node_id
        self.all_nodes = all_nodes
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.leader_id = None

    def request_votes(self):
        self.current_term += 1
        self.voted_for = self.node_id
        votes_received = 1  # Vote for itself
        for node in self.all_nodes:
            if node.node_id != self.node_id:
                response = node.receive_vote_request(self.node_id, self.current_term)
                if response:
                    votes_received += 1

        if votes_received > len(self.all_nodes) / 2:
            self.become_leader()

    def receive_vote_request(self, candidate_id, candidate_term):
        if candidate_term > self.current_term:
            self.current_term = candidate_term
            self.voted_for = None

        if self.voted_for is None and candidate_term == self.current_term:
            self.voted_for = candidate_id
            return True
        else:
            return False

    def become_leader(self):
        self.leader_id = self.node_id
        print(f"Node {self.node_id} became the leader for term {self.current_term}")

# Example Usage
nodes = [RaftNode(1, []), RaftNode(2, []), RaftNode(3, [])]
nodes[0].all_nodes = nodes
nodes[1].all_nodes = nodes
nodes[2].all_nodes = nodes

# Simulate a leader election
nodes[0].request_votes()
