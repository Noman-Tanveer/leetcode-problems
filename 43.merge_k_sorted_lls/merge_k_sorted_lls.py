from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        last_node = ListNode()
        new_ll = last_node
        if not any(lists):
            return new_ll.next
        # get index and node of the LL with min value
        while any(lists):
            lists = list(filter(lambda val: val != None, lists))
            min_ll_idx = lists.index(min(lists, key=lambda l: l.val))
            last_node.next = lists[min_ll_idx]
            lists[min_ll_idx] = lists[min_ll_idx].next
            last_node = last_node.next
        return new_ll.next