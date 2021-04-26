n1 = int(input())
englishSet = set(map(int, input().split()))

n2 = int(input())
frenchSet = set(map(int, input().split()))

newSet = englishSet.union(frenchSet)

print(len(newSet))