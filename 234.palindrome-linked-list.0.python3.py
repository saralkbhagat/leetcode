#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (34.11%)
# Total Accepted:    184.3K
# Total Submissions: 540.3K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self,head):
        if head is None:
            return True
        
        """
        :type head: ListNode
        :rtype: bool
        """
        global flag
        flag = True

        global count
        count=1
        front = head
        def countt(front):
            global count
            while front.next is not None:
                front=front.next
                count += 1
        global prev
        prev = None
        countt(head)
        if count==1:
            return True
        #print(count)
        front = head
        if count % 2 != 0 :
            for i in range(count // 2 - 1):
                front = front.next
            front.next = front.next.next

        front = head
        for i in range(count // 2 ):  # Reverse list

            # #print (prev)

            # #print(" data ",front.val,end='--> ')
            # if prev is not None: #print(prev.val, " is this prev ")
            next = front.next
            front.next = prev
            # if front.next is not None: #print(front.next.val, " is this prev ")
            prev = front
            front = next
            # #print(front.val,front.next. val , end=" ||")
        # #print(front.val," after in the middle ")
        newfront = front

        # #print(newfront.val,"xxxxxxxxxxxxxxxxxxxxxx")
        front=prev
        # for i in range(count // 2 ):
        #
        #     #print(front.val,".....",i)
        #     front=front.next
        # for i in range(count // 2 ):
        #
        #     #print(newfront.val,".....",i)
        #     newfront=newfront.next

        for i in range(count // 2 ):
            global flag
            # #print(newfront.val,front.val)
            if newfront.val != front.val:
                flag = False
            front=front.next
            newfront=newfront.next
        return flag
    
            
        
            
            






        
        
