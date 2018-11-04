#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n,req={0:0,1:1,2:2,3:4}):
    if n in req:
        return req[n]
    req[n] = stepPerms(n-3)+stepPerms(n-2)+stepPerms(n-1)
    return req[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
