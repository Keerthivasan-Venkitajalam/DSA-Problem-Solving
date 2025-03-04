# class HeapItem:
#     def __init__(self,word:str,count:int)->None:
#         self.word=word
#         self.count=count
    
#     def __lt__(self,to_compare)->bool: #less than function as default heap in py is minHeap
#         if self.count==to_compare.count:
#             return self.word>to_compare.word
#         return self.count<to_compare.count

# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         words_counts=collections.Counter(words) #map between each word and count of that word
#         heap=[]

#         #populating the empty heap
#         for word, count in words_counts.items():
#             item=HeapItem(word,count)

#             #if heap doesn't have k elements in it, then we just put it in there without any popping
#             if len(heap)<k:
#                 heapq.heappush(heap,item) #pushing current item
#             else: # as default heap in py is minHeap
#                 if item>heap[0]:
#                     heapq.heappop(heap)
#                     heapq.heappush(heap,item)
#         res=[]

#         #k times pop
#         while k:
#             current=heapq.heappop(heap)
#             res.append(current.word)
#             k-=1
#         return list(reversed(res))

# # Time Complexity - O(n log(k)) => n words to process and k is the size of the heap.
# # Space Complexity - O(n) for mapping and O(n) for the heap and asymptotically O(n)

# Approach 2 - Tuple instead of HeapItem. Tuple is set as (-count, word). Tuple comparison is resolved on the first element. If first element is equal, then it'll starts to compare the second element, and it happens that it's a minHeap so it's already in lexicographical order.
import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words)  #count frequency of words
        heap = []

        #populate heap with tuples (-count, word) to maintain order
        for word, count in word_counts.items():
            heapq.heappush(heap, (-count, word))

        #extract top k frequent words
        return [heapq.heappop(heap)[1] for _ in range(k)]
