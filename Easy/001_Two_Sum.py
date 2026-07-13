"""
LeetCode #1 - Two Sum

Problem Link:
https://leetcode.com/problems/two-sum/

Difficulty: Easy

Approach:
- Use a hash map (dictionary) to store the numbers and their indices.
- For each number, calculate the complement (target - current number).
- If the complement already exists in the hash map, return the indices.
- Otherwise, store the current number and its index.

Time Complexity: O(n)
Space Complexity: O(n)

Author: Shrivatsa Khandare
Language: Python
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i


# Test Case
if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    result = solution.twoSum(nums, target)

    print("Input:", nums)
    print("Target:", target)
    print("Output:", result)

