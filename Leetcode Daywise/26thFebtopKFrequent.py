# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         class Solution:
#             count={} #hashmap
#             fre=[[] for i in range(len(nums)+1)] #special array ~ count the elements - values ~ list of values occur particular no. of times -- size - input +1
#             for n in nums:
#                 #every value in nums
#                 count[n]=1+count.get(n,0)
#                 #count every value like how many times it occurs
#                 for n,c in count.items():
#                     #every value we count
#                     fre[c].append(n) #index count append n ~ n occurs c number of times and ~ return key value pair we added to the dict
#                 res=[]
# #Array fre is traversed in descending order as we start with most frequent occurances
#                 for i in range(len(fre)-1,0,-1): #descending decrimentation
#                     for n in fre[i]:
#                         res.append(n)
#                         if len(res)==k: #will always be satisfied so no outer return statements
#                             return res


from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # hashmap to count occurrences
        fre = [[] for _ in range(len(nums) + 1)]  # special array to group numbers by frequency
        
        for n in nums:
            # count occurrences of each number
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            # group numbers by their frequency
            fre[c].append(n)
        
        res = []
        # traverse the frequency array in descending order
        for i in range(len(fre) - 1, 0, -1):  # descending decrement
            for n in fre[i]:
                res.append(n)
                if len(res) == k:
                    return res
