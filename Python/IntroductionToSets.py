def average(array):
    newSet = set(array)
    
    return "%.3f" % (sum(newSet) / len(newSet))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)