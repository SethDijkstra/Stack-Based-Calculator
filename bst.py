class Node:

    def __init__(self, key, value):
        # the variable name, like "x"
        self.key = key
        # the number that variable holds, like 5
        self.value = value
        # points to the left child node (starts as nothing)
        self.left = None
        # points to the right child node (starts as nothing)
        self.right = None


class BinarySearchTree:

    def __init__(self):
        # the very top node of the tree, starts empty
        self.root = None

    def insert(self, key, value):
        # add a new variable into the tree
        new_node = Node(key, value)

        # if the tree is empty just put it at the top
        if self.root is None:
            self.root = new_node
            return

        # otherwise walk down the tree to find the right spot
        current = self.root
        while True:
            # go left if the new key is smaller
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            # go right if the new key is bigger
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
            # if the key already exists just update the value
            else:
                current.value = value
                break

    def search(self, key):
        # look through the tree for a variable name
        # returns its value if found, returns None if not found
        current = self.root

        while current is not None:
            if key == current.key:
                # found it, return the value
                return current.value
            elif key < current.key:
                # key is smaller so go left
                current = current.left
            else:
                # key is bigger so go right
                current = current.right

        # if we get here the key was not in the tree
        return None

    def delete(self, key):
        # remove a variable from the tree by its name
        # we need to track the parent so we can reconnect after removing
        parent = None
        current = self.root

        # walk down the tree to find the node we want to delete
        while current is not None:
            if key == current.key:
                break
            elif key < current.key:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        # if we never found the key, just stop
        if current is None:
            return

        # case 1 - node has no children (it is a leaf, just remove it)
        if current.left is None and current.right is None:
            if parent is None:
                # it was the only node in the tree
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # case 2 - node has two children (this one needs extra steps)
        elif current.left is not None and current.right is not None:
            # find the in-order successor which is the smallest node in the right subtree
            # we will copy its data here then delete it from down there
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            # copy the successor data into the node we want to delete
            current.key = successor.key
            current.value = successor.value

            # now delete the successor node (it can only have a right child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        # case 3 - node has one child (just skip over it)
        else:
            # figure out which child exists
            if current.left is not None:
                child = current.left
            else:
                child = current.right

            if parent is None:
                # the node being deleted was the root
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

    def delete_all(self):
        # wipe out the entire tree by setting root to nothing
        # Python will clean up all the nodes on its own
        self.root = None

    def display_tree(self):
        # print the tree visually, sideways
        # the right side shows at the top, root shows at the bottom
        # each level gets 4 extra spaces of indentation
        # we use a helper function that calls itself recursively
        self._show_node(self.root, 0)

    def _show_node(self, node, depth):
        # this helper does the actual printing
        # it prints right subtree first (shows at top), then itself, then left subtree
        if node is None:
            return

        # go right first so it shows up at the top of the output
        self._show_node(node.right, depth + 1)

        # print this node with indentation based on how deep it is
        indent = "    " * depth
        print(indent + "||==> " + node.key + ":" + str(node.value))

        # go left last so it shows up at the bottom
        self._show_node(node.left, depth + 1)
