# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def getTail(node):
            prev = None
            while node:
                _next = node.next
                if node.child:
                    # ... <-> node <-> node.child <-> ...
                    node.next = node.child
                    node.child = None
                    node.next.prev = node
                # get the end node of the node.child list
                    prev = getTail(node.next)
                    if _next:
                        # ... <-> prev (end node) <-> _next (originally node.next) <-> ...
                        _next.prev = prev
                        prev.next = _next
                else:
                    prev = node
                node = _next  # loop through the list of nodes
            return prev  # return end node

        getTail(head)
        return head
