"""
LeetCode 3: Longest Substring Without Repeating Characters

Problem: Find longest substring without repeating characters
Approach: Sliding window with hash map
Time: O(n) | Space: O(min(m,n))
"""

def lengthOfLongestSubstring(s):
    char_map = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        char = s[right]
        
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        
        char_map[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

if __name__ == "__main__":
    s1 = "abcabcbb"
    print(f"Test 1: '{s1}'")
    print(f"Output: {lengthOfLongestSubstring(s1)}")  # Expected: 3
    print()
    
    s2 = "bbbbb"
    print(f"Test 2: '{s2}'")
    print(f"Output: {lengthOfLongestSubstring(s2)}")  # Expected: 1
    print()
    
    s3 = "pwwkew"
    print(f"Test 3: '{s3}'")
    print(f"Output: {lengthOfLongestSubstring(s3)}")  # Expected: 3