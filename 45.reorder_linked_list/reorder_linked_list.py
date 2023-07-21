from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        cur, length = head, 0

        while cur:
            arr.append(cur)
            cur = cur.next
            length += 1

        left, right = 0, length-1

        while left<right:
            arr[left].next = arr[right]
            left += 1

            if left==right:
                arr[right].next = arr[left]
                break

            arr[right].next = arr[left]
            right -= 1

        return head
