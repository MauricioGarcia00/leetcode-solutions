# Mauricio Garcia
# Although this is classified as a medium problem, I found it closer to an easy one once I understood the main idea.
# The solution is based on maintaining the best running sum while updating the maximum sum seen so far.
# Whenever the current sum becomes negative, it is better to start a new subarray than continue carrying a loss.
# The implementation is surprisingly concise, and this problem is a great introduction to Kadane's Algorithm.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumaActual = 0
        sumaMaxima = nums[0]
        for n in nums:
            if sumaActual < 0:
                sumaActual = 0
            sumaActual += n
            sumaMaxima = max(sumaActual, sumaMaxima)
        return sumaMaxima
 