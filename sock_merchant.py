'''sock merchant problem
given an number of socks and array of colors for each sock, pair them up
'''
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
#my solution, using the set method to uniquely identify the colors, and run a count of each :)
def sockMerchant(n, ar):
    uniq_colors= set(ar)
    print(uniq_colors)
    pairs=0
    for i in uniq_colors:
        pair=(int)(ar.count(i)/2)
        print(pair)
        pairs=pairs+ pair
    print(pairs)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
