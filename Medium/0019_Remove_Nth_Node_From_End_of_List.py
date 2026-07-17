"""
LeetCode #19 - Remove Nth Node From End of List

Problem Link:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Difficulty: Medium

Approach:
- Use the two-pointer technique with a dummy node.
- Move the first pointer (var1) n+1 steps ahead.
- Move both pointers together until the first pointer reaches the end.
- The second pointer (var2) will be just before the node to remove.
- Update the links to skip the target node.

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
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        temp = ListNode(0)
        temp.next = head

        var1 = temp
        var2 = temp

        for _ in range(n + 1):
            var1 = var1.next

        while var1:
            var1 = var1.next
            var2 = var2.next

        var2.next = var2.next.next

        return temp.next
