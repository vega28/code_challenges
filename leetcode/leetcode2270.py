# Leetcode exercise # 2270
# Number of Ways to Split Array 
# https://leetcode.com/problems/number-of-ways-to-split-array

import time
from random import randint


class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        """ 
        given a 0-indexed integer array nums of legnth n, return the
        number of splits in the array which meet the following criteria:
        1. the sum of the first i + 1 elements is >= the sum of the last n - i - 1 elements
        2. there is at least one element to the right of i (i.e. 0 <= i < n-1)

        constraints:
            2 <= len(nums) <= 10**5
            -10**5 <= nums[i] <= 10**5
        """
        sumleft, sumright, valid_split_count = 0, sum(nums), 0
        for i in range(len(nums)-1):
            sumleft += nums[i]
            sumright -= nums[i]
            if sumleft >= sumright:
                valid_split_count += 1
        return valid_split_count

        

#####################################################################
# Tests
sol = Solution()

inputs = [
    [10,4,-8,7],
    [2,3,1,0],
    ]
expected_outputs = [
    2, 
    2,
    ]

for i, input_vals in enumerate(inputs):
    print(f"\nstarting test {i+1} --------------------------")
    start_time = time.time()
    actual_output = sol.waysToSplitArray(input_vals)
    run_time = time.time() - start_time
    passed = 'PASSED' if actual_output == expected_outputs[i] else 'FAILED'
    print(f"test {i+1} - {passed} - runtime: {run_time:.2}s")
    if not passed:
        print("    input:", input_vals)
        print("    expected output:", expected_outputs[i])
        print("    actual output:", actual_output)


print("\ncomparing runtimes for different input sizes:")
input_list = []
n = 10
for x in range(n):
    input_list.append(randint(-10**5, 10**5))
start_time = time.time()
sol.waysToSplitArray(input_list)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_list = []
n = 100
for x in range(n):
    input_list.append(randint(-10**5, 10**5))
start_time = time.time()
sol.waysToSplitArray(input_list)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_list = []
n = 10**3
for x in range(n):
    input_list.append(randint(-10**5, 10**5))
start_time = time.time()
sol.waysToSplitArray(input_list)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_list = []
n = 10**4
for x in range(n):
    input_list.append(randint(-10**5, 10**5))
start_time = time.time()
sol.waysToSplitArray(input_list)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")

input_list = []
n = 10**5
for x in range(n):
    input_list.append(randint(-10**5, 10**5))
start_time = time.time()
sol.waysToSplitArray(input_list)
run_time = time.time() - start_time
print(f"input length: {n} - runtime: {run_time:.2}s")