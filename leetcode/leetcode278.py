# Leetcode exercise # 278
# Binary Search range example - find first bad product version 
# https://leetcode.com/problems/first-bad-version

import time


class Solution:
    def set_first_bad_ver(self, first_bad_ver: int):
        """ sets the first bad version for testing purposes """
        self.first_bad_ver = first_bad_ver


    def isBadVersion(self, version: int) -> bool:
        """ was defined by leetcode - returns True for any bad version """
        if version >= self.first_bad_ver:
            return True
        else:
            return False


    def firstBadVersion(self, n: int) -> int:
        """ 
            use ranged binary search to find the first version number n
            that returns isBadVersion(n) == True

            constraints:
                1 <= bad <= n <= 2**31 - 1
                (there will always be at least one bad version)

            time complexity: O(log n)
            space complexity: O(1)
        """
        low, high = 0, n
        while low <= high:
            m = (low + high) // 2
            if low == high:
                if self.isBadVersion(m):
                    return m
                else:
                    return m + 1
            elif self.isBadVersion(m): # check lower
                high = m
            else: # not bad version - check higher
                low = m + 1
        

#####################################################################
# Tests
sol = Solution()

inputs = [
    (5, 4),
    (1, 1),
    (3, 2)
    ]
expected_outputs = [
    4,
    1,
    2
    ]

for i, input_vals in enumerate(inputs):
    print(f"\nstarting test {i+1} --------------------------")
    sol.set_first_bad_ver(input_vals[1])
    start_time = time.time()
    actual_output = sol.firstBadVersion(input_vals[0])
    run_time = time.time() - start_time
    passed = 'PASSED' if actual_output == expected_outputs[i] else 'FAILED'
    print(f"test {i+1} - {passed} - runtime: {run_time:.2}s")
    if not passed == 'PASSED':
        print("    input:", input_vals)
        print("    expected output:", expected_outputs[i])
        print("    actual output:", actual_output)
