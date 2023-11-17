#!/usr/bin/env python3
from math import factorial

def pascal_triangle(n):
    for i in range(n):
        for j in range(i+1):
            return(factorial(i)//(factorial(j)*factorial(i-j)))