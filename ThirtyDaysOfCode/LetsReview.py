n = int(input())

for i in range(n):
    string = str(input())
    
    evenString = ""
    oddString = ""
    for j in range(len(string)):
        if (j % 2 == 0):
            evenString += string[j]
        
        else:
            oddString += string[j]
    
    print(evenString + " " + oddString)