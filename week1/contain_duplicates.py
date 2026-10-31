# Problem: Contains Duplicate
# Platform: LeetCode
# Approach: Set
# Time Complexity: O(n) average
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
    
