# Leetcode exercise # 15
# 3Sum 
# https://leetcode.com/problems/3sum/

import time
from random import randint


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """ given a list of at least 3 integers, return all unique triplets
            for which the sum is zero.

            fourth attempt: peeked at a sample and realized switching the
            direction of travel for k allows a lot quicker math to skip over
            duplicates and jump to the next likely element to make real change

            constraints:
                3 <= nums.length <= 3000
                -10**5 <= nums[i] <= 10**5

            utilize the 2-pointer method
        """
        
        n = len(nums)
        nums.sort() 
        triplets_list = []

        for i in range(n - 2): # O(n)-ish (maybe more?)
            if i == 0 or not nums[i] == nums[i-1]: # skip duplicate i values
                j, k = i + 1, n - 1
                while j < k:
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0: # store the triple, increment j, decrement k
                        triplets_list.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while j < k and nums[j] == nums[j-1]: # skip duplicate j values
                            j += 1
                        k -= 1
                        while j < k and nums[k] == nums[k+1]: # skip duplicate k values
                            k -= 1
                    elif total > 0: # decrement k to reduce total towards zero
                        k -= 1
                    elif total < 0: # increment j to increase total towards zero
                        j += 1

        return triplets_list # net O(n^2)


    def threeSumV1(self, nums: list[int]) -> list[list[int]]:
        """ given a list of at least 3 integers, return all unique triplets
            for which the sum is zero.

            first attempt: naive method with untenable complexity from nested loops

            utilize the 2-pointer method
        """
        
        n = len(nums)
        triplets_list = []

        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0: # check validity of triplet
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort() # to ensure uniqueness
                        if triplet not in triplets_list:
                            triplets_list.append(triplet)

        return triplets_list

        
    def threeSumV2(self, nums: list[int]) -> list[list[int]]:
        """ given a list of at least 3 integers, return all unique triplets
            for which the sum is zero.

            second attempt: increase efficiency by setting limits on i and k

            utilize the 2-pointer method
        """
        
        n = len(nums)
        triplets_list = []

        nums_map = {} # store num as key, count as value
        for num in nums:
            nums_map[num] = nums_map.get(num,0) + 1
        unique_nums = list(nums_map.keys())
        unique_nums.sort()

        # handle edge case quickly for all positive or all negative
        if min(unique_nums) >= 0 or max(unique_nums) <= 0:
            if nums_map.get(0) and nums_map[0] >= 3:
                return [[0, 0, 0]] # all zeroes is allowed
            return []

        # get values sorted and max of 2 in a row:
        nums_short = []
        for num in unique_nums:
            count = nums_map[num] if nums_map[num] <= 2 or num == 0 else 2
            nums_short += [num]*count

        n = len(nums_short)
        first_non_negative_index = 1
        while nums_short[first_non_negative_index] < 0:
            first_non_negative_index += 1
        
        for i in range(0, first_non_negative_index+1):
            for j in range(i+1, n-1):
                k_min = first_non_negative_index if j+1 < first_non_negative_index else j+1
                for k in range(k_min, n):
                    if nums_short[i] + nums_short[j] + nums_short[k] == 0: # check validity of triplet
                        triplet = [nums_short[i], nums_short[j], nums_short[k]]
                        triplet.sort() # to ensure uniqueness
                        if triplet not in triplets_list:
                            triplets_list.append(triplet)

        triplets_list.sort()
        return triplets_list

        
    def threeSumV3(self, nums: list[int]) -> list[list[int]]:
        """ given a list of at least 3 integers, return all unique triplets
            for which the sum is zero.

            third attempt: increase efficiency by setting limits on i and k 
            and using hashes/sets (also drifting away from the two pointer method...)

            utilize the 2-pointer method
        """
                     
        n = len(nums)
        triplets_set = set()
        triplets_list = []

        nums_map = {} # store num as key, count as value
        pointed_values = {'i_vals': set(), 'j_vals': set(), 'k_vals': set()} # store list of values each pointer would pass by
        for num in nums:
            if not nums_map.get(num) or nums_map[num] < 2 or num == 0:
                nums_map[num] = nums_map.get(num,0) + 1
            if num < 0:
                pointed_values['i_vals'].add(num)
                pointed_values['j_vals'].add(num)
            elif num > 0:
                pointed_values['k_vals'].add(num)
                pointed_values['j_vals'].add(num)
            elif num == 0:
                pointed_values['j_vals'].add(num)
                if nums_map[num] > 1:
                    pointed_values['i_vals'].add(num)
                if nums_map[num] > 2:
                    pointed_values['k_vals'].add(num)

        for i_val in pointed_values['i_vals']:
            for j_val in pointed_values['j_vals']:
                for k_val in pointed_values['k_vals']:
                    if i_val == j_val and nums_map[j_val] < 2:
                        pass
                    elif j_val == k_val and nums_map[j_val] < 2:
                        pass
                    elif i_val == j_val == k_val == 0 and nums_map[0] < 3:
                        pass
                    elif i_val + j_val + k_val == 0: # check validity of triplet
                        triplet = [i_val, j_val, k_val]
                        triplet.sort() # to ensure uniqueness
                        triplet_tuple = (triplet[0], triplet[1],triplet[2])
                        if triplet_tuple not in triplets_set:
                            triplets_list.append(triplet)
                            triplets_set.add(triplet_tuple)

        return triplets_list



#####################################################################
# Tests
sol = Solution()

inputs =    [[1,2,-3],
            [-1,0,1,2,-1,-4],
            [0,0,0,0,0,5],
            [0,1,2],
            [1,2,3],
            [1,1,-2],
            [-1,0,1,2,-1,-4,-2,-3,3,0,4],
            [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
            ]
expected_outputs =  [[[-3, 1, 2]],
                    [[-1, 0, 1], [-1, -1, 2]],
                    [[0,0,0]],
                    [],
                    [],
                    [[-2,1,1]],
                    [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]],
                    [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]
                    ]

for i, input_vals in enumerate(inputs):
    print(f"\nstarting test {i+1} --------------------------")
    start_time = time.time()
    actual_output = sol.threeSum(input_vals)
    run_time = time.time() - start_time
    actual_output.sort()
    expected_outputs[i].sort()
    passed = 'PASSED' if actual_output == expected_outputs[i] else 'FAILED'
    print(f"test {i+1} - {passed} - runtime: {run_time:.2}s")
    if not passed:
        print("    input:", input_vals)
        print("    expected output:", expected_outputs[i])
        print("    actual output:", actual_output)

print("\ncomparing runtimes of different implementations with larger input:")
input_list = []
for x in range(1000):
    input_list.append(randint(-10**5, 10**5))
start_time = time.time()
actual_output = sol.threeSumV1(input_list)
run_time = time.time() - start_time
print(f"test 8 using version 1 runtime: {run_time:.2}s")
start_time = time.time()
actual_output = sol.threeSumV2(input_list)
run_time = time.time() - start_time
print(f"test 8 using version 2 runtime: {run_time:.2}s")
start_time = time.time()
actual_output = sol.threeSumV3(input_list)
run_time = time.time() - start_time
print(f"test 8 using version 3 runtime: {run_time:.2}s")
start_time = time.time()
actual_output = sol.threeSum(input_list)
run_time = time.time() - start_time
print(f"test 8 using version 4 (final) runtime: {run_time:.2}s")