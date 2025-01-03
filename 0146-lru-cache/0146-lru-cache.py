class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

        self.cache = {}

    def remove_from_left(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_to_right(self, node):
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.prev = prev_node

        next_node.prev = node
        node.next = next_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        get_key_node = self.cache[key]
        self.remove_from_left(get_key_node)

        self.insert_to_right(get_key_node)

        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_from_left(self.cache[key])

        new_node = Node(key, value)
        self.insert_to_right(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            least_recently_used_node = self.left.next
            self.remove_from_left(least_recently_used_node)
            del self.cache[least_recently_used_node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)