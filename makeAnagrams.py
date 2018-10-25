#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    req_chars = []
    #dict1 = defaultdict(int)
    #dict2 = defaultdict(int)
    for char in a:
        if char in b and char not in req_chars:
            req_chars.append(char)
    print(req_chars)
    dict1 = Counter(a)
    print(dict1)
    dict2 = Counter(b)
    print(dict2)
    result = len(a) + len(b)
    print('result is '+str(result))
    for char in req_chars:
        result -= dict1[char]
        result -= dict2[char]
        result += 2 * abs(dict1[char]-dict2[char])
    return (result)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)
    #fptr.write(str(res) + '\n')

    #fptr.close()
