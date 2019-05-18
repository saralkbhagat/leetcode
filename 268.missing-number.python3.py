#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (46.37%)
# Total Accepted:    214.5K
# Total Submissions: 462.7K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#
class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        sum=(n*(n+1))/2


        for i in nums:
            sum=sum-i

        return int(sum)




