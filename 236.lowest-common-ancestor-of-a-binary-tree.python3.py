#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (32.70%)
# Total Accepted:    207.1K
# Total Submissions: 633.5K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# ⁠       _______3______
# ⁠      /              \
# ⁠   ___5__          ___1__
# ⁠  /      \        /      \
# ⁠  6      _2       0       8
# ⁠        /  \
# ⁠        7   4
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself
# ⁠            according to the LCA definition.
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
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
    


    def lowestCommonAncestor(self, root, p, q):

        def dec():
            global lisaa
            global lisa
            global result
            global a 
            global b
            lisb=[]
            lisaa=[]
            lisa=[]
            a=[]
            b=[]
            result=[]
        
        
        def search(root,var):
            global lisaa
            global lisa
            global result
            global a 
            global b
            
        
            # print("come",end='')
            if root is None:
                return
        
            # print(root.data,end=',')
            lisa.append(root.val)
            # print(lisa,'this is lis')
            if root.val==var:
                lisaa=lisa[:]
                # print(lisa)
            search(root.left,var)
            search(root.right,var)
            lisa.pop(-1)
            # print("going",a,end='...')
            # print("")
        
        def lca(root, p, q):
            global lisaa
            global lisa
            
            global a 
            global b
            
            
            search(root,p)
            a=lisaa[:]
            del lisaa
        
            search(root,q)
            b=lisaa[:]
            while a and b:
                global result
                
                # print(a, b)
                apop=a.pop(0)
                bpop=b.pop(0)
        
                if apop==bpop :
                   result.append(apop)
        
            return result.pop(-1)
        
        dec()
        answer=lca(root,5,4)
        return answer