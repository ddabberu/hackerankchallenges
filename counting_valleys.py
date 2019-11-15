'''
Count the valleys problem
example: DDUUDDUDUUUD, valleys are 2, UDDDUDUU valleys are 1, we can use same for peaks
'''

import sys,os,random,re,math

# Complete the countingValleys function below.
# used a regex pattern starts with a d and d+ with a step up U
# return number of entries in the tuple
def countingValleys(n, s):
    #need look for dd*u pattern and count
    valleys=re.findall(r'dd+u',s,re.I)
    print(len(valleys))
    return len(valleys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()

