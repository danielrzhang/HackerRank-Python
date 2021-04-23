def printString(n):
    string = "";
    
    for i in range(1, n + 1):
        string += str(i)
        
    return string

n = int(input())
print(printString(n))
    
    