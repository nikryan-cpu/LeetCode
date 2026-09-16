# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if lists is None:
            return None
        result = ListNode()
        write = result
        id_ = 0
        heap = []
        for node in lists:
            if node is not None:
                heapq.heappush(heap, (node.val, id_, node))
                id_ += 1
        
        while len(heap) != 0:
            min_ = heapq.heappop(heap)[-1]
            write.next = min_
            write = write.next

            if min_.next is not None:
                heapq.heappush(heap, (min_.next.val, id_, min_.next))
                id_ += 1

        

        return result.next