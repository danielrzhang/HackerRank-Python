n = int(input())
s = set(map(int, input().split()))

numCommands = int(input())

for i in range(numCommands):
    command = str(input()).split()
    
    if len(command) == 2:
        if command[0] == "remove":
            s.remove(int(command[1]))
            
        elif command[0] == "discard":
            s.discard(int(command[1]))
            
            
    else:
        s.pop()
        
print(sum(s))
        