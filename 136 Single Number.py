# Mauricio Garcia
# This problem introduces the XOR operator as the key insight rather than relying on brute force.
# My first instinct was to use a brute-force solution, but after reading the required time complexity,
# I realized I needed a different approach and started over.
# Learning the XOR properties (a ^ a = 0 and a ^ 0 = a) made the solution much simpler.
# I reviewed a few guides to better understand why XOR works so well for this problem.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
                        #nums = [2,2,1]
        res = 0         # res ^ 0 = res
        for n in nums:
            res = n ^ res
        return res
