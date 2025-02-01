class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#2 pointers approach
        left,right=0,len(numbers)-1 #left and right pointers initialized for 2 pointers approach
        while left<right:
            currentSum=numbers[left]+numbers[right]
            if currentSum>target:
                right-=1 #shift right pointer to one index left
            elif currentSum<target:
                left+=1 #shift left pointer to one index right
            else:
                return[left+1,right+1]
        return[]
#brute Force Approach
        #iterate through each element in the list
#        for i in range(len(numbers)):
            #compare it with every other element in the list
#            for j in range(i+1,len(numbers)):
                #If the sum of the two elements equals the target
#                if numbers[i]+numbers[j]==target:
                    #Return their indices (1-based indexing as required in the problem)
#                    return [i+1,j+1]
#        return []
