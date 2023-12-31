'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        def dfs(root, level):
            if  not root.left and  not root.right:
                return level
            ans=2**31
            if root.left:
                ans=min(ans, dfs(root.left, level+1))
            if root.right:
                ans=min(ans, dfs(root.right, level+1))
            return ans
        
        if not root: 
            return 0
        return dfs(root, 1)
    

root = [3,9,20,None,None,15,7]
# root = [2,None,3,None,4,None,5,None,6]

print('\nRes:', Solution().minDepth(root))