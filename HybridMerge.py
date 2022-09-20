# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 05:11:19 2022

@author: Mukarram ali
"""

from funcs import HybridMergeSort
from funcs import RandomArray

size = int(input("Enter the value:"))
arr=RandomArray(size)
HybridMergeSort(arr, 0, len(arr)-1)
print(arr)
