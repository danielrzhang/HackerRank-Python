if __name__ == '__main__':
    n = int(input())
    
    lst = []
    
    for i in range(n):
        line = str(input()).split()
        
        if len(line) == 3:            
            lst.insert(int(line[1]), int(line[2]))
           
        elif len(line) == 2:       
            if line[0] == "append":
                lst.append(int(line[1]))
                
            elif line[0] == "remove":
                lst.remove(int(line[1]))
                
        else:
            if line[0] == "print":
                print(lst)
                
            elif line[0] == "sort":
                lst.sort()
                
            elif line[0] == "pop":
                lst.pop()
                
            else:
                lst.reverse()