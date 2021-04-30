if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    counter = 0
    maxCounter = -2 ** 31
    
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            counter = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j] + arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1];
            
            if (counter > maxCounter):
                maxCounter = counter
                
    print(maxCounter)