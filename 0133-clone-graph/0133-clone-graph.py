"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_map = {}
        node_map[node] = Node(node.val)

        node_q = deque()
        node_q.append(node)

        while node_q:
            old_node = node_q.popleft()
            for nei in old_node.neighbors:
                if nei not in node_map:
                    node_map[nei] = Node(nei.val)
                    node_q.append(nei)
            
                node_map[old_node].neighbors.append(node_map[nei])

        return node_map[node]
        

        