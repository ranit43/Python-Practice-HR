# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:24:38 2020

@author: Ranit
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
from collections import OrderedDict
ordDict = OrderedDict()
n = int(input())
for i in range(n):
    itemName, itemPrice = input().rsplit(" ", 1)
    itemPrice = int(itemPrice)
    print(itemName, itemPrice)
    if itemName in ordDict:
        ordDict[itemName] = ordDict[itemName] + itemPrice
    else:
        ordDict[itemName] = 0
        
"""
# your code goes here
roll = int('001')  # if your roll 191-115-233
m = (roll % 10)

element = []
idx = 0
element.append((roll + m) % 33)
element.append(int(roll / m) + 17)
element.append(roll + (55 % m))
element.append(22 * m + 3)
element.append((roll - (2 * m)))
element.append(roll + 10 * m)
element.append((roll % m) + 123)
element.append((33 + m) * 2)
element.append((roll % 15 + m))
element.append(m * (roll - 15))
element.append(roll - 22)

print(element)
