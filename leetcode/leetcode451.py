# Leetcode exercise # 451
# Bucket Sort example - sort characters by frequency 
# https://leetcode.com/problems/sort-characters-by-frequency

import time
import string
from random import choice


class Solution:
    def frequencySort(self, s: str) -> str:
        """ 
        given a string s, sort it in decreasing order based on the frequency of the characters.

        use bucket sort since there are a limited number of characters.

        this sorting method is unstable, so return any one if there are multiple answers.

        constraints:
            1 <= s.length <= 5 * 10**5
            s consists of uppercase and lowercase English letters

        time complexity: O(n)
        space complexity: O(n)
        """
        sorted_s = ''
        charbuckets = {}
        for c in s:
            charbuckets[c] = charbuckets.get(c,0) + 1

        # sort charbuckets by descending count of values
        sorted_buckets = sorted(charbuckets.items(), key=lambda c: c[1], reverse=True)

        for (char, count) in sorted_buckets:
            sorted_s = sorted_s + char*count

        return sorted_s

        

#####################################################################
# Tests
sol = Solution()

inputs = [
    'tree',
    'cccaaa',
    'Aabb',
    ''
    ]
expected_outputs = [
    ['eert','eetr'],
    ['aaaccc','cccaaa'],
    ['bbAa','bbaA'],
    ['']
    ]

for i, input_vals in enumerate(inputs):
    print(f"\nstarting test {i+1} --------------------------")
    start_time = time.time()
    actual_output = sol.frequencySort(input_vals)
    run_time = time.time() - start_time
    passed = 'PASSED' if actual_output in expected_outputs[i] else 'FAILED'
    print(f"test {i+1} - {passed} - runtime: {run_time:.2}s")
    if not passed == 'PASSED':
        print("    input:", input_vals)
        print("    expected output:", expected_outputs[i])
        print("    actual output:", actual_output)


print("\ncomparing runtimes for different input sizes:")
chars = string.ascii_letters

input_string = ''
n = 10
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.frequencySort(input_string)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_string = ''
n = 100
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.frequencySort(input_string)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_string = ''
n = 10**3
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.frequencySort(input_string)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_string = ''
n = 10**4
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.frequencySort(input_string)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_string = ''
n = 10**5
for x in range(n):
    input_string += choice(chars)
start_time = time.time()
sol.frequencySort(input_string)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")