class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#Hash map 
        preHashmap={} #value:index

        for i,n in enumerate(nums):
            diff=target-n
            if diff in preHashmap:
                return[preHashmap[diff],i] #solution -> pair of indices
            preHashmap[n]=i #update of solution if solution is not found as we are guarenteeing the presence of the solution
        return[]

#Brute Force
#iterate through each element in the list
#        for i in range(len(nums)):
            #compare it with every other element in the list
#            for j in range(i + 1, len(nums)):
                #if the sum of the two elements equals the target
#                if nums[i] + nums[j] == target:
                    #return their indices as the solution
#                    return [i, j]

#Hash Map Approach -> Space O(n) => Time O(n)
#Brute Force Approach -> Space O(1) => Time O(n*n)
