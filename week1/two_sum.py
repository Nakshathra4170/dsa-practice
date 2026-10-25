"""
LeetCode 1: Two Sum

Problem: 
Given array of integers nums and integer target,
return indices of two numbers that add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]  (because 2+7=9)

Approach:
Use hash map to store: {number: index}
For each number, check if (target - number) exists
If yes, return both indices
If no, add current number to map

Time: O(n) - single pass
Space: O(n) - hash map storage
"""

def twoSum(nums, target):
    """
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    # Dictionary to store: {number: index}
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in map
        if complement in num_map:
            return [num_map[complement], i]
        
        # Add current number to map
        num_map[num] = i
    
    # No solution found
    return []

# Test cases
if __name__ == "__main__":
    # Test 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: {nums1}, target={target1}")
    print(f"Output: {twoSum(nums1, target1)}")  # Expected: [0, 1]
    print()
    
    # Test 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2: {nums2}, target={target2}")
    print(f"Output: {twoSum(nums2, target2)}")  # Expected: [1, 2]
    print()
    
    # Test 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Test 3: {nums3}, target={target3}")
    print(f"Output: {twoSum(nums3, target3)}")  # Expected: [0, 1]