# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 07:54:30 2020

@author: Ranit
"""
from tabulate import tabulate

Val = input()

print("Last 3 digit of your roll number is: ", Val)

Val = int(Val)

singleData = []
wholeDataSet = []

fibre = [Val % 10, Val % 13, Val % 5, Val % 17, Val % 3]
energy = [(Val % 19) + 9, (Val % 33) + 12, (Val % 15) + 13, (Val % 16) + 23, (Val % 21) + 24]
fat = [(Val + 6) % 5, (Val + 8) % 5, (Val + 34) % 5, (Val + 18) % 5, (Val + 37) % 5]
protein = [(Val % 31) - 9, (Val % 32) - 6, (Val % 33) - 5, (Val % 34) - 2, (Val % 35) - 1]
priceOfOats = [Val + 100, Val + 300, Val + 500, Val + 700, Val + 200]

for i in range(5):
    singleData.append(fibre[i])
    singleData.append(energy[i])
    singleData.append(fat[i])
    singleData.append(protein[i])
    singleData.append(priceOfOats[i])

    wholeDataSet.append(singleData)  # adding the data to the data set
    print(wholeDataSet)
    print(singleData)
    singleData.clear()

print("single Data ", singleData)
print("AllData  ", wholeDataSet)

print(tabulate(wholeDataSet, headers=["Fibre (gm)", "Energy (kCal)", "Fat (gm)", "Protein (gm)", "Price of Oats (BDT)"]))
