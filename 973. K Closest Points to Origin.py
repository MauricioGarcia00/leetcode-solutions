# Mauricio Garcia
# This problem introduced me to the Min Heap data structure and how it can efficiently retrieve the closest elements.
# Instead of sorting every point, I stored each point along with its squared distance from the origin inside a min heap.
# Since the heap always keeps the smallest distance at the top, I simply removed the closest point k times.
# This problem helped me understand a practical use case for heaps and why they are useful for top-k problems.

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        
        minHeap = []

        for x,y in points:
            distance = (x**2) + (y**2)
            minHeap.append([distance,x,y]) # Heap has [distance, x,y] of every point that we have
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res