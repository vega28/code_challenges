# Get Middle
# https://www.codewars.com/kata/56747fd5cb988479af000028

# Challenge:
# You are going to be given a non-empty string. Your job is to 
# return the middle character(s) of the string.
# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters. 

# Constraints: none


'given a string s, return the middle character(s)'
def get_middle(s)
    mid_i = s.length/2
    mid = s.length.odd? ? s[mid_i] : s[mid_i-1..mid_i]
end


#####################################################################
# tests

describe("Tests") do

    def do_test(input, expected)
      actual = get_middle(input)
      message = 'expected "' + expected + '" but got "' + actual + '" for string "' + input + '"'
      expect(actual).to eq(expected), message
    end
  
    it("Sample Tests") do
      do_test("test","es")
      do_test("testing","t")
      do_test("middle","dd")
      do_test("A","A")
      do_test("of","of")
    end
  end

