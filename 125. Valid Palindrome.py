# Mauricio Garcia
# This problem gave me another opportunity to practice the two-pointer technique, which I had previously used in Two Sum II.
# It is a very powerful approach because it allows both ends of the string to be processed simultaneously in linear time.
# The main challenge here is correctly skipping non-alphanumeric characters while performing a case-insensitive comparison.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            if not s[leftPointer].isalnum():
                leftPointer += 1
                continue    
            elif not s[rightPointer].isalnum():
                rightPointer -= 1
                continue
            elif s[leftPointer].lower() != s[rightPointer].lower():
                return False
            leftPointer += 1
            rightPointer -= 1
        return True