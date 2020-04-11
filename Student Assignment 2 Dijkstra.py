# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:11:13 2020

@author: Ranit
"""
#r = int("064") #if your roll 191-115-001 

# give the last 3 digit of your roll numer as input
# so if your  191-115-001 then input 001 in the input section and then run
r = input()

print("Last 3 digit of your roll number is: ",  r)

r = int(r) 

if r%10 == 0:
	m = r % 9
else :
	m = r % 10
 
print("r = ", r)
print("m  = ", m)

print("Edges of the graph is given below: ")
print("A -> B  ", ( (r % m) +2 ))
print("A -> D  ", ( r% (m+1) ) + 1)
print("C -> B  ", ( r % (m+3) ) + 2*m )
print("D -> C  ", ( r % (m+2) ) + (2*m-1))
print("B -> E  ", ( r + m + 2 ))
print("C -> F  ", ( r + m ))
print("D -> G  ", ( r + m + 1 ))
print("G -> E  ", ( r + 2 ))
print("E -> F  ", ( r + 1 ))
print("F -> H  ", (( r + m ) % m ) + m )
print("E -> H  ", (( r + m ) % m ) + (m+2))
print("G -> H  ", (( r + m ) % m ) + (m+3))
print("B -> I  ", ( (r+4) % m ) + 4)
print("E -> I  ", ( (r+13) % (m + 1))+ 3)
print("A -> C  ", ( (r+15) % (m + 2))+ 4)
print("I -> H  ", (( r + m ) % m ) + (m+4))

print("Source is A and find the shortest path for E F G and H from A and print what are shortest distance to them from A.")
print("Also, print the paths for them ( how you reached to them).")
print("That means starting from A which set of nodes were included in the shortest path to H.")