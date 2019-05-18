#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (24.21%)
# Total Accepted:    323.6K
# Total Submissions: 1.3M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nm=nums1
        nnm=nums2
        l=len(nm)+len(nnm)
        
        def findkth(k,n,nn):
            # print(n," ",nn)
            x=len(n)//2
            y=len(nn)//2
            if len(n)==0:
                print("returningh",nn[k])
                return nn[k]
            if len(nn)==0:
                print("returningh",n[k])
                return n[k]
            
            if k>x+y: #right
                if n[x]>nn[y]:
                    return findkth(k-y-1,n,nn[y+1:])
                else:
                    return findkth(k-x-1,n[x+1:],nn)
            else:
                if n[x]>nn[y]:
                    return findkth(k,n[:x],nn)
                else:
                    return findkth(k,n,nn[:y])
        if l%2==0:
            print("this")
            return (findkth(l//2,nm,nnm)+findkth((l//2)-1,nm,nnm))/2
        else:
            print(findkth(l//2,nm,nnm),"madar")
            return findkth(l//2,nm,nnm)
        

        
