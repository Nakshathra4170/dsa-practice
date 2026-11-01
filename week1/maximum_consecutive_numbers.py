# Problem: Longest Consecutive Sequence
# Platform: LeetCode
# Problem Number: 128
# Topic: Arrays & Hashing
# Approach: Hash Set
# Description:
# Find the length of the longest consecutive
# sequence in an unsorted integer array.
# The solution uses a set to identify sequence
# starting points and count consecutive numbers.
# Time Complexity: O(n) average
# Space Complexity: O(n)



class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen=set(nums)
        longest=0
        for num in seen:
            
            if num-1  not in seen:
                count=1
                
                while num+1 in seen:
                    count+=1
                    
                    num+=1
                longest=max(longest,count)
        return longest