print("Welcome to Quan Ly Diem So. ente the list of grades, separate by space")

gradeList = input(">>> "). split()
#1
sum = 0
for i in range(len(gradeList)):
    gradeList[i] = int(gradeList[i])
    sum+=gradeList[i]

averageGrade = sum/len(gradeList)
print(f"Average: {averageGrade}")
#2
gradeList.sort()
gradeSecond = -2
while True:
    if gradeList[-1] > gradeList[gradeSecond]:
        print(gradeList[gradeSecond])
        break

    else:
        gradeSecond-=1

#3
for j in range (len(gradeList)):
    if gradeList[j] <= 5:
        gradeList[j] = 9
    else:
        break   #The list was sorted, so we should stop here when j>5

print(gradeList)

