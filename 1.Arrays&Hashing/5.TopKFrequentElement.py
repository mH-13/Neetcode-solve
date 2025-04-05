# Problem: 347. Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
#Author: mh0111 


#solution 1 
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyCount = {} # dictionary to store the frequency of each number in nums 

        for num in nums: 
            frequencyCount[num] = frequencyCount.get(num, 0) + 1 # get() returns the value of the key if it is in the dictionary,   otherwise it returns the default value 0 and then we add 1 to it 
            # get(num, 0) + 1 is equivalent to frequencyCount[num] = frequencyCount[num] + 1 if num is in frequencyCount else frequencyCount[num] = 0 + 1

        top_frequent_numbers = sorted(frequencyCount, key = frequencyCount.get, reverse = True)[:k]
        # sorted() returns a list of sorted keys in frequencyCount based on the values in frequencyCount in descending order and then we slice the list to get the first k elements
        # key = frequencyCount.get is a function that returns the value of the key in frequencyCount
        # reverse = True sorts the keys in descending order
        # [:k] slices the list to get the first k elements

        return list(top_frequent_numbers) # returns the list of top k frequent numbers 

# Time complexity: O(NlogN) where N is the length of nums. Counting each number is linear in the size of the list, and we count every number. Sorting the unique numbers in frequencyCount takes O(NlogN) time. 
# Runtime: 96 ms, faster than 93.68% of Python3 online submissions for Top K Frequent Elements.


#solution 2 
#using heapsort 
''' Heapsort is a comparison-based sorting algorithm that uses a binary heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements.

The heap data structure is a complete binary tree that satisfies the heap property. The heap property states that the parent node is greater than or equal to its child nodes (max heap) or the parent node is less than or equal to its child nodes (min heap).

In Python, the heapq module provides a heap data structure that can be used to implement heapsort. The heapq module provides functions like heappush(), heappop(), and heapify() to work with heaps.

heappush(heap, item) - Pushes the item onto the heap.
heappop(heap) - Pops and returns the smallest item from the heap.
heapify(heap) - Transforms the list into a heap in-place.

The heapq module provides a min heap implementation. To use a max heap, we can negate the values and use a min heap.
In this solution, we use a min heap to find the top k frequent elements. We iterate through the keys in frequencyCount and push the tuple (frequencyCount[num], num) into the heap. If the heap size exceeds k, we pop the smallest element from the heap. The result is the k largest elements in the heap.
The time complexity of this solution is O(NlogK) where N is the length of nums. Counting each number is linear in the size of the list, and we count every number. The heap operations take O(logK) time, and we perform these operations for each number in nums. The space complexity is O(N) where N is the length of nums. The space complexity of the dictionary is O(N), and the heap stores at most k elements. '''
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencyCount = {} 
        
        for num in nums: 
            frequencyCount[num] = frequencyCount.get(num, 0) + 1
            
        heap = []
        for num in frequencyCount.keys(): # iterating through the keys in frequencyCount
            
            heapq.heappush(heap, (frequencyCount[num], num)) #frequencyCount[num] is the frequency of num and num is the number itself
            # heappush() pushes the tuple (frequencyCount[num], num) into the heap
            # frequencyCount[num] is the frequency of num and num is the number itself
            # heappush() pushes the tuple into the heap based on the first element of the tuple i.e. frequencyCount[num]
            # if two tuples have the same frequency, then the number itself is used to break the tie 
            
            if len(heap) > k:
                heapq.heappop(heap)



#solution 3
#using bucket sort 
''' Bucket sort is a sorting algorithm that divides the input into a number of buckets, each containing a subset of the input elements. The buckets are then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sort algorithm. Finally, the sorted buckets are concatenated to produce the final sorted output.  
In this solution, we use bucket sort to find the top k frequent elements. We first count the frequency of each number in nums and store it in frequencyCount. We then create a list of buckets, where each bucket represents a frequency count. We iterate through the keys in frequencyCount and place the number in the corresponding bucket based on its frequency. We then iterate through the buckets in reverse order and add the numbers to the result list until we have k elements. The result is the top k frequent elements. ''' 

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencyCount = {} 
        
        for num in nums: 
            frequencyCount[num] = frequencyCount.get(num, 0) + 1
            
        buckets = [[] for _ in range(len(nums) + 1)] 
        # creating a list of buckets where each bucket represents a frequency count. bucket generally means a container that holds a group of items and in this case, the items are the numbers with the same frequency count. 
        
        # the length of the buckets list is len(nums) + 1 because the maximum frequency count can be len(nums) 
        # each bucket is an empty list where we will store the numbers with the corresponding frequency count 
        # the index of the bucket represents the frequency count of the numbers in that bucket and the value at that index is the list of numbers with that frequency count 
        # for example, if buckets[2] = [3, 4], it means that the numbers 3 and 4 have a frequency count of 2
        
        for num in frequencyCount.keys(): # iterating through the keys in frequencyCount
            buckets[frequencyCount[num]].append(num) # placing the number in the corresponding bucket based on its frequency
        
        result = []
        for i in range(len(buckets) - 1, -1, -1): # iterating through the buckets in reverse order
            result.extend(buckets[i]) # adding the numbers to the result list until we have k elements
            if len(result) >= k:
                break

        return result[:k] # returns the top k frequent elements

# Time complexity: O(N) where N is the length of nums. Counting each number is linear in the size of the list, and we count every number. Iterating through the buckets is also linear in the size of the list. 

#Bukcet sort is more efficient than heapsort because it does not require sorting the numbers with the same frequency count and is more efficient.
#Heapsort is more efficient than sorting the dictionary based on the values because it does not require sorting the dictionary based on the values and is more efficient.
#Sorting the dictionary based on the values is less efficient because it requires sorting the dictionary based on the values which is more computationally expensive.

#The most efficient solution is the bucket sort solution because it does not require sorting the numbers with the same frequency count and is more efficient. The heapsort solution is also efficient but requires sorting the numbers with the same frequency count. The sorting solution is less efficient because it requires sorting the dictionary based on the values which is more computationally expensive.

#bucket sort stracture
#buckets = [[] for _ in range(len(nums) + 1)] 
#buckets[0] = []
#buckets[1] = []

#buckets[2] = [3, 4]
#buckets[3] = [2, 5]
