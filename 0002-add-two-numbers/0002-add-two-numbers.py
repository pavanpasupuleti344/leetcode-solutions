# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry=0
        ans=ListNode(0)
        main=ans
        while True:
            s=0
            
            if l1:
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next
            put=(s+carry)%10
            ans.next=ListNode(put)
            ans=ans.next
            carry=(s+carry)//10
            if l1==None and l2==None and carry==0:return main.next


