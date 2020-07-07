class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the trew
    def insert(self, value):
        if self.contains(value):
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
                return True
        elif value <= self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
                return True

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found
    # Return the maximum value found in the tree

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        current = self
        if current:
            fn(current.value)
            if current.left:
                current.left.for_each(fn)
            if current.right:
                current.right.for_each(fn)
