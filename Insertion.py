# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:57:43 2022

@author: Mukarram ali
"""

from funcs import RandomArray
from funcs import InsertionSort
from funcs import Save_in_File

import time


arr=[]
arr=RandomArray(60000)
start=time.time()
arr2=InsertionSort(arr, 0, len(arr))
end=time.time()
print(end-start)
Save_in_File(arr2)

