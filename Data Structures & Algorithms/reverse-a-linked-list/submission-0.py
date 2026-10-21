# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        current = head

        while current:
            list1.append(current.val)
            current = current.next

        #new_list
        new_head = ListNode()
        current = new_head
        for element in list1[::-1]:
            current.next = ListNode(val=element)
            current = current.next

        return new_head.next