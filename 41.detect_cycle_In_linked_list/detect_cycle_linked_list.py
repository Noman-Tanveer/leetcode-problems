# Solution if the Linked list has unique values.

from types import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack = []
        while True:
            if not head:
                return False
            if not head.next:
                return False
            if head.val not in stack:
                stack.append(head.val)
            else:
                return True
            head = head.next

# Simple solution stores all nodes and compares them
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack = []
        while True:
            if not head:
                return False
            if not head.next:
                return False
            if head not in stack:
                stack.append(head)
            else:
                return True
            head = head.next

# Effecient two pointers solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast != slow:
            if not fast or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
