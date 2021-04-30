n, m = map(int, input().split())

countDesign = 1
countDash = (m - (countDesign * 3) ) // 2

for i in range(n // 2):
    print((countDash - (i * 3)) * "-" + (countDesign + (i * 2)) * ".|." + (countDash - (i * 3)) * "-")
    
print(((m - 7) // 2) * "-" + "WELCOME" + ((m - 7) // 2) * "-")

for i in range((n // 2) - 1, -1, -1):
    print((countDash - (i * 3)) * "-" + (countDesign + (i * 2)) * ".|." + (countDash - (i * 3)) * "-")
    

    