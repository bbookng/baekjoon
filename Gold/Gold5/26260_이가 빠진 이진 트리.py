N = int(input())

nodes = list(map(int, input().split()))
X = int(input())

nodes[nodes.index(-1)] = X
nodes.sort()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BST(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = Node(nums[mid])

    root.left = BST(nums[:mid])
    root.right = BST(nums[mid + 1:])

    return root

tree = BST(nodes)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

postorder(tree)