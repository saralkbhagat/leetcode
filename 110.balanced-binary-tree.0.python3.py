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
    def isBalanced(self, root):
        flag=True


        def height(root):
            global flag
            
            if root is None:
                # print("None root")
                return 0

            hleft= height(root.left)
            hright=height(root.right)

            
            h = hleft + hright + 1
            if (root.left and root.right) is None:
                
                h=0
                
            # print("here",root.data,h)    
                
            print(root.data, h,"  l r",hleft,hright)
            if hleft<hright:
                hleft,hright=hright,hleft
            if hleft-hright>1:
                flag=False
            

            return h
        return flag
        
