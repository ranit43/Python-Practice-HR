# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:58:38 2020

@author: Ranit
"""
from bisect import bisect_left
n, m = map(int, input().split())
# print("n", n)
# print("m", m)
arrInp = list(map(int, input().split()))
aSetInp = list(map(int, input().split()))
bSetInp = list(map(int, input().split()))
# print("arrInp ", arrInp)
aSetInp.sort()
bSetInp.sort()
# print("aSet", aSetInp)
# print("bSet", bSetInp)

totHappiness = 0
for x in arrInp:
    # print(arrInp, "arrinp", x)
    # print("asetInp", bisect_left(aSetInp, x))
    # print("bsetInp", bisect_left(bSetInp, x))
    idxforA = bisect_left(aSetInp, x)
    idxforB = bisect_left(bSetInp, x)
    if idxforA < m and aSetInp[idxforA] == x:
        totHappiness += 1
        # print("asetInp", bisect_left(aSetInp, x))

    if idxforB < m and bSetInp[idxforB] == x:
        totHappiness -= 1
        # print("bsetInp", bisect_left(bSetInp, x))

    # print(x, "in Loop ", totHappiness)

print(totHappiness)

"""
Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
"""
