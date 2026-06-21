# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers at the head of the list.
        # slow moves one node at a time, fast moves two nodes at a time.
        slow = head
        fast = head

        # Continue while fast can safely move two steps.
        # When fast reaches the end of the list,
        # slow will be positioned at the middle node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # For even-length lists, this naturally returns
        # the second middle node, as required.
        return slow
        