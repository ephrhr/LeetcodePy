from asyncio.windows_events import NULL
from typing import List, Set, Dict, Tuple, Optional
from TreeNode import TreeNode, createTreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


sol = Solution()

print(sol.hasPathSum(createTreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
                     22))
