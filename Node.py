
# Import deque to use as a queue for level-order traversal
from collections import deque


# Create a Node class to represent each folder or file
class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name  # Store the folder or file name
        self.left = left  # Store the left child
        self.right = right  # Store the right child


# Pre-order Traversal: Root, Left, Right
def preorder(node):
    if node is None:  # Stop if there is no node
        return

    print(node.name, end=" ")  # Visit the current node
    preorder(node.left)  # Visit the left child
    preorder(node.right)  # Visit the right child


# In-order Traversal: Left, Root, Right
def inorder(node):
    if node is None:  # Stop if there is no node
        return

    inorder(node.left)  # Visit the left child
    print(node.name, end=" ")  # Visit the current node
    inorder(node.right)  # Visit the right child


# Post-order Traversal: Left, Right, Root
def postorder(node):
    if node is None:  # Stop if there is no node
        return

    postorder(node.left)  # Visit the left child
    postorder(node.right)  # Visit the right child
    print(node.name, end=" ")  # Visit the current node


# Level-order Traversal: Visit nodes level by level
def levelorder(root):
    if root is None:  # Stop if the tree is empty
        return

    queue = deque([root])  # Add the root node to the queue

    while queue:  # Continue while the queue is not empty
        node = queue.popleft()  # Remove the first node from the queue
        print(node.name, end=" ")  # Visit the current node

        if node.left is not None:  # Check if a left child exists
            queue.append(node.left)  # Add the left child to the queue

        if node.right is not None:  # Check if a right child exists
            queue.append(node.right)  # Add the right child to the queue


# Create the file system directory tree
root = Node(
    "C:",  # Root folder
    Node("Documents", Node("School"), Node("Resume.pdf")),
    Node("Pictures", Node("Vacation.jpg"))
)


# Display the result of pre-order traversal
print("Pre-order Traversal:")
preorder(root)

# Display the result of in-order traversal
print("\n\nIn-order Traversal:")
inorder(root)

# Display the result of post-order traversal
print("\n\nPost-order Traversal:")
postorder(root)

# Display the result of level-order traversal
print("\n\nLevel-order Traversal:")
levelorder(root)

# Print a final newline
print()