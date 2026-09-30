# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        h=ListNode(0)
        h.next=head
        h=h.next
        num=[]
        while h:
            num.append(h.val)
            h=h.next
        ans=ListNode(0)
        main=ans
        for i in num[::-1]:
            ans.next=ListNode(i)
            ans=ans.next
        return main.next