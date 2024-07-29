"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.clone_map = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node in self.clone_map:
            return self.clone_map[node]
        
        clone = Node(node.val)
        self.clone_map[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))

        return self.clone_map[node]