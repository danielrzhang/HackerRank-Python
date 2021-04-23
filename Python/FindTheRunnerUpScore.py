if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    maxNum = max(arr)
    
    while maxNum in arr:
        arr.remove(maxNum)
        
    print(max(arr))
    