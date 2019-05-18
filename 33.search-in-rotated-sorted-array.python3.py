#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.16%)
# Total Accepted:    319K
# Total Submissions: 991.9K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#
class Solution:
    def search(self, nums, target):
        inp=nums
        t=target
        high = len(inp)-1
        low=0
        global res
        res=-1
        def helper(A,high,low,x):
            global res
            #print("")
            if low>high:
                return
            mid=(high-low)/2+low
            mid=int(mid)
            #print("L,M,H", A[low], A[mid], A[high],  end=",")
            if A[mid]==x:
                #print("case 1")
                res=mid
                #print("this is result",res)
                return mid
# to Optimize use the below code
            # if A[low]<=A[high]:
            #     #print("case 2", end='')
            #     if A[mid]<x:
            #         #print("case 2A mid<x")
            #         low=mid+1
            #     else:
            #         #print("case 2b mid>x")
            #         high=mid-1

                helper(A, high, low, x)
            else:
                if A[low]<=A[mid]:
                    if x>=A[low] and x<A[mid]:
                        high = mid - 1
                    else:low=mid+1
                if A[mid]<=A[high]:
                    if x>A[mid] and x<=A[high]:
                        low = mid + 1
                    else:high=mid-1
                helper(A, high, low, x)

        helper(inp, high, low, t)
        return res
            
