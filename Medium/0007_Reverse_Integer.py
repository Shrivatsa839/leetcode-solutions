"""
LeetCode #7 - Reverse Integer

Problem Link:
https://leetcode.com/problems/reverse-integer/

Difficulty: Medium

Approach:
- Check if the number is negative and store its sign.
- Reverse the digits using modulo (%) and integer division (//).
- Restore the sign if the original number was negative.
- Check whether the reversed integer lies within the 32-bit signed integer range.
- Return 0 if it overflows; otherwise, return the reversed integer.

Time Complexity: O(log10(n))
Space Complexity: O(1)

Author: Shrivatsa Khandare
Language: Python
"""


class Solution:
    def reverse(self, x: int) -> int:

        negative = False

        if x < 0:
            negative = True
            x = -x

        rev = 0

        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        if negative:
            rev = -rev

        if rev < -(2**31) or rev > (2**31 - 1):
            return 0

        return rev
