"""
LeetCode #9 - Palindrome Number

Problem Link:
https://leetcode.com/problems/palindrome-number/

Difficulty: Easy

Approach:
- Negative numbers cannot be palindromes because of the negative sign.
- Convert the integer to a string.
- Compare the string with its reverse.
- If both are equal, the number is a palindrome.

Time Complexity: O(n)
Space Complexity: O(n)

Author: Shrivatsa Khandare
Language: Python
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        return str(x) == str(x)[::-1]
