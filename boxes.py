boxSize = []
packageVol = []
answers = []
n = int(input())
for i in range (n):
    boxl,boxw,boxh = [int(x) for x in input().split()] 
    boxsizes = boxl * boxw * boxh
    boxSize.append(boxsizes)
boxSize.sort()
m = int(input())        
for i in range(m):
    packagel,packagew,packageh = [int(x) for x in input().split()] 
    packageVolume = packagel * packagew * packageh
    packageVol.append(packageVolume)
for i in range(m):
    answers.append(-1)
    for j in range(n):
        if (packageVol[i] <= (boxSize[j])):
            answers[i] = boxSize[j]
            break
        else:
            continue
        break
for i in range(m):
    if (answers[i] == -1):
        print ("Item does not fit.")
    else:
        print(answers[i])
