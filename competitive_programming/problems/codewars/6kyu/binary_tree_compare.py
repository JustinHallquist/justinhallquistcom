# return True if the two binary trees rooted and a and b are equal in value and structure
# return False otherwise


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def tree_obj_to_arr(node, res):
    if not node:
        return res

    res.append(node.val if node else None)

    tree_obj_to_arr(node.left, res) if node.left else res.append(None)
    tree_obj_to_arr(node.right, res) if node.right else res.append(None)

    return res


def compare(a, b):
    return tree_obj_to_arr(a, []) == tree_obj_to_arr(b, [])


a_node = Node(1, Node(2, None, None), None)
b_node = Node(1, Node(2, None, None), None)
c_node = Node(1, None, Node(2, None, None))

results1 = compare(a_node, b_node)

assert results1 == True

results2 = compare(a_node, c_node)
assert results2 == False
