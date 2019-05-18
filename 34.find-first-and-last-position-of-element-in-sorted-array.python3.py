#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (32.20%)
# Total Accepted:    233.3K
# Total Submissions: 724.7K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution:
    def searchRange(self, nums, target):
        start=0
        end=len(nums)-1
        lowresult=-1
        highresult=-1

        while(start<=end):
            mid=(start+end)//2

            if nums[mid]==target:
                lowresult=mid
                end=mid-1
            if nums[mid]<target:
                start=mid+1
            if nums[mid]>target:
                end=mid-1
        # print(start,end,lowresult,highresult)

        start=0
        end=len(nums)-1

        while(start<=end):
            mid=(start+end)//2

            if nums[mid]==target:
                highresult=mid
                start=mid+1
            if nums[mid]<target:
                start=mid+1
            if nums[mid]>target:
                end=mid-1
        lis=[lowresult,highresult]
        return lis
            



        
