def wrap(string, max_width):
    newString = ""
    
    counter = 0
    for i in string:
        newString += i
        counter += 1
        
        if counter % max_width == 0:
            newString += "\n"
        
    return newString

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)