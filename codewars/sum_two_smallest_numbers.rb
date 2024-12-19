# Sum of two lowest positive integers
# https://www.codewars.com/kata/558fc85d8fd1938afb000014

# Challenge:
# Create a function that returns the sum of the two lowest positive 
# numbers given an array of minimum 4 positive integers. 
# 
# For example, when an array is passed like [19, 5, 42, 2, 77], 
# the output should be 7.

# Constraints: 
# No floats or non-positive integers will be passed.


'given an array a, return the sum of the lowest two integers'
def sum_two_smallest_numbers(a)
    a.sort!
    a[0..1].sum
end


#####################################################################
# tests

describe("Tests") do

    def do_test(input, expected)
      actual = sum_two_smallest_numbers(input)
      message = 'expected "' + expected.to_s + 
        '" but got "' + actual.to_s + '" for input "' + 
        input.to_s + '"'
      expect(actual).to eq(expected), message
    end
  
    it("Sample Tests") do
      do_test([5, 8, 12, 18, 22], 13) 
      do_test([7, 15, 12, 18, 22], 19) 
      do_test([25, 42, 71, 12, 18, 22], 30) 
      do_test([1, 1, 1, 4], 2) 
    end
  end
