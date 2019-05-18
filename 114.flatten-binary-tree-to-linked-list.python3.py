#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (39.13%)
# Total Accepted:    195.6K
# Total Submissions: 499.9K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
# 

#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev=None
        self.temp=None

        def dfs(root):
            if root is None:
               return None

            dfs(root.right)
            dfs(root.left)
           
            
            root.left=None
            root.right=self.prev
            self.prev=root
            self.temp=root
             
            # print(self.temp.val,"local temp")
             

        dfs(root)
        # print(self.temp.val,"----------")
        

             
