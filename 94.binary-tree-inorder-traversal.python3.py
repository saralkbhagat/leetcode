
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        res=[]

        def go(root):
            if root is None:
                return
            else:          
            
            
                go(root.left)
                print(root.val,"       ")
                res.append(root.val)
                go(root.right)
        go(root)
        print(res)
        return res



         

        
        
