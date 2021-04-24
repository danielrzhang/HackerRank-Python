if __name__ == '__main__':
    s = input()
    
    hasAlnum = False
    hasAlpha = False
    hasDigit = False
    hasLower = False
    hasUpper = False
    
    for i in s:
        if (i.isalnum()):
            hasAlnum = True
            
        if (i.isalpha()):
            hasAlpha = True
            
        if (i.isdigit()):
            hasDigit = True
            
        if (i.islower()):
            hasLower = True
            
        if (i.isupper()):
            hasUpper = True
        
    print(hasAlnum)
    print(hasAlpha)
    print(hasDigit)
    print(hasLower)
    print(hasUpper)