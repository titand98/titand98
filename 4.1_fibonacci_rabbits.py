#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:46:13 2021

@author: sayakdutta
"""
months = int(input('Enter the no of months::'))
off = int(input('Enter the no of childeren produced each gen::'))
def fib(months,off):
    parent,child = 1, 1
    for itr in range (months-1):
        child, parent = parent ,parent +(child* off)
    return child
print(fib(months,off))    