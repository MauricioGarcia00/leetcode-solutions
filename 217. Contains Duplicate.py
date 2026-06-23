# Mauricio Garcia
# This problem requires understanding how the XOR operator behaves.
# My first idea was to use a brute-force approach, but after reading the constraints more carefully,
# I realized the time complexity would not be ideal and decided to rethink the solution.
# XOR works perfectly here because a number XORed with itself cancels out to 0,
# leaving only the number that appears once.
# I reviewed a few guides to better understand the XOR properties before implementing the solution.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #nums = [2,2,1]
        res = 0  # res ^ 0 = res
        for n in nums:
            res = n ^ res
        return res
