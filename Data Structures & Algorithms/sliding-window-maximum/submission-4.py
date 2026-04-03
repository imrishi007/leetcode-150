class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))

            if i >= k - 1:
                #If the element in the top of heap has an index lower than the window's first element we pop it
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                
                ans.append(-heap[0][0])
                
        return ans
    