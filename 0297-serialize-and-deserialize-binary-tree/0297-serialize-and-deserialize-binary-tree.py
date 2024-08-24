# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque()
        output = []

        q.append(root)
        while q:
            curr = q.popleft()

            if not curr:
                output.append("N")
                continue
                
            output.append(str(curr.val))

            q.append(curr.left)
            q.append(curr.right)

        print(",".join(output))
        return ",".join(output)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        vals = data.split(",")
        print(vals)

        if vals[0] == "N":
            return None

        nodes = []

        for val in vals:
            if val == "N":
                nodes.append(TreeNode("null"))  
            else:
                nodes.append(TreeNode(val))

        print(len(nodes))

        i = 0
        for node in nodes:
            if node.val == "null":
                continue

            if 2 * i + 1 in range(len(nodes)) and (nodes[2 * i + 1]).val != "null":
                node.left = nodes[2 * i + 1]

            if 2 * i + 2 in range(len(nodes)) and (nodes[2 * i + 2]).val != "null":
                node.right = nodes[2 * i + 2]
            
            i += 1

        return nodes[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))