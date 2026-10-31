# Problem: Remove Duplicates from Sorted Array
# Platform: LeetCode
# Problem Number: 26
# Topic: Arrays
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0

        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1