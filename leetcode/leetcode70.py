# Leetcode exercise # 70
# 1D Dynamic Programming Example - climbing stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairsTopDown(self, n: int) -> int:
        """ Returns the number of distinct ways you can climb a staircase of n steps 
            if each time you can either climb one or two steps.

            Uses top-down 1D dynamic programming (memoization)

            constraints:
                1 <= n <= 45

            e.g.
            >>> s.climbStairsTopDown(n=1)
            1
            >>> s.climbStairsTopDown(n=2)
            2
            >>> s.climbStairsTopDown(n=3)
            3
            >>> s.climbStairsTopDown(n=4)
            5
            >>> s.climbStairsTopDown(n=45)
            1836311903
        """
        return self.memoization(n)


    def memoization(self, n, cache = {}):
        # base case:
        if n <= 2:
            return n

        # check if step is in cache, which stores number of paths at given step
        if cache.get(n):
            return cache[n]

        # otherwise check paths
        cache[n] = self.memoization(n - 1,cache) + self.memoization(n-2,cache)
        
        return cache[n]


    def climbStairsBottomUp(self, n: int) -> int:
        """ Returns the number of distinct ways you can climb a staircase of n steps 
            if each time you can either climb one or two steps.

            Uses bottom-up 1D dynamic programming

            constraints:
                1 <= n <= 45

            e.g.
            >>> s.climbStairsBottomUp(n=1)
            1
            >>> s.climbStairsBottomUp(n=2)
            2
            >>> s.climbStairsBottomUp(n=3)
            3
            >>> s.climbStairsBottomUp(n=4)
            5
            >>> s.climbStairsBottomUp(n=45)
            1836311903
            
        """
        if n <= 2:
            return n

        paths, i = [1,2], 2

        while i < n:
            # each step includes all prior paths
            paths[0], paths[1] = paths[1], paths[0]+paths[1]
            i += 1

        return paths[1]


        


#####################################################################
# run tests

if __name__ == '__main__':
    import doctest
    result = doctest.testmod(globs={'s': Solution()})
    if not result.failed:
        print("ALL DOCTESTS PASSED. GOOD WORK!")
