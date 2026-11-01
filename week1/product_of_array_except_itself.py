# Problem: Product of Array Except Self
# Platform: LeetCode
# Problem Number: 238
# Topic: Arrays
# Approach: Prefix and Suffix Products
# Description:
# Return an array where each element is the
# product of all other elements in the input array.
# The solution does not use division.
# Time Complexity: O(n)
# Space Complexity: O(1) extra space (excluding output)




class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            result[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]