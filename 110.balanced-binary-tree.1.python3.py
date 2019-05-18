#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (39.07%)
# Total Accepted:    248.7K
# Total Submissions: 636.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, r):
        def isBalancedd(root):
        
            def height(roott):
                if roott is None:
                    return -1
                
                h= max(height(roott.left), height(roott.right)) + 1
                return h

            if root is None:
                return True
                
            else:
                hr=height(root.right)
                hl=height(root.left)
                # leftheight=height(root.left)
                # rightheight=height(root.right)
                if (abs(hl - hr) <= 1) and isBalancedd( root.left) is True and isBalancedd( root.right) is True: return True
                else: return False
        f=isBalancedd(r)
        return f
 