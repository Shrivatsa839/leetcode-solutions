"""
LeetCode #28 - Find the Index of the First Occurrence in a String

Problem Link:
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Difficulty: Easy

Approach:
- Traverse the haystack string.
- At each index, extract a substring having the same length as the needle.
- Compare the substring with the needle.
- If they match, return the current index.
- If no match is found after checking all positions, return -1.

Time Complexity: O((n - m + 1) * m)
Space Complexity: O(m)

Author: Shrivatsa Khandare
Language: Python
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):

            if haystack[i:i + len(needle)] == needle:
                return i

        return -1
