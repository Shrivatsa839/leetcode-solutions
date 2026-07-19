"""
LeetCode #24 - Swap Nodes in Pairs

Problem Link:
https://leetcode.com/problems/swap-nodes-in-pairs/

Difficulty: Medium

Approach:
- Create a dummy node pointing to the head.
- Traverse the linked list two nodes at a time.
- Swap every adjacent pair by updating the node links.
- Move to the next pair until the end of the list.

Time Complexity: O(n)
Space Complexity: O(1)

Author: Shrivatsa Khandare
Language: Python
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next and current.next.next:

            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next
