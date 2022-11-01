from TreeNode import TreeNode, createTreeNode, TreeNodeToList
from typing import Optional
from collections import deque


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newHead = TreeNode(val, root)
            return newHead
        currDepth = 1
        q = deque()
        q.append(root)
        while len(q):
            qNext = deque()
            currDepth += 1
            while len(q):
                node = q.popleft()
                if currDepth == depth:
                    newLeft = TreeNode(val, node.left, None)
                    newRight = TreeNode(val, None, node.right)
                    node.left = newLeft
                    node.right = newRight
                if node.left is not None:
                    qNext.append(node.left)
                if node.right is not None:
                    qNext.append(node.right)
            q = qNext
        return root


sol = Solution()
data = createTreeNode([4, 2, 6, 3, 1, 5])

print(TreeNodeToList(sol.addOneRow(data, 1, 2)))

print(TreeNodeToList(sol.addOneRow(data, 1, 1)))
