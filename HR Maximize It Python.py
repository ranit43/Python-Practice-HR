"""
Created on Wed Apr 1 12:54:38 2020

@author: Ranit
"""
from itertools import product

n, modVal = map(int, input().split())
# print("n", n)
# print("m", m)
arrCollection = []
for i in range(n):
    arrCollection.append(list(map(int, input().split()))[1:])

carSetArrCollection = list(product(*arrCollection))

sumList = []
for x in carSetArrCollection:
    sumList.append(sum([(val * val) for val in list(x)]) % modVal)

print(max(sumList))

"""
Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output
206

Input (stdin)
Download
7 588
7 3729019 6589533 9497010 1956867 4094190 1785314 9410145
7 6241592 9563118 4665482 3629252 418388 795859 816643
7 7924805 2362312 7324277 3672134 1005196 8234278 9131319
7 9978282 1999589 9658103 7451768 20958 1718778 3850870
7 4802255 5530524 3732809 8531273 2120056 3229818 488140
7 8730597 7531483 2414636 7488541 7094601 7080117 3634144
7 7512988 392327 4450786 7954145 2754638 4291414 1626278

Expected Output
Download
587

"""
