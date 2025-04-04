#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.

def solve(s):
    # Capitalize first letter of each word without affecting words like '12abc'
    return ' '.join(word.capitalize() for word in s.split(' '))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
