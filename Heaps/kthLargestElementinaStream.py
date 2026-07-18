# You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)    # returns the kth largest element in the pool of test scores so far.

# Solution:
# 1. We can use a min heap to keep track of the kth largest element.
# 2. We can use a heapq.heapify to initialize the heap.
# 3. We can use a heapq.heappush to add a new element to the heap.
# 4. We can use a heapq.heappop to remove the smallest element from the heap.
# 5. We can use a heapq.heappushpop to add a new element to the heap and remove the smallest element from the heap.

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Time complexity: O(log n) for the add method.
# Space complexity: O(n) for the heap.