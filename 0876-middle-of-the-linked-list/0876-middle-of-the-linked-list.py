# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        ans=head
        c=0
        while ans:
            c+=1
            ans=ans.next
        mid=(c//2)+1
        # start=0
        for i in range(mid-1):
            head=head.next
        # print(c,mid)
        return head
