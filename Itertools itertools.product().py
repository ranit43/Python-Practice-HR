"""
Created on 4/2/2020 6:27 PM

@author: Ranit
"""
from itertools import  product
totList = []
totList.append(list(map(int, input().split())))
totList.append(list(map(int, input().split())))
prodTotList = list(product(*totList))
# print(list(prodTotList))
for x in prodTotList:
    print(x, end=" ")

"""
Sample Input

 1 2
 3 4
Sample Output

(1, 3) (1, 4) (2, 3) (2, 4)
 
 """