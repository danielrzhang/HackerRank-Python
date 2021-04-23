if __name__ == '__main__':
    
    n = int(input())
    scoreList = []
    nameAndScoreList = []
    answerList = []
    
    for i in range(n):
        name = input()
        score = float(input())
         
        if (score not in scoreList):
            scoreList.append(score)
        nameAndScoreList.append([name, score])
         
    scoreList.sort()
    secondSmallestScore = scoreList[1]
    
    for i in nameAndScoreList:        
        if (i[1] == secondSmallestScore):
            answerList.append(i[0])
    
    answerList.sort() 
    
    for i in answerList:
        print(i)   
         
    
    
        
        
        
        