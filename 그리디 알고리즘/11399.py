#11399번
#input : 사람 수 N
#input2 : 각 사람이 인출하는데 걸리는 시간 N개(한줄에)
#return : 각 사람이 돈을 인출하는데 걸리는 시간 합

N = int(input())
times = input().split(" ")
times = list(map(int,times))

times.sort()

total = 0
count = 0
for i in times:
    count = int(i)+count
    total = count+total
    
print(total)