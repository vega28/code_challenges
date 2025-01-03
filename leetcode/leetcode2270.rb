# Leetcode exercise # 2270
# Number of Ways to Split Array 
# https://leetcode.com/problems/number-of-ways-to-split-array


# @param {Integer[]} nums
# @return {Integer}
def ways_to_split_array(nums)
    sumleft, sumright, valid_split_count = 0, nums.sum, 0
    for i in 0..(nums.length-2)
        sumleft += nums[i]
        sumright -= nums[i]
        valid_split_count += 1 if sumleft >= sumright
    end
    valid_split_count
end


#####################################################################
# tests

describe("Tests") do

    def do_test(input, expected)
      actual = ways_to_split_array(input)
      message = 'expected "' + expected.to_s + '" but got "' + actual.to_s + '" for array "' + input.to_s + '"'
      expect(actual).to eq(expected), message
    end

    it("Sample Tests") do
      do_test([10,4,-8,7],2)
      do_test([2,3,1,0],2)
    end
  end

