n = int(input())

binary = bin(n)[2:]

counter = 0

contains = "1"
while True:
    if contains in binary:
        counter += 1
        contains += "1"
        
    else:
        break
    
print(counter)