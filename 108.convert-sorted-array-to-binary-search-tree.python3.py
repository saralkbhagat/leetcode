#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (47.09%)
# Total Accepted:    208.7K
# Total Submissions: 443.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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
    def sortedArrayToBST(self, nums):
        startt=0
        endd=len(nums)-1
        
        def make(start,end,nums):
            if  end<start:
                return
            mid=int((start+end)/2)
            root=TreeNode(nums[mid])
            root.left=make(start,mid-1,nums)
            root.right=make(mid+1,end,nums)
            return root
        return  (make(startt,endd,nums))


        
