N = int(input())
sumlist = []
for n in range(N):
    t = input()
    countO = sumOfCount = 0
    for i in range(len(t)):
        if (t[i] == 'X'):
            countO = 0
        else:
            countO +=1
        sumOfCount+=countO
    sumlist.append(sumOfCount)
for j in range(N):
    print(sumlist[j])