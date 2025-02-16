# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         #direct approach
#         # nums.sort()
#         # return nums[len(nums)-k]
#         k=len(nums)-k #reassigning k to index if sorted
#         def quickSelect(l,r): #2 pointer approach
#             pivot,p = nums[r],l
#             for i in range(l,r): #r is non inclusive py
#                 if nums[i]<=pivot:
#                     nums[p], nums[i] = nums[i], nums[p] #swap with p index
#                     p+=1
#             nums[p], nums[r] = nums[r], nums[p] #nums[pivot], nums[p]
#             if p>k: return quickSelect(r, p-1) #right shifted to left by 1 and left is unchanged
#             elif p<k: return quickSelect(p+1, r) #left becomes p+1 and right is unchanged
#             else: return nums[p]
#         return quickSelect(0,len(nums)-1)

# from typing import List

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k  # Convert k to the index in a sorted array

#         def quickSelect(l, r):
#             pivot, p = nums[r], l
#             for i in range(l, r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]  # Swap
#                     p += 1
#             nums[p], nums[r] = nums[r], nums[p]  # Swap pivot to correct place

#             if p > k: 
#                 return quickSelect(l, p - 1)  # Fix: Correct range for left partition
#             elif p < k: 
#                 return quickSelect(p + 1, r)  # Fix: Correct range for right partition
#             else: 
#                 return nums[p]  # Found the kth largest element

#         return quickSelect(0, len(nums) - 1)

# from typing import List
# import random

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k  # Convert k to the correct index in sorted order

#         def quickSelect(l, r):
#             # Randomly select a pivot to avoid worst-case scenarios
#             pivot_index = random.randint(l, r)
#             nums[pivot_index], nums[r] = nums[r], nums[pivot_index]  # Swap pivot with the last element
            
#             pivot, p = nums[r], l  # Use last element as pivot
#             for i in range(l, r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]  # Swap elements
#                     p += 1
#             nums[p], nums[r] = nums[r], nums[p]  # Swap pivot to final place

#             if p > k:
#                 return quickSelect(l, p - 1)  # Search in the left half
#             elif p < k:
#                 return quickSelect(p + 1, r)  # Search in the right half
#             else:
#                 return nums[p]  # Found the kth largest element

#         return quickSelect(0, len(nums) - 1)

# from typing import List
# import heapq

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return heapq.nlargest(k, nums)[-1]  # Extract the kth largest element

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)  # Push to heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Keep heap size at k
        return min_heap[0]  # Root of heap is the k-th largest element
