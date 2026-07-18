"""
LeetCode #27 - Remove Element

Problem Link:
https://leetcode.com/problems/remove-element/

Difficulty: Easy

Approach:
- Use a pointer (k) to track the position where the next valid element should be placed.
- Traverse the array once.
- If the current element is not equal to the value to remove, copy it to index k.
- Increment k after placing a valid element.
- Return k, which represents the number of remaining elements.

Time Complexity: O(n)
Space Complexity: O(1)

Author: Shrivatsa Khandare
Language: Python
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
