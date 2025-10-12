def calculator(score):
    sum = 0
    for i in range(1, len(score)):
        sum+=int(score[i])
    sum+=int(score[-1])*2
    average = sum/(len(score)+1)
    return average

scoreList = input().split()
output = calculator(scoreList)
print(output)