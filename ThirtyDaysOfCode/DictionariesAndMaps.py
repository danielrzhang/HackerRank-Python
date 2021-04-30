n = int(input())

dictionary = {}

for i in range(n):
    namePhone = input().split()
    dictionary[namePhone[0]] = int(namePhone[1])
    
while True:
    try:
        query = input()

        if query in dictionary:
            print(query + "=" + str(dictionary.get(query)))
            
        else:
            print("Not found")
    
    except EOFError:
        break
    