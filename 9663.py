N = int(input())
row = [0] * N
result = 0

#내 윗줄에 나와 겹치는 라인에 퀸이 있는지
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
           
#재귀
def dfs(x):
    global result
    
    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)

dfs(0)
print(result)