# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:26:26 2020

@author: Ranit
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
nmtupleOrder = input()
# print(nmtupleOrder)
students = namedtuple("students", nmtupleOrder)
# print(students)
sum = 0.0
for i in range(n):
    inpStudentInfo = list(map(str,input().split()))
    # print(inpStudentInfo)
    nStudentInfo = students._make(inpStudentInfo)
    # print(nStudentInfo)
    sum += int(nStudentInfo.MARKS)

print("{:.2f}".format(sum/n))


"""
Sample Input:
-----------------------------------------------
TESTCASE 01

5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
TESTCASE 02

5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5

Sample Output
------------------------------------------------
TESTCASE 01

78.00
TESTCASE 02

81.00
"""