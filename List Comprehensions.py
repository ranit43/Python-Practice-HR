# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:31:01 2020

@author: rda
"""

x = int(input().strip())
y = int(input().strip())
z = int(input().strip() )
n = int(input().strip() )
result = []
for i in range(x + 1):
    for j in range( y + 1):
        for k in range( z + 1):
            if (i + j + k) != n :
                result.append([i, j, k]) 


print(result)

result = [ [i, j, k] for i in range(x + 1) for j in range( y + 1) for k in range( z + 1) if ( ( i + j + k ) != n )]
print(result)