# Problem: Valid Anagram
# Platform: LeetCode
# Problem Number: 242
# Topic: Arrays & Hashing
# Approach: Character Frequency using Dictionaries
# Time Complexity: O(n)
# Space Complexity: O(k)


s = "a"
t = "ab"
if len(s)==len(t):

    counter={}
    counter1={}
    for char in s:
        if char in counter:
             counter[char]+=1
        else:
             counter[char]=1
    for char in t:
        if char in counter1:
            counter1[char]+=1
        else:
            counter1[char]=1
    if counter==counter1:
        print (True)
    else:
        print(False)
else:
    print(False)