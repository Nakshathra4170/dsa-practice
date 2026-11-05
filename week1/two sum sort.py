# Problem: Two Sum II - Input Array Is Sorted
# Platform: LeetCode
# Problem Number: 167
# Topic: Two Pointers, Arrays
# Approach: Two Pointers
# Description:
# Find two numbers in a sorted array whose
# sum equals the given target.
# Return their 1-based indices.
# Time Complexity: O(n)
# Space Complexity: O(1)





class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [left+1,right+1]
            elif sum>target:
                right-=1
            else:
                
                left+=1
            
        