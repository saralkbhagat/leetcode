#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (35.83%)
# Total Accepted:    245K
# Total Submissions: 683.7K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    
    def hasPathSum(self, root, sum):
        

        if root is None:
            return False
        def hhasPathSum(root,sum):
            
            
            if root is None:
                return 
            sum=sum-root.val
            if sum == 0 and root.left is None and root.right is None:
                found = True
                print("this worked")
            else:
                found = False
                
            return found
        l=hhasPathSum(root.left, sum)
        r=hhasPathSum(root.right, sum)
        return l or r 
            
        # a=hhasPathSum(root,sum)
        # print(a)
        # return(a)


        
    
        
