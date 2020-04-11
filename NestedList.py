# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:23:59 2020

@author: Ranit
"""


if __name__ == '__main__':
    lowest = secondLowest = 100000000
    studentList = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        studentList.append([name, score]);
        
        if score > lowest:
            secondLowest = lowest
            lowest = score
        elif  score < secondLowest and lowest < score :
            secondLowest = score

    
    studentListofSecondLowest = []
    for x in studentList:
        if x[1] == secondLowest:
            studentListofSecondLowest.append(x[0])
            
        
    studentListofSecondLowest.sort()
    for x in studentListofSecondLowest:
        print(x)


"""
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""