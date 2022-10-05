import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTreeNode(data, index=0):
    node = None
    if index < len(data):
        if data[index] == None:
            return
        node = TreeNode(data[index])
        node.left = createTreeNode(data, 2 * index + 1)
        node.right = createTreeNode(data, 2 * index + 2)
    return node


def TreeNodeToList(root: TreeNode):
    arr = []
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        qNext = queue.Queue()
        while not q.empty():
            node = q.get()
            if node is not None:
                arr.append(node.val)
                qNext.put(node.left)
                qNext.put(node.right)
            else:
                arr.append(None)
        q = qNext
    while arr[len(arr) - 1] is None:
        arr.pop()
    return arr
