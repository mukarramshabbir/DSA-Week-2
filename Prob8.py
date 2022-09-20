# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 03:50:08 2022

@author: Mukarram ali
"""
    
from funcs import ReadfromFileProb8
from funcs import InsertionSort
from funcs import MergeSortProb8
from funcs import ShuffleArray
import time

arr=ReadfromFileProb8()
#------------before shuffling-----------
dup_arr1=arr
start=time.time()
InsertionSort(dup_arr1, 0, len(dup_arr1))
end=time.time()
print("Insertion Sort Time:",end-start)
print(dup_arr1)
dup_arr2=arr
mergeStart=time.time()
MergeSortProb8(dup_arr2, 0, len(arr)-1)
mergeEnd=time.time()
print("Merge Sort Time:",mergeEnd-mergeStart)
print(dup_arr2)
#-------------------------------------
#-----------After shuffling-----------
dup_arr3=ShuffleArray(arr, 0, len(arr)-1)
print(dup_arr3)
dup_arr1=dup_arr3
InsertionSort(dup_arr1, 0, len(dup_arr1))
end=time.time()
print("Insertion Sort Time:",end-start)
print(dup_arr1)
dup_arr2=dup_arr3
mergeStart=time.time()
MergeSortProb8(dup_arr2, 0, len(arr)-1)
mergeEnd=time.time()
print("Merge Sort Time:",mergeEnd-mergeStart)
print(dup_arr2)
#---------------------------------------