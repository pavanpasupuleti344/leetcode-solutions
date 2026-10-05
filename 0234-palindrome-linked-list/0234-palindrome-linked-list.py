# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        i=0
        j=len(a)-1
        while i<j:
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True
