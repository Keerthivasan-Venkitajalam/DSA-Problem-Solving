class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0 #pointer to track the position for non-zero elements
        for right in range(len(nums)): #iterate through the list using right pointer
            if nums[right]: #check if the current element is non-zero
                nums[left], nums[right]=nums[right], nums[left] #swap non-zero element with left pointer position
                left +=1 #move left pointer to the next position
        return nums #return modified list (though function modifies in-place)
