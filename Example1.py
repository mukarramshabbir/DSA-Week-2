# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:43:01 2022

@author: Mukarram ali
"""

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

import time
start=time.time()
ans=factorial(1500)
end=time.time()
runtime=end-start
print(runtime)