def Round3f(num):
    #
C = int(input())
result = []
for n in range(C):
    nlist = list(map(int,input().split()))
    total = 0
    for i in range(1,len(nlist)):
        total +=nlist[i]
    average = total/nlist[0]
    Pstudent = [x for x in nlist if x>average]
    result.append(len(Pstudent)/nlist[0])
for k in range(len(result)):
    print(str(format(result[k]*100,".3f"))+"%")