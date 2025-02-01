from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr: List[int], left: int, right: int) -> None:
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
        n = len(nums)
        k = k % n  #handle cases where k is greater than the list size
        #reverse the entire array
        reverse(nums, 0, n - 1)
        #reverse the first k elements
        reverse(nums, 0, k - 1)
        #reverse the remaining elements
        reverse(nums, k, n - 1)
