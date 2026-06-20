#Mauricio Garcia
#Initial approach: brute-force comparison of every pair of elements.
#This solution resulted in O(n²) time complexity and exceeded the time limit
#on large test cases in LeetCode.


#I then optimized the solution by using a hash-based approach, reducing the
#average time complexity to O(n). Beyond meeting the performance requirements,
#this optimization also provided an opportunity to practice selecting more
#efficient data structures and algorithms.
#class Solution:
#    def containsDuplicate(self, nums: List[int]) -> bool:
#        for i in range(len(nums)):
#            for j in range(i+1,len(nums)):
#                if nums[i] == nums[j]:
#                    return True
#        return False



# After re-evaluating my initial approach, I developed a more efficient solution.
# This problem encouraged me to think from a different perspective and reinforced
# the importance of reconsidering assumptions when solving algorithmic challenges.
# I particularly enjoyed the problem because it highlighted the value of iterative
# problem-solving and optimization.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in range(len(nums)): # We make a whole for loop analyzing the whole array

            if nums[i] in h:    #We found a repetition! therefore it is True and we don't care no more
                return True
                
            if nums[i] not in h:    #We check if the value in NUMS is NOT IN HASHMAP and then, we add it into the hashmap!
                h[nums[i]] = i




        return False # If we finished this loop, and we don't get into this condition, therefore, there are no repetitions, and we should return False
            