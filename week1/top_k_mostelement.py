# Problem: Top K Frequent Elements
# Platform: LeetCode
# Problem Number: 347
# Topic: Arrays & Hashing
# Approach: Dictionary + Sorting
# Description:
# Find the k most frequently occurring elements
# in the given integer array.
# Time Complexity: O(n + m log m)
# Space Complexity: O(m)




class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for num in  nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        new_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        result= [item[0] for item in new_freq[:k]]
        return result
    