# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 23:22:30 2022

@author: Mukarram ali
"""
from funcs import RandomArray
from funcs import SelectionSort
from funcs import SaveSelectionSort_in_File
import time



arr=RandomArray(20000)
start=time.time()

arr2=SelectionSort(arr, 0,len(arr))

end=time.time()
print(end-start)
SaveSelectionSort_in_File(arr2)