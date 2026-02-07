# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting anchor
        dummy = ListNode(0)
        tail = dummy

        # While both lists have nodes remaining
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1    # Attach list1 node
                list1 = list1.next   # Move list1 pointer forward
            else:
                tail.next = list2    # Attach list2 node
                list2 = list2.next   # Move list2 pointer forward
            
            # Move the tail of our new list forward
            tail = tail.next

        # If one list is exhausted, attach the remainder of the other list
        tail.next = list1 or list2

        # Return the actual head (skipping the dummy node)
        return dummy.next