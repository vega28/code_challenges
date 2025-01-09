# Leetcode exercise # 3
# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters

import time
import string
from random import choice


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' given a string s, find the length of the longest substring with no repeating characters
            
            use the sliding window method

            constraints:
                0 <= s.length <= 5 * 10**4
                s consists of English letters, digits, symbols and spaces
        '''
        if not s:
            return 0
        left, right, longest = 0, 1, 1
        windowset = set(s[left])
        while right < len(s):
            if s[right] in windowset:
                while not s[right] == s[left]:
                    windowset.remove(s[left])
                    left += 1
                left += 1
            else:
                windowset.add(s[right])
                if longest < (right-left+1):
                    longest += 1 
            right += 1
        return longest

        

#####################################################################
# Tests
sol = Solution()

inputs = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    ""
    ]
expected_outputs = [
    3, 
    1,
    3,
    0
    ]

for i, input_vals in enumerate(inputs):
    print(f"\nstarting test {i+1} --------------------------")
    start_time = time.time()
    actual_output = sol.lengthOfLongestSubstring(input_vals)
    run_time = time.time() - start_time
    passed = 'PASSED' if actual_output == expected_outputs[i] else 'FAILED'
    print(f"test {i+1} - {passed} - runtime: {run_time:.2}s")
    if not passed:
        print("    input:", input_vals)
        print("    expected output:", expected_outputs[i])
        print("    actual output:", actual_output)


print("\ncomparing runtimes for different input sizes:")
chars = string.ascii_letters + string.digits

input_string = ''
n = 10
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.lengthOfLongestSubstring(input_string)
run_time = time.time() - start_time
print(input_string)
print(f"input length: {n} - runtime: {run_time:.2}s")

input_string = ''
n = 100
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.lengthOfLongestSubstring(input_string)
run_time = time.time() - start_time
print(input_string)
print(f"input length: {n} - runtime: {run_time:.2}s")

input_string = ''
n = 10**3
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.lengthOfLongestSubstring(input_string)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_string = ''
n = 10**4
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.lengthOfLongestSubstring(input_string)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_string = ''
n = 10**5
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.lengthOfLongestSubstring(input_string)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")