# Problem: Group Anagrams
# Platform: LeetCode
# Problem Number: 49
# Topic: Arrays & Hashing
# Approach: Sorting + Dictionary
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)




class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
               counter={}
               for char in strs:
                    key=''.join(sorted(char))
                    if key in counter:
                         counter[key].append(char)
                    else:
                         counter[key]=[char]
               return list(counter.values())