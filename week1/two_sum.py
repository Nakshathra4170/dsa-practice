# Problem: Two Sum
# Platform: LeetCode
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in freq:
                return [freq[complement], i]

            freq[nums[i]] = i