# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 22:28:28 2022

@author: Mukarram ali
"""
from funcs import MergeSort
from funcs import RandomArray
from funcs import SaveMergeSort_in_File
import time


A=RandomArray(1000000)
#merge_sort(A)
start=time.time()

MergeSort(A, 0,len(A)-1)
end=time.time()
print(end-start)
SaveMergeSort_in_File(A)
#Merge(A,0,4,9)
#print(A)