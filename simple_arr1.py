"""
Given an array of integers, find the sum of its elements.
For examp le, if the array ar =  [1,2,3], 1+2+3=6  so return 6
Function Description

simpleArraySum has the following parameter(s):
ar: an array of integers

Input Format

The first line contains an integer, n denoting the size of the array
The second line contains n space-separated integers represengting the array's elements

Constraints

0 < n, ar[i] <= 1000

Output Format
Print the sum of the array's elements as a single integer.

Sample Input
6
1 2 3 4 10 11

Sample Output
31

Explanantion

We print the sum of the array's elements: 1 + 2 + 3 + 4 + 10 + 11 = 31
"""

import os
import sys

#
# Complete the simpleArraySum function below.
#


def simpleArraySum(ar):
    #
    # Write your code here.
    #
    sum = 0
    for element in ar:
        # sum = sum + element
        sum += element
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # first line gets count
    ar_count = int(input())
    # second line splits into an element and casts the integer puts it into list
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
