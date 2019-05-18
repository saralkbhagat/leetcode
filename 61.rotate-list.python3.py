#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (25.63%)
# Total Accepted:    161.2K
# Total Submissions: 628.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        
        front=head
        count=0
        flag=True
        if front is None:
            return None


        while front is not None:
            front=front.next
            count=count+1
        if k==0:
            return head
        round=k/count
        if k>count:
            k=k%count
            if k==0:
                k=count

        print(k,count)
        if round==1:
            return head
        
        front=head
        for i in range(1,count+1):
            prev=front
            front=front.next
            if i==count-k:

                out=front
                inn=prev
                flag=False
                print(out.val)
        if flag is True:
            return head
        prev.next=head
        inn.next=None
        return out
            



        
