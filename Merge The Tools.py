"""
Created on 4/1/2020 2:32 PM

@author: Ranit
"""

def merge_the_tools(string, k):
    # your code goes here
    totSubStrings =int(len(string) / k )
    subStrList = []
    idStart= 0
    idEnd = totSubStrings
    for i in range(totSubStrings):
        # print(string[idStart:idEnd].split())
        # subStrList.append(string[idStart:idEnd])
        isPrinted = {}
        for j in string[idStart:idEnd]:
            if isPrinted.get(j) is None:
                print(j, end="")
                isPrinted[j] = 1
        print("")
        idStart = idEnd
        idEnd += k


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


"""
Sample Input

AABCAAADA
3   
Sample Output

AB
CA
AD 
"""