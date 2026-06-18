# Mauricio Garcia
# This problem was a good exercise for practicing array traversal and adjacent-element comparisons.
# The sorted property of the array makes the solution fairly intuitive and introduces an interesting in-place modification challenge.
# Personally, I found the problem enjoyable, although many people in the community seem to dislike it.
# I think additional edge cases could make the problem more interesting and test implementations more thoroughly.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        array = range(len(nums)-1) 
        counter = 1
        
        for i in (array):
            if nums[i] < nums[i+1]:
                # we check if there are no more repetitions, and we add one to the counter
                #and we use the counter - 1  as as the slot where we place the number
                # nums = [0,1,1,1,2,3,3,4]

                # nums = [0,1]
                
                 
                nums[counter] = nums[i+1] 
                counter += 1  
                
            if nums[i] == nums[i+1]:
                pass
        del nums[counter :]
