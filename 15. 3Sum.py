class Solution:

    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:########### 
                continue

            leftPointer = i + 1
            rightPointer = len(nums) - 1

            while leftPointer < rightPointer:
                currentSum = nums[i] + nums[leftPointer] + nums[rightPointer]

                if currentSum == 0:
                    result.append(
                        [nums[i], nums[leftPointer], nums[rightPointer]]
                    )
                    leftPointer += 1
                    rightPointer -= 1

                    while (
                        leftPointer < rightPointer
                    and nums[leftPointer] == nums[leftPointer - 1]
                    ):
                        
                        leftPointer += 1
                    while (
                        leftPointer < rightPointer 
                        and nums[rightPointer] == nums[rightPointer + 1]
                        ):
                        rightPointer -= 1

                elif currentSum < 0:
                    leftPointer += 1
                else:
                    rightPointer -= 1

        return result
        
        
        