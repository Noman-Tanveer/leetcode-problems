# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_ll = count_node = ListNode()
        new_ll.next = count_node.next = head
        if not head:
            return head
        nodes = 0
        while count_node.next:
            nodes += 1
            count_node = count_node.next

        from_start = nodes-n

        if from_start < 0:
            return None
        elif from_start == 0:
            return head.next

        for i in range(from_start):
            new_ll = new_ll.next

        new_ll.next = new_ll.next.next

        return head
