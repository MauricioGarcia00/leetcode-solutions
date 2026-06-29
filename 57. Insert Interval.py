# Mauricio Garcia
# This was one of the first medium problems I solved, and I struggled with it quite a bit.
# It forced me to slow down and develop my own way of approaching interval problems instead of looking for a direct pattern.
# The key insight was to process the intervals in three stages: add the intervals before the overlap, merge all overlapping intervals, and append the remaining ones.
# Solving this problem gave me a better understanding of how to break a seemingly complex problem into smaller, manageable steps.

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals that end before the new interval starts.
        # These cannot overlap, so we keep them as they are.
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge every interval that overlaps with the new interval.
        # Expand the boundaries of newInterval to cover all overlaps.
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval.
        result.append(newInterval)

        # Add the remaining intervals.
        # Since they start after the merged interval ends,
        # they cannot overlap.
        while i < n:
            result.append(intervals[i])
            i += 1

        return result