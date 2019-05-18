#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (57.34%)
# Total Accepted:    396.8K
# Total Submissions: 692K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):

#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global maxx
        maxx=0
        if root is None:
            return 0

        
        def help(root,depth):
            
            if root is None:
                return 
            global maxx
            
            
            
            if depth>maxx:
                maxx=depth
                # print(maxx)
            help(root.left,depth+1)
            help(root.right,depth+1)

        help(root,0)
        return maxx+1

        
