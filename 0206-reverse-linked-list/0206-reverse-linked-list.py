# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # temp
        if head:
            temp=ListNode(head.val)
            head=head.next
        else:return head
        while head:
            new=ListNode(head.val)
            new.next=temp
            temp=new
            head=head.next
        return temp

