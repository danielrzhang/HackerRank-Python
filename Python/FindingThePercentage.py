if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    tempList = student_marks.get(query_name)
    
    counter = 0
    
    for i in tempList:
        counter += i
        
    print("%.2f" % (counter / len(tempList)))
    
    
        