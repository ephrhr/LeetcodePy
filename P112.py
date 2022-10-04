from asyncio.windows_events import NULL
from typing import List, Set, Dict, Tuple, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


sol = Solution()


def createTreeNode(data, index=0):
    node = None
    if index < len(data):
        if data[index] == None:
            return
        node = TreeNode(data[index])
        node.left = createTreeNode(data, 2 * index + 1)
        node.right = createTreeNode(data, 2 * index + 2)
    return node


print(sol.hasPathSum(createTreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
                     22))
